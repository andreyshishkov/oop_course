class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        start = root
        while start.left:
            if x[start.indx]:
                start = start.left
            else:
                start = start.right
        return start.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node is None:  # create root
            return obj

        if left:
            node.left = obj
        else:
            node.right = obj
        return obj
