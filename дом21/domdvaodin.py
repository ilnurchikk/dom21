#######1 калька
# print("Это приложение колькулятор")
# calculate = input('Калькулятор:\n Введите + или *:')
# a = float(input('ВВедите первое число:'))
# b = float(input('ВВедите второе число:'))
# c = float(input('ВВедите третие число:'))
# if calculate =='+':
#     print(f'Резултат вычесления: {a + b + c}')
# elif calculate == '*':
#     print(f'Резултат вычесления: {a * b * c}')
##########2 на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
# print("Это приложение позволяет выводить на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.")
# tri = input("Выберете: maks min sr:")
# a = float(input('ВВедите первое число:'))
# b = float(input('ВВедите второе число:'))
# c = float(input('ВВедите третие число:'))
# if tri =="maks":
#     print(max(a, b, c))
# elif tri =="min":
#     print(min(a, b, c))
# elif tri =="sr":
#     print((a + b + c)/3)
#################################################3 Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программапереводит метры в мили, дюймы или ярды.
print("Это приложение позволяет переводит метры: в мили, дюймы или ярды.")
metr = input("Выберете: мили, дюймы или ярды:")
a = float(input('ВВедите число м:'))
if metr =="мили":
   print(f'Резултат вычесления: {a / 1609.34}')
elif metr =="дюймы":
   print(f'Резултат вычесления: {a * 39.3701}')
elif metr == "ярды":
   print(f'Резултат вычесления: {a * 1.09361}')
