class StackObj:
    def __init__(self, data):
        self.__next = None
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top:
            start = self.top
            while start.next:
                start = start.next
            start.next = obj
        else:
            self.top = obj

    def pop(self):
        if not self.top:
            return
        if self.top.next is None:
            p = self.top
            self.top = None
            return p
        start = self.top
        while start.next.next:
            start = start.next
        p = start.next
        start.next = None
        return p

    def get_data(self):
        start = self.top
        arr = []
        while start:
            arr.append(start.data)
            start = start.next
        return arr
