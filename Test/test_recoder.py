from unittest import TestCase

from Common.Config import Config
from Common.Recoder import Recorder


class TestRecorder(TestCase):
    def setUp(self):
        self.config: Config = Config("../config.ini")

    def test_1(self):
        id1 = "aaa"
        id2 = "bbb"
        recorder1 = Recorder(self.config, id1)
        recorder2 = Recorder(self.config, id2)
        recorder1.info("aaa")
        recorder2.info("bbb")
