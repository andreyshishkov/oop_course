import random


class Ship:

    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1 for _ in range(length)]

    @property
    def tp(self):
        return self._tp

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    @property
    def length(self):
        return self._length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def is_collide(self, ship):
        """
        Method is used to determine if ships are collided
        """
        x_bounds, y_bounds = None, None
        if ship.tp == 1:
            x_bounds = [ship.x - 1, ship.x + ship.length]
            y_bounds = [ship.y - 1, ship.y + 1]
        if ship.tp == 2:
            x_bounds = [ship.x - 1, ship.x + 1]
            y_bounds = [ship.y - 1, ship.y + ship.length]

        if x_bounds[0] <= self._x <= x_bounds[1] and y_bounds[0] <= self._y <= y_bounds[1]:
            return True
        return False

    def is_out_pole(self, size):
        if any(i < 0 for i in (self._x, self._y)):
            return True
        if self._x > (size - 1) or self._y > (size - 1):
            return True

        if self._tp == 1:
            return not (self._x + self._length) <= (size - 1)
        else:
            return not (self._y + self._length) <= (size - 1)

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:

    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        stated_ships = []
        for length in range(4, 0, -1):
            for _ in range(5 - length):
                while True:
                    curr_x = random.randint(0, self._size)
                    curr_y = random.randint(0, self._size)
                    curr_tp = random.choice([1, 2])
                    curr_ship = Ship(length, curr_tp, curr_x, curr_y)
                    if not curr_ship.is_out_pole(self._size) and \
                            not any(curr_ship.is_collide(ship) for ship in stated_ships):
                        stated_ships.append(curr_ship)
                        break

    def get_ships(self):
        return self._ships

    def move_ships(self):
        move_step = [-1, 1]
        for i in range(len(self._ships)):
            ship = self._ships[i]
            step = random.choice(move_step)

            ship.move(step)
            if ship.is_out_pole(self._size) or any(ship.is_collide(self._ships[j] for j in range(len(self._ships))
                                                                   if i != j)):
                ship.move(-2 * step) # comeback to start state and make one step in against direction
                if ship.is_out_pole(self._size) or any(ship.is_collide(self._ships[j] for j in range(len(self._ships))
                                                                       if i != j)):
                    ship.move(-step)

    def get_pole(self):
        field = tuple(
            tuple(0 for _ in range(self._size)) for _ in range(self._size)
        )
        return field


if __name__ == '__main__':
    ship = Ship(2)
    ship = Ship(2, 1)
    ship = Ship(3, 2, 0, 0)

    assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
    assert ship._cells == [1, 1, 1], "неверный список _cells"
    assert ship._is_move, "неверное значение атрибута _is_move"

    ship.set_start_coords(1, 2)
    assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
    assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

    ship.move(1)
    s1 = Ship(4, 1, 0, 0)
    s2 = Ship(3, 2, 0, 0)
    s3 = Ship(3, 2, 0, 2)

    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
    assert s1.is_collide(
        s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

    s2 = Ship(3, 2, 1, 1)
    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

    s2 = Ship(3, 1, 8, 1)
    assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

    s2 = Ship(3, 2, 1, 5)
    assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

    s2[0] = 2
    assert s2[0] == 2, "неверно работает обращение ship[indx]"

    p = GamePole(10)
    p.init()
    for nn in range(5):
        for s in p._ships:
            assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

            for ship in p.get_ships():
                if s != ship:
                    assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
        p.move_ships()

    gp = p.get_pole()
    assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
    assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

    pole_size_8 = GamePole(8)
    pole_size_8.init()
