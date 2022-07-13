import random
from string import ascii_letters, digits
import re


class EmailValidator:

    def __new__(cls, *args, **kwargs):
        pass

    allow_symbs = list(ascii_letters) + list(digits) + ['_', '.']

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if email.count('@') != 1:
            return False
        if not re.fullmatch(r'[\w.]+@[\w.]+', email, re.ASCII):
            return False
        if len(email.split('@')) != 2:
            print('123')
            return False
        first, second = email.split('@')
        if not (0 < len(first) <= 100 and 0 < len(second) <= 50):
            return False
        if second.count('.') == 0:
            return False
        if second.count('..') or first.count('..'):
            return False
        return True

    @classmethod
    def get_random_email(cls):
        n = random.randint(1, 100)
        address = ''
        for _ in range(n):
            address += random.choice(cls.allow_symbs)
        return address + '@gmail.com'

    @staticmethod
    def __is_email_str(email):
        correct = isinstance(email, str)
        return correct


assert EmailValidator.check_email("sc_lib@list.ru"), '1'
assert not EmailValidator.check_email("sc_lib@list_ru"), '2'
assert not EmailValidator.check_email("sc@lib@list_ru"), '3'
assert not EmailValidator.check_email("sc.lib@list_ru"), '4'
