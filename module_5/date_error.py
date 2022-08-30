# здесь объявляйте классы
from datetime import datetime


class DateError(Exception):
    """Дата в строке записана неверно"""


class DateString:

    def __init__(self, date_string):
        try:
            self._date = datetime.strptime(date_string, '%d.%m.%Y').strftime('%d.%m.%Y')
        except ValueError:
            raise DateError

    def __str__(self):
        return self._date


date_string_ = input()

# здесь создавайте объект класса DateString и выполняйте обработку исключений
try:
    date = DateString(date_string_)
    print(date)
except DateError:
    print("Неверный формат даты")
