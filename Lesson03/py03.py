# Codding UTF-8

# Комментарий

import os #для работы с системой
import psutil
import getpass

print("file.name: " + __file__)
print("Программа приветствия 2.0")
print("Hello!")
# name = input("Введите имя: ")
print("Привет,", getpass.getuser() + "!")

question = input("Давайте поработаем? (Y/N): ")

if question == "Y":
    print("Выберете действие:")
    print("a) Вывести список файлов директории")
    print("b) Вывести список процессов")
    print("c) Вывести текущую дерикторию")
    print("d) Вывести информацию о системе")
    print("e) Вывести информацию об использовании памяти системой")
    question2 = input()
    if question2 == "a":
        print(os.listdir())
    elif question2 == "b":
        print(os.pids())
    elif question2 == "c":
        print(os.getcwd())
    elif question2 == "d":
        print(os.uname())
    elif question2 == "e":
        print(psutil.virtual_memory())
    else:
        print("Ошибка!!!")
elif question == "N":
    print("До свиданья!")
else:
    print("Ошибка!!!")
