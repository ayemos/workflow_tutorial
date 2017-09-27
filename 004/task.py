from target import LocalTarget

import os
import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Task(object):
    @abc.abstractmethod
    def run(self):
        """Run task."""

    @abc.abstractmethod
    def task_id(self):
        """Generate task id.
        ID has to be same between logically identical tasks and vice versa.
        """

    @property
    def deps(self):
        """List of tasks the task depends on."""
        return []

    @abc.abstractmethod
    def output(self):
        """Tasks write result here."""

    def inputs(self):
        return [d.output() for d in self.deps]


class HelloTask(Task):
    def run(self):
        print('Hello!')

    def task_id(self):
        return "hello"

    def output(self):
        return None


class GreetTask(Task):
    _ages = {
        'Alice': 25,
        'Bob': 22,
        'Charlie': 30}

    def __init__(self, name):
        self._name = name

    def task_id(self):
        return "greet_%s" % self._name

    def run(self):
        print("I'm %s, %s years old." % (self._name, self._ages[self._name]))
        self.output().open('tw').write("\t".join([self._name, str(self._ages[self._name])]))

    def output(self):
        return LocalTarget(os.path.join('data', '%s.tsv' % self._name))

    @property
    def deps(self):
        """Say hello before start talking about yourself."""
        return [HelloTask()]


class HeightTask(Task):
    def __init__(self, names):
        self._names = names

    def task_id(self):
        return "_".join(['height'] + self._names)

    def run(self):
        outs = []
        for inp in self.inputs():
            d = inp.open(mode='tr').read().split('\t')
            name = d[0]
            age = int(d[1])
            height = age * 2 + 120
            print("%s's height is estimated as %s" % (name, height))
            outs.append("\t".join([name, str(age), str(height)]))

        self.output().open('tw').write("\n".join(outs))

    def output(self):
        return LocalTarget(os.path.join('data', 'height_data.tsv'))

    @property
    def deps(self):
        return [GreetTask(n) for n in self._names]


if __name__ == '__main__':
    GreetTask('Alice').run()
