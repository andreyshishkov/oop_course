from random import randint


class Cell:

    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not 0 <= value <= 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open


class GamePole:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, N, M, total_mines):
        self.__pole_cells = [[Cell() for i in range(M)] for j in range(N)]
        self.n = N
        self.m = M
        self.total_mines = total_mines

    def init_pole(self):
        k = 0  # current number of mines
        while k < self.total_mines:
            i = randint(0, self.n - 1)
            j = randint(0, self.m - 1)
            if not self.__pole_cells[i][j].is_mine:
                self.__pole_cells[i][j].is_mine = True
                k += 1
        for i in range(self.n):
            for j in range(self.m):
                if not self.__pole_cells[i][j].is_mine:
                    r = sum((self.__pole_cells[i + p][j + q].is_mine for p in [-1, 0, 1] for q in [-1, 0, 1] \
                             if 0 <= (i + p) <= (self.n - 1) and 0 <= (j + q) <= (self.m - 1)))
                    self.__pole_cells[i][j].number = r

    def show_pole(self):
        return self.__pole_cells

    def open_cell(self, i, j):
        try:
            self.__pole_cells[i][j].is_open = True
        except IndexError:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    @property
    def pole(self):
        return self.__pole_cells
