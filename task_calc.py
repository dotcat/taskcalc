#!/usr/bin/env python
import sys
command = int(sys.argv[1])

w = 25
sb = 5
lb = 15
t = [w, sb, w, sb, w, sb, w, lb, ]


class TaskCalc():

    def __init__(self, amount, template):
        self.template = template
        self.amount = amount

    def task_generator(self):
        i = r = len(self.template)
        while True:
            yield self.template[-i]
            if i == 0:
                i += r - 1
            else:
                i -= 1

    def calc_duration(self):
        duration = 0
        for task in self.task_generator():
            if self.amount == 0:
                break
            elif task == w:
                self.amount -= 1
            duration += task
        return duration

    def pretty_duration(self):
        duration = self.calc_duration()
        hours = duration // 60
        minutes = duration % 60
        return {'h': hours, 'm': minutes}


if __name__ == '__main__':
    pom = TaskCalc(command, t)
    print(pom.pretty_duration())
