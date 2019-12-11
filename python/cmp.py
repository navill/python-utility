import functools

"""
https://docs.python.org/ko/3/howto/sorting.html#the-old-way-using-the-cmp-parameter
sequence에 포함된 값 중 가장 큰 수 조합을 찾을 때 사용할 수 있는 코드
각 요소(n)는 cmp_to_key의 매개변수인 comparator를 거치면서 요소들의 조합된 값을 비교
"""


def comparator(a, b):
    # 문자 조합
    t1 = a + b
    t2 = b + a
    # integer 변환 -> t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution(numbers):
    # 문자형으로 변환
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


li = [3, 30, 34, 5, 9]
print(solution(li))

print(True - False)
print(False - True)

