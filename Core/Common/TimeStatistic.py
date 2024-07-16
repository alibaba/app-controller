import time
from threading import current_thread, Lock

from pandas import DataFrame

from Common.Recoder import Recorder


class TimeStatistic:
    _start_time = {}
    _count = {}
    _total_time = {}
    _lock = Lock()

    @classmethod
    def start(cls, name):
        with cls._lock:
            thread_id = current_thread().ident
            cls._start_time[(thread_id, name)] = time.time()

    @classmethod
    def end(cls, name, recorder: Recorder, output=True):
        with cls._lock:
            thread_id = current_thread().ident
            if (thread_id, name) in cls._start_time:
                inc_time = time.time() - cls._start_time[(thread_id, name)]
                cls._add_time(name, inc_time)
                del cls._start_time[(thread_id, name)]
            else:
                raise RuntimeError("end but no start")

            if output:
                recorder.info(f"{name} cost time: {inc_time}")

    @classmethod
    def _add_time(cls, name, inc_time):
        if name not in cls._total_time:
            cls._total_time[name] = 0
            cls._count[name] = 0
        cls._total_time[name] += inc_time
        cls._count[name] += 1

    @classmethod
    def add_time(cls, name, inc_time):
        with cls._lock:
            cls._add_time(name, inc_time)

    @classmethod
    def clear(cls):
        cls._start_time = {}
        cls._count = {}
        cls._total_time = {}
        cls._lock = Lock()
