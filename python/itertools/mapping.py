import itertools
import operator

# itertools.accumulate 예제
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

list(itertools.accumulate(sample))  # [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
list(itertools.accumulate(sample, min))  # [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
list(itertools.accumulate(sample, max))  # [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]

list(itertools.accumulate(sample, operator.mul))  # [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]

# itertools를 이용한 매핑 제너레이터 예제
list(enumerate('albatroz', 1))
# [(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]

list(map(operator.mul, range(11), range(11)))
# 정수의 제곱 출력: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list(map(operator.mul, range(11), [2, 4, 8]))
# 가장 짧은 it에 의해 반복 중단: [0, 4, 16]
list(map(lambda a, b: (a, b), range(11), [2, 4, 8]))
# zip 모방: [(0, 2), (1, 4), (2, 8)]


list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))
# 인덱스만큼 각 단어를 복사(*연산): ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(sample), 1)))
# 이동 평균: [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333,
# 5.0, 4.375, 4.888888888888889, 4.5]
