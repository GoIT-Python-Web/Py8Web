from models import Post, User

if __name__ == "__main__":
    posts = Post.objects()

    print(len(posts))

    for post in posts:
        print(post.to_json())
