from mongoengine import (
    connect,
    Document,
    StringField,
    ReferenceField,
    ListField,
    CASCADE,
)

connect(host="mongodb://127.0.0.1:27017/my_db")


class User(Document):
    email = StringField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Post(Document):
    title = StringField(required=True, max_length=250, min_length=5)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField())
    meta = {"allow_inheritance": True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_url = StringField()


class LinkPost(Post):
    link_url = StringField()
