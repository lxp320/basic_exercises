# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# Функция для подсчета повторений каждого имени
def name_counter(user_list: list, need_print: int = 0) ->dict:
    if need_print == 1:
        print('Задача 1:')
    # Новый словарь для записи результатов
    name_list = {}
    # Проход по всем словарям в списке
    for dict in user_list:
        # Переменная для простой записи имени
        name = dict.get('first_name')
        # Если это имя уже хоть раз попадалось, то увеличиваем количество на 1
        if name_list.get(name) != None:
            name_list[name] += 1
        # В противном случае создается новая пара ключ-значение
        else:
            name_list[name] = 1
    # Вывод результатов подсчета из словаря
    for key in name_list:
        if need_print == 1:
            print(f"{key}: {name_list[key]}")
    # Возращение словаря с подсчетами
    if need_print == 1:
        print()
    return name_list
# Тест
name_counter(students, 1)

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# Функция для определения самого популярного имени в классе
def most_popular_name(user_list: list, need_print: int = 0) ->str:
    if need_print == 1:
        print('Задача 2:')
    # Запись результата работы функции по подсчету имен в переменную
    student_list = name_counter(user_list)
    # Определение самого большого значения, соответствующего ключу
    top_name = max(student_list, key = student_list.get)
    if need_print == 1:
        print(f'Самое популярное имя среди учеников: {top_name}')
        print()
    return top_name
# Тест    
most_popular_name(students1, 1)

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# Функция для определения самого популярного имени в каждом классе
def most_popular_names_in_class(classes_list: list, need_print: int = 0) ->None:
    # Красивый вывод решения
    if need_print == 1:
        print('Задача 3:')
    # Счетчик номера класса
    i = 1
    for classes in classes_list:
        print(f"Самое популярное имя в классе {i}: {most_popular_name(classes)}")
        i += 1
    if need_print == 1:
        print()
# Тест
most_popular_names_in_class(school_students, 1)

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# Функция для подсчета девочек и мальчиков в каждом классе
def gender_in_class_counter(classes_list: list, gender_list: dict, need_print: int = 0) ->list:
    # Красивый вывод решения
    if need_print == 1:
        print('Задача 4:')
    # Список для хранения словарей с результатами
    gender_list_in_classes = []
    # Проход по списку классов
    for any_class in classes_list:
        # Предварительное наполнение словаря
        class_gender = {'male': 0, 'female': 0}
        class_gender['class'] = any_class.get('class')
        # Проход по ученикам в классе
        for student in any_class.get('students'):
            # Если мальчик, то увеличивается счетчик по ключу male на 1
            if gender_list[student.get('first_name')]:
                class_gender['male'] += 1
            # В противном случае увеличивается счетчик female
            else:
                class_gender['female'] += 1
        # Внесение словаря в список
        gender_list_in_classes.append(class_gender)
    # Вывод данных в терминал
    if need_print == 1:
        for dict in gender_list_in_classes:
            print(f"Класс {dict['class']}: Девочки {dict['female']}, Мальчики {dict['male']}")
    if need_print == 1:
        print()
    return gender_list_in_classes
# Тест
gender_in_class_counter(school, is_male, 1)

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school1 = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male1 = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# Функция для поиска в каком классе больше всего мальчиков и в каком больше всего девочек
def max_class_male_and_female(classes_list: list, gender_list: dict, need_print: int = 0) ->None:
    # Красивый вывод решения
    if need_print == 1:
        print('Задача 5:')
    # Переменные для подсчета
    max_male = 0
    max_female = 0
    # Перебор всех словарей в списке
    for dict in gender_in_class_counter(classes_list, gender_list):
        # Если попалось значение больше актуального максимума, то он обновляется и фиксируется класс где он найден
        if dict['male'] > max_male:
            max_male = dict['male']
            max_male_class = dict['class']
        # Если попалось значение больше актуального максимума, то он обновляется и фиксируется класс где он найден
        if dict['female'] > max_male:
            max_female = dict['female']
            max_female_class = dict['class']
    print(f"Больше всего мальчиков в классе {max_male_class}")
    print(f"Больше всего девачек в классе {max_female_class}")
# Тест
max_class_male_and_female(school1, is_male1, 1)