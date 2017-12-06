# Codding UTF-8

# Комментарий

print("file.name: " + __file__)
print("Программа приветствия 2.0")
print("Hello!")
name = input("Введите имя: ")

print("Привет,", name + "!")

question = input("Давайте поработаем? (Y/N): ")

if question == "Y":
    print("Какой рабочий день вас устаривает?")
    print("a) С 8-ми до 17:00")
    print("b) С 9-ти до 18:00")
    print("c) С 10-ти до 19:00")
    question2 = input()
    if question2 == "a":
        print(name +" ,вы рання пташка)))")
    elif question2 == "b":
        print("Ошибка!!!")
    elif question2 == "c":
        print("Привыкайте к новому распорядку дня")
    else:
        print("Ошибка!!!")
elif question == "N":
    print("До свиданья!")
else:
    print("Ошибка!!!")
