from functools import wraps

"""
memoization
재귀 함수와 같이 불필요한 반복 연산을 피하기 위해 사용됨
"""


def memoize(fn):
    # closure - free variable
    # dictionary를 cache로 사용
    cache = dict()

    @wraps(fn)
    def memoizer(*args):
        # 값이 cache에 없을 경우
        if args not in cache:
            cache[args] = fn(*args)
        # 있을 경우 cache에 있는 데이터 반환
        return cache[args]

    return memoizer


@memoize
def number_sum(n):
    if n == 0:
        return 0
    else:
        return n + number_sum(n - 1)


@memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


"""
# 아래와 같이 dictionary나 list를 이용해 간단하게 memoization을 구현할 수 있다.
"""
sum_cache = {0: 0}


def number_sum2(n):
    if n in sum_cache:
        return sum_cache[n]
    res = n + number_sum2(n - 1)
    # Add the value to the cache
    sum_cache[n] = res
    return res
