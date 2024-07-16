import unittest

from AppSupports.SmartVscodeExtension.code.tests.BaseTest import BaseTest


class TestExtension(BaseTest):
    def test_install(self):
        case = {
            "q": "我想安装jupyter notebook的插件",
            "a": {
                "getInstalledExtensions": {
                    "arguments": {
                        "filterKey": "@:type(x) is str and 'jupyter' in x.lower()"
                    },
                    "result": "",
                },
                "requireUserToInstallExtension": {
                    "arguments": {
                        "extensionName": "@:type(x) is str and 'jupyter' in x.lower()"
                    }
                },
            },
        }
        self.evaluate(case)

    def test_theme_light(self):
        case = {
            "q": "I want use the light theme.",
            "a": [
                {
                    "listThemes": {"arguments": {}},
                    "applyTheme": {
                        "arguments": {
                            "themeId": "@:type(x) is str and 'light' in x.lower()",
                            "uiTheme": "@:type(x) is str",
                        }
                    },
                },
                {
                    "executeCommand": {
                        "arguments": {
                            "commandId": "workbench.action.toggleLightDarkThemes"
                        }
                    }
                },
            ],
        }
        self.evaluate(case)

    def test_theme_dark(self):
        case = {
            "q": "I want use the dark theme.",
            "a": [
                {
                    "listThemes": {"arguments": {}},
                    "applyTheme": {
                        "arguments": {
                            "themeId": "@:type(x) is str and 'dark' in x.lower()",
                            "uiTheme": "@:type(x) is str",
                        }
                    },
                },
                {
                    "executeCommand": {
                        "arguments": {
                            "commandId": "workbench.action.toggleLightDarkThemes"
                        }
                    }
                },
            ],
        }
        self.evaluate(case)

    def test_auto_saving(self):
        case = {
            "q": "enable auto-saving of files every 5 seconds",
            "a": {
                "setProperties": {
                    "arguments": {
                        "key2Value": {
                            "files.autoSave": "afterDelay",
                            "files.autoSaveDelay": 5000,
                        },
                        "onGlobal": "@:True",
                    }
                },
                "getProperties": {"arguments": {}},
            },
        }
        self.evaluate(case)


if __name__ == "__main__":
    unittest.main()
