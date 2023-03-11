"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

time_in_seconds = input('Введите время в секундах: ')
seconds_in_int = int(time_in_seconds)
count_hours = seconds_in_int / 3600
count_minutes = seconds_in_int / 60
hours = str(seconds_in_int // 3600)
minutes = str((seconds_in_int % 3600) // 60)
seconds = str((seconds_in_int % 3600) % 60)
print(f'Время в часах : минутах : секундах - {count_hours} : {count_minutes} : {time_in_seconds}')
print(f'Время в формате времени - чч : мм : сс - {hours.rjust(2, "0")} : {minutes.rjust(2, "0")} :'
      f' {seconds.rjust(2, "0")}')
