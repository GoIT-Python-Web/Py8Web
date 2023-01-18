from models import Post, User

if __name__ == "__main__":
    post = Post.objects(title="Mongoengine documentation")
    post.update(link_url="https://docs.mongoengine.org/")
    for p in post:
        print(p.to_json())
