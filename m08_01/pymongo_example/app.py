import argparse
from functools import wraps

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://userweb8:567234@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority",
                     server_api=ServerApi('1'))

db = client.book

parser = argparse.ArgumentParser(description='CRUD Cat')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arguments = vars(parser.parse_args())  # object -> dict

action = arguments.get('action')
id_ = arguments.get('id')
name = arguments.get('name')
age = arguments.get('age')
if age:
    age = int(age)
features = arguments.get('features')


class ExceptionValidation(Exception):
    pass


def validate(func):
    @wraps(func)
    def wrapper(*args):
        for el in args:
            if el is None:
                raise ExceptionValidation(f'Вхідні дані не валідні: {func.__name__}{args}')
        result = func(*args)
        return result
    return wrapper


@validate
def create(name: str, age: int, features: list):
    result = db.cats.insert_one(
        {
            "name": name,
            "age": age,
            "features": features,
        }
    )
    return result.inserted_id


def find():
    return db.cats.find()


def find_by_id(id_):
    return db.cats.find_one({"_id": ObjectId(id_)})


@validate
def update(id_: str, name: str, age: int, features: list):
    r = db.cats.update_one({"_id": ObjectId(id_)}, {
        "$set": {
            "name": name,
            "age": age,
            "features": features,
        }
    })
    return find_by_id(id_)


@validate
def remove(id_: str):
    return db.cats.delete_one({"_id": ObjectId(id_)})


def main():
    try:
        match action:
            case 'create':
                r = create(name, age, features)
                print(r)
            case 'update':
                r = update(id_, name, age, features)
                print(r)
            case 'find':
                r = find()
                [print(el) for el in r]
            case 'remove':
                r = remove(id_)
                print(r)
            case _:
                print('Unknowns command')
    except ExceptionValidation as err:
        print(err)


if __name__ == '__main__':
    main()