import random
# print(random.randrange(6,12,2))

# a=int(input("Введите нижнюю границу"))
# b=int(input("Введите верхнюю границу"))
# s=input("Введите ц или в")
# if s=="ц":
#     print(random.randint(a,b))
# if s=="в":
#     print(random.random()*(b-a)+a)
# a=random.randint(1,3)
# if a == 1:
#     print("Безудержная радость!!!")
# elif a ==2:
#     print("Спокойствие и безмятежность")
# elif a == 3:
#     print("Уныние и грусть")
# num=1
# while num < 10:
#     print("Мы в цикле")
#     num+=1
# number = 5
# while number > 0:
#     number -= 1
#     if number == 2:
#         continue
#     print(number)
# while True:
#     num = int(input("Введите число"))
#     if num < 10:
#         continue
#     elif num > 100:
#         break
#     print(num)
print("Привет!")
a = random.randint(1,100)
print("Угадай число")
s = int(input("Введи число"))
p = 1
while s != a:
    s = int(input("Введи число"))
    if s > a:
        print("Число больше загаданного")
    elif s < a:
        print("Число меньше загадонного")
    elif s == a:
        print("Вы угадали!", "С", p, "попытки")
    p+=1