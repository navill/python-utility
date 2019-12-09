import functools

"""
https://docs.python.org/ko/3/howto/sorting.html#the-old-way-using-the-cmp-parameter
"""


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


li = [3, 30, 34, 5, 9]
print(solution(li))

print(True - False)
print(False - True)

a = 'apple'
b = 'sauce'

print(''.join([a, b]))
print(f'{a}{b}')
