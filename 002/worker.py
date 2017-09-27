from task import GreetTask


class Worker(object):
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        for d in task.deps:
            self.add_task(d)

        self._tasks.append(task)

    @property
    def _next_to_run(self):
        return self._shift(self._tasks)

    def _shift(self, arr):
        if len(arr) == 0:
            return None
        else:
            return arr.pop(0)

    def run(self):
        t = self._next_to_run
        while t:
            t.run()
            t = self._next_to_run


if __name__ == '__main__':
    w = Worker()
    w.add_task(GreetTask('Alice'))
    w.run()
