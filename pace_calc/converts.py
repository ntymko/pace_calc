'''

Библиотека расчета темпа бега (pace_calc)
MIT License Copyright (c) 2024 ntymko

'''

'''Методы для конвертации'''

import time


def time_str_to_int_sec(t):
    '''Для перевода времени из формата М:С в секунды'''
    t_sek_list = t.split(':')
    t_total = 0
    if len(t_sek_list) == 2:
        first = True
        for i in t_sek_list:
            if first:
                t_total += int(i) * 60
                first = False
            else:
                t_total += int(i)

    if len(t_sek_list) == 3:
        for i in range(len(t_sek_list)):
            if i == 0 or i == 1:
                t_total += int(t_sek_list[i]) * 3600
            else:
                t_total += int(t_sek_list[i])
    return t_total


def temp_str_to_int_sec(Temp):
    '''Для перевода темпа из формата М:С в секунды'''
    Temp_list = Temp.split(':')
    Temp_sec = int(Temp_list[0]) * 60 + int(Temp_list[1])
    return Temp_sec


def get_formating_time_by_seconds(seconds):
    '''Для перевода времени из секунд в формат Ч:М:С'''
    format = '%M:%S'
    if seconds >= 3600:
        format = '%H:%M:%S'

    return time.strftime(format, time.gmtime(seconds))


def get_str_to_float_speed(u):
    '''Для перевода скорости из строки в число с плавающей точкой'''
    u_list = []
    new_u = ''
    if '.' in str(u):
        return float(u)
    if ',' in u:
        return float(u.replace(',', '.'))
