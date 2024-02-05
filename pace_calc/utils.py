'''

Библиотека расчета темпа бега (pace_calc)
MIT License Copyright (c) 2024 ntymko

'''

from .converts import *
import enum


class PaceCalculator:
    def __init__(self, distance):
        if type(distance) != int:
            raise PaceCalculatorError('Неверный тип дистанции')

        self.distance = int(distance)

    def calc_temp(self, time_sec):
        '''Для расчета темпа бега в секундах'''
        u = self.distance / time_sec * 3600 / 1000
        temp = 3600 / u
        return temp

    def calc_time(self, temp_sec):
        '''Для расчета времени в секундах'''
        u = 3600 / temp_sec
        t = int(self.distance) * 3.6 / u
        return t

    def calc_speed(self, temp_sec):
        '''Для рассчета скорости'''
        u = 3600 / temp_sec
        return u

    def from_speed_calc_temp(self, u):
        '''Для рачета темпа из скорости'''
        temp = 3600 / get_str_to_float_speed(u)
        return round(temp, 2)


class PaceKind(enum.Enum):
    SPEED = 'скорость'
    TEMP = 'темп'
    TIME = 'время'


def parse_pace_kind(str_kind):
    lower_value = str_kind.lower()
    if lower_value == PaceKind.SPEED.value:
        return PaceKind.SPEED
    elif lower_value == PaceKind.TEMP.value:
        return PaceKind.TEMP
    elif lower_value == PaceKind.TIME.value:
        return PaceKind.TIME
    return None


class PaceCalculatorError(Exception):
    pass
