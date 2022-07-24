class StackObj:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.__len = 0

    def push(self, obj):
        last = self[self.__len - 1] if self.__len > 0 else None

        if last:
            last.next = obj

        if self.top is None:
            self.top = obj
        self.__len += 1

    def pop(self):
        if self.__len == 0:
            return None
        obj = self[self.__len - 1]
        if self.__len == 1:
            self.top = None
        else:
            self[self.__len - 2].next = None
        self.__len -= 1
        return obj

    def __check_index(self, ind):
        if type(ind) != int or not (0 <= ind < self.__len):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)

        h = self.top
        k = 0
        while h and k < item:
            h = h.next
            k += 1

        return h

    def __setitem__(self, key, value):
        self.__check_index(key)
        obj = self[key]
        prev = self[key - 1] if key > 0 else None
        value.next = obj.next

        if prev:
            prev.next = value

    def show(self) -> None:
        tmp = self.top
        s = []
        while tmp.next is not None:
            s.append(tmp.data)
            tmp = tmp.next
        s.append(tmp.data)
        return ' '.join(s)


def test_push():
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    assert st.show() == 'obj1 obj2 obj3'


def test_setitem():
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    st[1] = StackObj("new obj2")
    assert st.show() == 'obj1 new obj2 obj3'


def test_getitem():
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    st[1] = StackObj("new obj2")
    assert st[2].data == 'obj3'


def test_pop():
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    st[1] = StackObj("new obj2")
    assert st.pop().data == 'obj3'
