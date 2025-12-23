import random
b = 0
print("Wasd- управление")
a = input("Введите: ")
while a!=8:
    r= random.randint(1,10)
    print(r)
    if r==8:
        print(f"Вы выйграли за {b} Ходов")
        break
    elif a=="a" or a=="w" or a=="s" or a=="d":
        a = input("Введите: ")
        print(f"Вы нажали {a} И не нашли выхода")
        b +=1
    else:
        print("Ошибка! Можно использовать только wasd")
        a = input("Введите ")
print("Ты гиперудачлив")
