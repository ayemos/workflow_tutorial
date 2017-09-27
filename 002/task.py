import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Task(object):
    @abc.abstractmethod
    def run(self):
        """Run task."""

    @property
    def deps(self):
        """List of tasks the task depends on."""
        return []


class HelloTask(Task):
    def run(self):
        print('Hello!')

    def output(self):
        return None


class GreetTask(Task):
    _ages = {
        'Alice': 25,
        'Bob': 22,
        'Charlie': 30}

    def __init__(self, name):
        self._name = name

    def run(self):
        print("I'm %s, %s years old." % (self._name, self._ages[self._name]))

    @property
    def deps(self):
        """Say hello before start talking about yourself."""
        return [HelloTask()]


if __name__ == '__main__':
    GreetTask('Alice').run()
