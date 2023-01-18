def pretty_view(body):
    print(f"Pretty view: {body}")


def calc(num: int):
    result = num + 100
    return result


def calc_cb(num: int, cb):
    result = num + 100
    cb(result)


if __name__ == '__main__':
    r = calc(1000)
    pretty_view(r)

    calc_cb(2000, pretty_view)
