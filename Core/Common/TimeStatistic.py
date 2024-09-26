import time


class TimeStatistic:
    def __init__(self):
        self._start_time = {}
        self._count = {}
        self._total_time = {}

    def start(self, name):
        self._start_time[name] = time.time()

    def end(self, name):
        if name in self._start_time:
            inc_time = time.time() - self._start_time[name]
            self._add_time(name, inc_time)
            del self._start_time[name]
        else:
            raise RuntimeError(f"TimeStatistic: {name} not started")
        return str(inc_time)

    def _add_time(self, name, inc_time):
        if name not in self._total_time:
            self._total_time[name] = 0
            self._count[name] = 0
        self._total_time[name] += inc_time
        self._count[name] += 1

    def get_statistics(self, name):
        if name in self._total_time:
            return {
                "Total time": self._total_time[name],
                "Count": self._count[name],
                "Average_time": self._total_time[name] / self._count[name]
            }
        else:
            raise RuntimeError(f"TimeStatistic: {name} has no statistics")
