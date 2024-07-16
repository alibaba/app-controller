import unittest

from AppSupports.SmartVscodeExtension.code.tests.BaseTest import BaseTest


class CommandTest(BaseTest):
    def test_1(self):
        case = {
            "q": "go to line 35 in the current file.",
            "a": {
                "executeCommand": {
                    "arguments": {"commandId": "workbench.action.gotoLine"}
                }
            },
        }
        self.evaluate(case)

    def test_2(self):
        case = {
            "q": "navigate back to the previous location.",
            "a": {
                "executeCommand": {
                    "arguments": {"commandId": "workbench.action.navigateBack"}
                }
            },
        }
        self.evaluate(case)
        # Use necessary or non-existed api 'getProperties'. Think add this api or not.Use necessary or non-existed api 'openKeybindingSettings'. Think add this api or not.Not pass all api needed.

    def test_3(self):
        case = {
            "q": "comment out the selected block",
            "a": {
                "executeCommand": {
                    "arguments": {"commandId": "editor.action.blockComment"}
                }
            },
        }
        self.evaluate(case)

    def test_4(self):
        case = {
            "q": "duplicate the current line or selection.",
            "a": [
                {
                    "executeCommand": {
                        "arguments": {"commandId": "editor.action.copyLinesDownAction"}
                    }
                },
                {
                    "executeCommand": {
                        "arguments": {"commandId": "editor.action.duplicateSelection"}
                    }
                }]
        }
        self.evaluate(case)
        # Not pass all api needed.argument(str) commandId do not equal. pred :editor.action.duplicateSelection, gt :editor.action.copyLinesDownAction.

    def test_5(self):
        case = {
            "q": "collapse all sections in the current JSON file.",
            "a": {"executeCommand": {"arguments": {"commandId": "editor.foldAll"}}},
        }
        self.evaluate(case)
        # Not pass all api needed.argument(str) commandId do not equal. pred :list.collapseAll, gt :editor.foldAll.

    def test_6(self):
        case = {
            "q": "format current file.",
            "a": {"formatCurrentFile": {"arguments": {"onlySelectedText": False}}},
        }
        self.evaluate(case)

    def test_7(self):
        case = {
            "q": "close the sidebar on the left.",
            "a": [{"executeCommand": {"arguments": {"commandId": "workbench.action.toggleSidebarVisibility"}}},
                  {"executeCommand": {"arguments": {"commandId": "workbench.action.closeSidebar"}}}]
        }
        self.evaluate(case)

    def test_8(self):
        case = {
            "q": "connect to a remote SSH server.",
            "a": {"createRemoteSSHServerConnect": {"arguments": {}}},
        }
        self.evaluate(case)
        # Use unnecessary or non-existed api 'getProperties'. Think add this api or not.


if __name__ == "__main__":
    unittest.main()
