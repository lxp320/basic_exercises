# Вывести последнюю букву в слове
word = 'Архангельск'
# Функция для вывода последней буквы
def last_letter(word: str) -> None:
    print(f'Последняя буква в слове {word}: {word[-1]}')
last_letter(word)

# Вывести количество букв "а" в слове
#word = 'Архангельск'
# Функция для вывода количества букв "а"
def letter_a_count(word: str) -> None:
    # Строка приводится к нижнему регистру
    word = word.lower()
    print(f"Количество букв 'а' в слове {word}: {word.count('а')}")
letter_a_count(word)

# Вывести количество гласных букв в слове
#word = 'Архангельск'
# Функция для вывода количества гласных букв в слове
def vowels_letters(word: str) -> None:
    # Множество с гласными буквами
    vowels_data = set("аяуюоеёэиы")
    count = 0
    # Проверка есть ли буква в множестве
    for letter in word.lower():
        if letter in vowels_data:
            count += 1
    print(f"Количество гласных равно: {count}")
vowels_letters(word)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# Функция для подсчета слов в предложении
def word_counter(sentence: str) -> None:
    print(f"Количество слов равно: {len(sentence.split())}")
word_counter(sentence)

# Вывести первую букву каждого слова на отдельной строке
#sentence = 'Мы приехали в гости'
# Функция для вывода первой буквы каждого слова
def fist_letter_every_word(sentence: str) -> None:
    # Разделение предложения на слова
    sentence_list = sentence.split()
    print('Первая буква каждого слова:')
    # Для каждого слова вывод первой буквы
    for word in sentence_list:
        print(word[0])
fist_letter_every_word(sentence)

# Вывести усреднённую длину слова в предложении
#sentence = 'Мы приехали в гости'
# Функция для вывода усредненной длины слова в предложении
def average_word_length(sentence: str) -> None:
    # Разделение предложения на слова
    sentence_list = sentence.split()
    # Переменная с количеством слов
    words = len(sentence_list)
    # Счетчик букв
    letter_counter = 0
    # Подсчет общего числа букв во всех словах
    for word in sentence_list:
        print(len(word))
        letter_counter += len(word)
    # Вычисление средней длины
    ave_word_lenght = letter_counter / words
    print(f'Средняя длина слова: {ave_word_lenght}')
average_word_length(sentence)