import itertools

print(list(zip('ABC', range(5))))
# [('A', 0), ('B', 1), ('C', 2)]
print(list(zip('ABC', range(5), [10, 20, 30, 40])))
# [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
print(list(itertools.zip_longest('ABC', range(5))))
# [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))
# [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]


# 순차 소비
print(list(itertools.chain('ABC', range(2))))
# ['A', 'B', 'C', 0, 1]
print(list(itertools.chain(enumerate('ABC'))))
# [(0, 'A'), (1, 'B'), (2, 'C')]
print(list(itertools.chain.from_iterable(enumerate('ABC'))))
# [0, 'A', 1, 'B', 2, 'C']


# 병렬 소비
print(list(itertools.product('ABC', range(2))))
# [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product('AK', suits)))
# [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'),
# ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
print(list(itertools.product('ABC')))
# [('A',), ('B',), ('C',)]
print(list(itertools.product('ABC', repeat=2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
# ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
print(list(itertools.product(range(2), repeat=3)))
# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
rows = itertools.product('AB', range(2), repeat=2)
for row in rows:
    print(row)

temp = itertools.product('abc', range(5))
for i in temp:
    print(i)
