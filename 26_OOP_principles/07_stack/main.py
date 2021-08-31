class Stack:
    def __init__(self):
        self.__stack = []

    def __str__(self):
        return '; '.join(self.__stack)

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        for i_priority in sorted(self.task.keys()):
            display.append('{} {}\n'.format(i_priority, self.task[i_priority]))
        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

