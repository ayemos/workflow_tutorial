import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Target(object):
    @abc.abstractmethod
    def open(self):
        """Return IO-like object"""


class LocalTarget(Target):
    def __init__(self, path):
        self._path = path

    def open(self, mode='r'):
        return open(self._path, mode)
