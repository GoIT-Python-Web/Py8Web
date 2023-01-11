"""
Типовое решение заполнения БД данными. Перед выполнением создаём
виртyальное окружение
    Будем использовать библиотеку Faker для генерации
случайных данных, в нашем случае имён студентов и преподавателей.
Больше информация - https://faker.readthedocs.io/en/master/index.html
Установка - pip install faker
    С библиотекой os вы уже знакомы.
Будем использовать для проверки существования файла БД и работы с файлом
скрипта SQL
"""

from datetime import date, datetime, timedelta
from random import randint
import sqlite3
import os
import faker

'''
Создаем свою ф-цию для получения списка дат, в которые происходит учебный процесс.
Для упрощения выбрасываем только дни, которые попадают на выходные.
'''


def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


'''
Функция создания БД, в качестве параметра - передаем путь к файлу с SQL скриптом
'''


def create_db(path):
    # проверяем на наличие существования БД
    if not os.path.exists(f'{os.path.basename(path).split(".")[0]}.db'):
        # если БД нет - читаем файл со скриптом, переданный в параметре ф-ции
        with open(path) as f:
            sql = f.read()
        # создаем соединение используя менеджер контекста
        with sqlite3.connect(f'{os.path.basename(path).split(".")[0]}.db') as conn:
            # создаем объект курсора
            cur = conn.cursor()
            # полностью выполняем скрипт из файла
            cur.executescript(sql)
            # подтверждаем наши действия
            conn.commit()


'''Функция генерации фейковых данных и заполнения ими БД'''


def fill_data():
    # Не все данные будут динамические. Создаем списки предметов и групп
    disciplines = ['Вища математика', 'Хімія', 'Економіка підприємства', 'Обчислювальна математика', 'Історія України',
                   'Теоретична механіка', 'Менеджмент організацій', 'Системне програмування']

    groups = ['ВВ1', 'ДД33', 'АА5']

    # Создаем объект библиотеки Faker. В качестве параметра передаем local 'uk-UA'
    # Больше - https://faker.readthedocs.io/en/master/locales.html
    fake = faker.Faker('uk-UA')
    # создаём соединение, можно
    conn = sqlite3.connect('hw.db')
    # создаем курсор
    cur = conn.cursor()
    number_of_teachers = 5
    number_of_students = 50

    def seed_teachers():
        teachers = []  # создаем пустой список преподавателей
        # заполняем его случайными именами из объекта fake
        # range принимает в качестве параметра кол-во требуемых объектов
        for _ in range(number_of_teachers):
            teachers.append(fake.name())
        # создаём переменную с текстом запроса для заполнения таблицы teachers
        sql_teachers = 'INSERT INTO teachers(fullname) VALUES (?)'
        # выполняем запрос используя функцию executemany объекта cursor
        # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany
        cur.executemany(sql_teachers, zip(teachers,))

    def seed_disciplines():
        # создаём переменную с текстом запроса для заполнения таблицы disciplines
        sql_disc = 'INSERT INTO disciplines(name, teacher_id) VALUES (?, ?)'
        cur.executemany(sql_disc, zip(
            disciplines, iter(randint(1, number_of_teachers) for _ in range(len(disciplines)))))

    def seed_groups():
        # создаём переменную с текстом запроса для заполнения таблицы groups
        # так как для SQLite group - зарезервированное слово, берем его в [] для использования
        sql_groups = 'INSERT INTO groups(name) VALUES (?)'
        cur.executemany(sql_groups, zip(groups,))

    def seed_students():
        students = []  # создаем пустой список студентов
        # заполняем его случайными именами из объекта fake
        for _ in range(number_of_students):
            students.append(fake.name())
        sql_students = 'INSERT INTO students(fullname, group_id) VALUES (?,?)'
        cur.executemany(sql_students, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))

    def seed_grades():
        # дата начала учебного процесса
        start_date = datetime.strptime("2020-09-01", "%Y-%m-%d")
        # дата окончания учебного процесса
        end_date = datetime.strptime("2021-05-25", "%Y-%m-%d")
        d_range = date_range(start=start_date, end=end_date)

        # создаём пустой список, в котором будем генерировать записи с оценками для каждого студента
        grades = []

        for d in d_range:  # пройдемся по каждой дате
            # Случайно выберем id одной дисциплины. Считаем, что в один день у нас один предмет
            r_disc = randint(1, len(disciplines))
            # допустим, что в один день могут ответить только три студента
            # выбираем троих из наших 30.
            r_students = [randint(1, number_of_students) for _ in range(3)]
            # проходимся по списку "везучих" студентов, добавляем их в результирующий список
            # и генерируем оценку
            for student in r_students:
                grades.append((student, r_disc, d.date(), randint(1, 12)))
        sql_ratings = 'INSERT INTO grades(student_id, discipline_id, date_of, grade) VALUES (?, ?, ?, ?)'
        cur.executemany(sql_ratings, grades)

    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seed_grades()
        conn.commit()

    except sqlite3.IntegrityError as err:
        print(err)

    finally:
        conn.close()


if __name__ == '__main__':
    # create_db('education.sql')
    fill_data()
