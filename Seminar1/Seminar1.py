# Задача №1
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами. 
# Input: n = 700 m = 750 
# Output: 2

# n = int(input("Введите растояние, которое проходит авто за день: "))
# m = int(input("Введите общий пробег: "))

# res = (m + n - 1) // n
# print(res)


# Задача № 2
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них. 
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

# a = int(input("Количество учеников в первом классе: "))
# b = int(input("Количество учеников во втором классе: "))
# с = int(input("Количество учеников во третьем классе: "))

# n = 2

# res = (a + n -1)// n + (b + n- 1)// n + (с + n- 1)// n
# print(res)


# Задача № 3
#Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
#(при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). 
#В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
#Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, 
#что без дополнительной информации это сделать невозможно. 
#Input: 3 4(ввод на разных строках) Output: 6

# a = int(input("Введите номер вагона от головы состава: "))
# b = int(input("Введите порядковый номер: "))
# if  a == b:
#   res =  "Информация недостаточно"
# else :
#    res = (a + b - 1)
# print(res)
