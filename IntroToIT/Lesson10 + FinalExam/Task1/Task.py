#INTRO TO IT 2nd COURSE / Final Exam / TASK 1

#ДОБАВЬТЕ СЛЕДУЮЩИЕ ФУНКЦИИ В ПРОГРАММУ

#1. Для данной игры установите ограничение в 5 попыток
#2. Если игрок ввел число которое отличается от загаданого на 15 значений, то вывести сообщение "Тепло"
#3. Если игрок ввел число которое отличается от загаданого на 10 значения, то вывести сообщение "Горячо"
#4. Если игрок ввел число которое отличается от загаданого на 5 значение, то вывести сообщение "Очень горячо"

#5. Если игрок ввел число которое отличается от загаданого на 20 значения, то вывести сообщение "Холодно"
#6. Если игрок ввел число которое отличается от загаданого на 30 значения, то вывести сообщение "Очень холодно"
#7. Если игрок ввел число которое отличается от загаданого на 40 значений, то вывести сообщение "Мерзлота"
#8. Если игрок ввел число которое отличается от загаданого на 50 значений, то вывести сообщение "Северный полюс!"


import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его.")

    while True:
        attempts += 1
        try:
            player_guess = int(input("Введи число: "))
            if player_guess < 1 or player_guess > 100:
                print("Пожалуйста, введите число от 1 до 100.")
                continue
        except ValueError:
            print("Это не число. Попробуйте снова.")
            continue

        if player_guess < number_to_guess:
            print("Слишком мало, попробуй еще раз." + "попыток: " + str(attempts))
        elif player_guess > number_to_guess:
            print("Слишком много, попробуй еще раз."+ "попыток: " + str(attempts))
        else:
            print(f"Поздравляю! Ты угадал число за {attempts} попыток.")
            break

if __name__ == "__main__":
    guess_the_number()
