from models import LinkPost, ImagePost, TextPost, User


if __name__ == "__main__":
    ross = User(email="ross@ex.ua", first_name="Ross", last_name="Garsia").save()

    post_text = TextPost(title="Fun title", author=ross)
    post_text.content = "Abababa galamaga"
    post_text.tags = ["mongodb", "mongoengine"]
    post_text.save()

    post_link = LinkPost(title="Mongoengine documentation", author=ross)
    post_link.link_url = "https://docs.mongoengine.com/"
    post_link.tags = ["mongoengine"]
    post_link.save()

    igor = User(email="igor@ex.ua", first_name="Igor", last_name="Omelchenko").save()

    post_img = ImagePost(title="C++ forever!", author=igor)
    post_img.image_url = (
        "https://ip-calculator.ru/blog/wp-content/uploads/2021/02/6038586442907648.png"
    )
    post_img.tags = ["C++", "C#"]
    post_img.save()
