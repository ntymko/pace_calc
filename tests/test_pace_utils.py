import unittest

from pace_calc import PaceCalculator, PaceCalculatorError, parse_pace_kind, PaceKind


class TestPaceCalculator(unittest.TestCase):
    def test_init_calculator(self):
        calc = PaceCalculator(5000)
        self.assertEqual(5000, calc.distance)

        with self.assertRaises(PaceCalculatorError):
            calc = PaceCalculator('ddd')

    def test_calc_temp(self):
        calc = PaceCalculator(5000)
        time = 25 * 60 # 25:00
        temp = calc.calc_temp(time)
        self.assertEqual(300, temp)

    def test_calc_time(self):
        calc = PaceCalculator(5000)
        temp_sec = 4 * 60   #'04:00'
        time = calc.calc_time(temp_sec)
        self.assertEqual(1200, time)

    def test_calc_speed(self):
        calc = PaceCalculator(5000)
        temp_sec = 4 * 60
        u = calc.calc_speed(temp_sec)
        self.assertEqual(15.0, u)

    def test_parse_pace_kind(self):
        str_kind = 'Время'
        kind = parse_pace_kind(str_kind)
        self.assertEqual(PaceKind.TIME, kind)

        str_kind = 'vyjbuinom'
        kind = parse_pace_kind(str_kind)
        self.assertEqual(None, kind)

        str_kind = 'ТемП'
        kind = parse_pace_kind(str_kind)
        self.assertEqual(PaceKind.TEMP, kind)

        str_kind = 'скорость'
        kind = parse_pace_kind(str_kind)
        self.assertEqual(PaceKind.SPEED, kind)


