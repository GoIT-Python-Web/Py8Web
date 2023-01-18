from models import User

if __name__ == "__main__":
    users = User.objects()
    for user in users:
        print(user.to_json())

    igor = User.objects(first_name="Igor")
    igor.delete()

    print("-------------------")
    users = User.objects()
    for user in users:
        print(user.to_json())
