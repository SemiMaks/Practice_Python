# Эта программа получает строку и возвращает список
# содержащий слова в строковом значении посредством метода split().

def main():
    # Создаем строковое значение с несколькики словами
    my_string = 'Один два три четыре'

    # Разбиваем строковое значение
    word_list = my_string.split()

    # Печатаем список слов
    print(word_list)


main()