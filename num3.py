#Задание 1 
x = int(input("Введите количество минут: "))
print("Часов : ",x//60 , "минут ",x%60 , " секунд")
#Задание 2
h = int(input("Введите сколько часов спит Аня: "))
a = int(input("Рекомендуется спать часов:"))
b = int(input("Не стоит спать более часов: "))
if h >= a:
    print("Это нормально")
elif h > b:
    print("Пересып")
else:
    print("Недопсып")
#Задние 3
a = int(input("Введите первую сторону треугольника: "))
b = int(input("Введите вторую сторону треугольника: "))
c = int(input("Введите третью сторону треугольника: "))
p = (a+b+c)/2 
 #Украдено у kievsky332
S = (p*(p-a)*(p-b)*(p-c))**0.5
print("Площадь треугольника по формуле герона: ", S )
#Задание 4
x = input("Введите тип фигуры команты: ")
if x == "Круг":
    a = int(input("Введите радиус команты: "))
    print("Площадь вашей комнаты: " , (a**2)*3.14)
elif x == "Прямоугольник":
    z =  int(input("Введите длинну команты: "))
    c =  int(input("Введите ширину команты: "))
    print("Площадь вашей комнаты: " , z*c)
elif x == "Треугольник":
    v =  int(input("Введите длинну команты: "))
    b =  int(input("Введите высоту команты: "))
    print("Площадь вашей комнаты: " , (v * b)/2) 
else: 
   #Украдено у kievsky332
    print("Неверный ввод")
#5
s = int(input)
# Получаем последнюю цифру числа
for i in range(0,a):
    num_str = i
    last_digit = i % 10
    last_two_digits = i % 100
    if 11 <= last_two_digits <= 14:
        print( f"{num_str} програмистов")
    elif last_digit == 1:
        print(f"{num_str} програмист")
    elif 2 <= last_digit <= 4:
        print( f"{num_str} програмиста")
    else:
        print(f"{num_str} програмистов")
#6
acc = input()

if acc[0]+acc[1]+acc[2] == acc[-1]+acc[-2]+acc[-3]:
    print(True)
else:
    print(False)
