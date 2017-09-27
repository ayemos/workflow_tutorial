import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Task(object):
    @abc.abstractmethod
    def run(self):
        """Run task."""


class HelloTask(Task):
    def run(self):
        print('Hello!')


if __name__ == '__main__':
    HelloTask().run()
