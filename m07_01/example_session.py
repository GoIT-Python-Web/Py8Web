from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///:memory:')
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship(Person)


Base.metadata.create_all(engine)
Base.metadata.bind = engine


if __name__ == '__main__':
    new_person = Person(fullname='Alexander Incognito')
    session.add(new_person)

    new_address = Address(street_name='Stepana Giga', post_code='36000', person=new_person)
    session.add(new_address)

    session.commit()
    person = session.query(Person).one()
    print(vars(person))
    print(person.id, person.fullname)
    addresses = session.query(Address).join(Person).all()
    for row in addresses:
        print(vars(row))
        print(row.person.fullname)
