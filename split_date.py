# Эта программа применяет метод split(),
# в которой символ '/' применяется в качестве разделителя.


def main():
    # Создаем строковое значение с датой
    date_string = '21/07/2021'

    # Разбиваем дату и выводим на печать
    date = date_string.split('/')
    print(date)
    print('Отформатированный вывод даты: ')
    print('Год: ', date[2])
    print('Месяц: ', date[1])
    print('День: ', date[0])


main()