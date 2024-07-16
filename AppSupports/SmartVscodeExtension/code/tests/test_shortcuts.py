import unittest

from AppSupports.SmartVscodeExtension.code.tests.BaseTest import BaseTest


class TestShortcuts(BaseTest):
    def test_shortcuts(self):
        case = {
            "q": "我想设置另存为的快捷键。",
            "a": {
                "openAndSetKeybinding": {
                    "arguments": {
                        "commandName": "@:type(x) is str and ('saveas' in x.lower() or 'save as' in x.lower())"
                    }
                }
            },
        }
        self.evaluate(case)
        # Not pass all api needed.argument commandName check fail. pred :workbench.action.saveWorkspaceAs, lambda:type(x) is str and ('saveas' in x.lower() or 'save as' in x.lower()).


if __name__ == "__main__":
    unittest.main()
