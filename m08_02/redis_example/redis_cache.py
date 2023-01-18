import timeit

import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def fibonacci_fast(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)


if __name__ == '__main__':
    start_time = timeit.default_timer()
    fibonacci(38)
    print(f"Duration fibonacci f(38): {timeit.default_timer() - start_time}")

    start_time = timeit.default_timer()
    fibonacci_fast(138)
    print(f"Duration fast fibonacci f(38): {timeit.default_timer() - start_time}")
