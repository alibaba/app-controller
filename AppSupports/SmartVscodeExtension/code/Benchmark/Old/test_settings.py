import unittest

from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BaseTest


class TestSettings(BaseTest):
    def test_fontsize(self):
        case = {
            "q": "请调小字体",
            "a": {
                "setProperties": {
                    "arguments": {
                        "key2Value": {"editor.fontSize": "@:type(x) is int and x < 20"}
                    }
                },
                "getProperties": {"arguments": {}},
            },
        }
        self.evaluate(case)

    def test_bg_color(self):
        case = {
            "q": "only change the background color to blue.",
            "a": {
                "setProperties": {
                    "arguments": {
                        "key2Value": {
                            "workbench.colorCustomizations": {
                                "editor.background": "@:type(x) is string and == '#0000FF'"
                            }
                        }
                    }
                },
                "getProperties": {"arguments": {}},
            },
        }
        self.evaluate(case)


if __name__ == "__main__":
    unittest.main()
