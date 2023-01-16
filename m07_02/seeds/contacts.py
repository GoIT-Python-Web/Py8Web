import random

from faker import Faker

from database.db import session
from database.models import Student, ContactPerson

fake = Faker('uk_UA')


def contact_persons():
    students = session.query(Student).all()

    for _ in range(len(list(students)) + 5):
        student = random.choice(students)

        cp = ContactPerson(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address(),
            student_id=student.id
        )
        session.add(cp)
    session.commit()


if __name__ == '__main__':
    contact_persons()
