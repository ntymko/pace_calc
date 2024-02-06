# `pace-calc` Калькулятор темпа бега

[![GitHub release](https://img.shields.io/github/release/ntymko/pace_calc.svg?style=flat-square)](https://github.com/ntymko/pace_calc/releases)
[![GitHub license](https://img.shields.io/github/license/ntymko/pace_calc.svg?style=flat-square)](https://github.com/ntymko/pace_calc/blob/main/LICENSE)

Рассчитывает по имеющимся данным темп бега, скорость или итоговое время, необходимое для преодоления определенной дистанции.

## Использование

Главный входной параметр - `distance` (пройденное расстояние, указанное в метрах) Указывается при создании объектов класса `PaceCalculator`. Используется в функциях расчета темпа, времени, скорости.

### Пример
Необходимо рассчитать темп по имеющимся расстоянию и времени

```python
from pace_calc import PaceCalculator, get_formating_time_by_seconds

distance = 5000 # в метрах
time_sec = 1500 # 25 мин.
calc = PaceCalculator(distance)
temp_sec = calc.calc_temp(time_sec) # 300 сек.
temp = get_formating_time_by_seconds(temp_sec) # 5:00
```



