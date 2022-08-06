from random import choice


class Cell:

    def __init__(self, value: int = 0):
        self.value = value

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    values = [FREE_CELL, HUMAN_X, COMPUTER_O]

    def __init__(self):
        self.pole = [[Cell(TicTacToe.FREE_CELL) for _ in range(3)] for _ in range(3)]

    @staticmethod
    def __check_index(index):
        r, c = index
        if not all(type(x) == int for x in index) or not (0 <= r <= 2) or not (0 <= c <= 2):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        r, c = key
        if value not in self.values:
            raise ValueError('Incorrect value')
        self.pole[r][c].value = value

    def output(self, value):
        if value == self.FREE_CELL:
            return ' '
        elif value == self.HUMAN_X:
            return 'X'
        else:
            return 'O'

    def show(self):
        k = 0
        for row in self.pole:
            print('|'.join([self.output(x.value) for x in row]))
            if k < 2:
                print('- ' * 3)
                k += 1

    def init(self):
        for i in range(3):
            for j in range(3):
                self[i, j] = self.FREE_CELL

    def human_go(self):
        coordinates = [int(x) for x in input().split()]
        self.__check_index(coordinates)
        r, c = coordinates
        self[r, c] = self.HUMAN_X
        print()

    def computer_go(self):
        r = choice(self.values)
        c = choice(self.values)
        while not bool(self.pole[r][c]):
            r = choice(self.values)
            c = choice(self.values)
        self[r, c] = self.COMPUTER_O
        print()

    def __check_win(self, value):
        # check rows
        for row in self.pole:
            if all(x.value == value for x in row):
                return True
        # check columns
        for c in range(3):
            if all(self[r, c] == value for r in range(3)):
                return True
        # check diagonals
        if all(self[i, i] == value for i in range(3)):
            return True
        if all(self[i, 2 - i] == value for i in range(3)):
            return True

        return False

    @property
    def is_human_win(self):
        result = self.__check_win(self.HUMAN_X)
        return result

    @property
    def is_computer_win(self):
        result = self.__check_win(self.COMPUTER_O)
        return result

    def __bool__(self):
        if self.__check_win(self.HUMAN_X) or self.__check_win(self.COMPUTER_O):
            return False
        if all(all(not bool(x) for x in row) for row in self.pole):
            return False
        return True

    @property
    def is_draw(self):
        if not bool(self) and not self.__check_win(self.HUMAN_X) and not self.__check_win(self.COMPUTER_O):
            return True
        return False


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
