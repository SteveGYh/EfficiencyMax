import Task

class TaskList:

    __slots__ = 'tasklist'

    def __init__(self):
        self.tasklist = []

    def addTask(self, task):
        self.tasklist.append(task)

    def sort_by_priority(self):
        pass

    def sort_by_date(self):
        pass

    def sort_by_ddl(self):
        pass