from builtins import print, int
import random

number = random.randint(0, 101)

while True:

    answer = input("Ввведите число: ")

    if not answer or answer == "exit":
        print("Работа завершена")
        break

    if not answer.isdigit():
        print("Введите правильное число!")
        continue

    user_ansewer = int(answer)

    if user_ansewer > number:
        print("Загаданное число меньше")
    elif user_ansewer < number:
        print("Загаданное число больше")
    else:
        print("Совершенно верно!")
        break
