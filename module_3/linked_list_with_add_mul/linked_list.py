class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if type(value) in (type(None), StackObj):
            self.__next = value


class Stack:

    def __init__(self):
        self.top = None

    def last_obj(self):
        start = self.top
        if start is None:
            return None
        while start.next:
            start = start.next
        return start

    def push_back(self, obj):
        if self.top:
            last = self.last_obj()
            last.next = obj
        else:
            self.top = obj

    def pop_back(self):
        start = self.top
        if start is None:
            return None
        if start.next is None:
            self.top = None
            return start.data
        while start.next.next:
            start = start.next
        data = start.next.data
        start.next = None
        return data

    def __add__(self, other):
        self.push_back(other)
        return self

    def __radd__(self, other):
        return self + other

    def __mul__(self, lst):
        for data in lst:
            obj = StackObj(data)
            self += obj
        return self

    def __rmul__(self, lst):
        return self * lst
