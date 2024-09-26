import unittest

from AppSupports.SmartVscodeExtension.code.Benchmark.Test.BaseTest import BaseTest


class TestFindAndReplace(BaseTest):
    def test_replace(self):
        case = {
            "q": "请把所有javascript文件中的所有“abcd”替换成“defg”。",
            "a": {
                "findAndReplace": {
                    "arguments": {
                        "position": "files",
                        "query": "abcd",
                        "replace": "defg",
                        "isRegex": "@:type(x) is bool",
                        "preserveCase": False,
                        "findInSelection": "@:type(x) is bool",
                        "matchWholeWord": False,
                        "isCaseSensitive": "@:type(x) is bool",
                        "filesToInclude": "*.js",
                        "filesToExclude": "",
                    }
                }
            },
        }
        self.evaluate(case)
        # now it call replaceAll command wrongly

    def test_replace_2(self):
        case = {
            "q": "请把当前文件中的所有“abcde”替换成“bc”, 无论大小写。",
            "a": [
                {
                    "findAndReplace": {
                        "arguments": {
                            "position": "editor",
                            "query": "abcde",
                            "replace": "bc",
                            "isRegex": "@:type(x) is bool",
                            "preserveCase": False,
                            "findInSelection": False,
                            "matchWholeWord": "@:type(x) is bool",
                            "isCaseSensitive": False,
                        }
                    }
                },
                {
                    "findAndReplace": {
                        "arguments": {
                            "position": "editor",
                            "query": "[aA][bB][cC][dD][eE]",
                            "replace": "bc",
                            "isRegex": "@:type(x) is bool and x",
                            "preserveCase": False,
                            "findInSelection": False,
                            "matchWholeWord": "@:type(x) is bool",
                            "isCaseSensitive": False,
                        }
                    }
                },
            ],
        }
        self.evaluate(case)

    def test_replace_3(self):
        case = {
            "q": "请把当前文件中的所有“abcde”替换成“replace”, 只替换完整单词。",
            "a": {
                "findAndReplace": {
                    "arguments": {
                        "position": "editor",
                        "query": "abcde",
                        "replace": "bc",
                        "isRegex": "@:type(x) is bool",
                        "preserveCase": False,
                        "findInSelection": False,
                        "matchWholeWord": True,
                        "isCaseSensitive": "@:type(x) is bool",
                    }
                }
            },
        }
        self.evaluate(case)
        # Not pass all api needed.argument(str) query do not equal. pred :\babcde\b, gt :abcde. argument(str) replace do not equal. pred :replace, gt :bc. Lack argument findInSelection.Lack argument isCaseSensitive.


if __name__ == "__main__":
    unittest.main()
