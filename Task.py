class Task:

    __slots__ = 'title', 'detail', 'priority', 'date'

    def __init__(self, title, detail, priority, date = ''):
        self.title = title
        self.detail = detail
        self.priority = priority
        self.date = date

    
