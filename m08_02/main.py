from datetime import datetime

from sqlalchemy.orm import joinedload
from sqlalchemy import and_

from database.db import session
from database.models import Student, Teacher, ContactPerson


def get_students():
    students = session.query(Student).options(joinedload('teachers')).all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {teacher.id} first_name: {teacher.first_name}' for teacher in s.teachers]}")


def get_students_join():
    students = session.query(Student).join('teachers').all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {teacher.id} first_name: {teacher.first_name}' for teacher in s.teachers]}")


def get_students_all():
    students = session.query(Student).options(joinedload(Student.teachers), joinedload(Student.contacts)).all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {teacher.id} first_name: {teacher.first_name}' for teacher in s.teachers]}")
        print(f"{[f'id: {contact.id} first_name: {contact.first_name}' for contact in s.contacts]}")


def get_teachers():
    teachers = session.query(Teacher).options(joinedload('students')).all()
    for t in teachers:
        print(vars(t))
        print(f"{[f'id: {student.id} first_name: {student.first_name}' for student in t.students]}")


# WHERE start_work > 1234 AND start_work < 3456
def get_teachers_filter():
    teachers = session.query(Teacher).options(joinedload('students')).filter(and_(
        Teacher.start_work > datetime(year=2021, month=6, day=1),
        Teacher.start_work < datetime(year=2021, month=12, day=31)
    )).all()
    for t in teachers:
        print(vars(t))
        print(f"{[f'id: {student.id} first_name: {student.first_name}' for student in t.students]}")


if __name__ == '__main__':
    # get_students()
    # get_teachers()
    # get_students_join()
    # get_teachers_filter()
    get_students_all()
