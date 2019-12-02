def vowel(c):
    return c.lower() in 'aeiou'


list(filter(vowel, 'Aardvark'))
import itertools

print(list(itertools.filterfalse(vowel, 'Aardvark')))
# output: ['r', 'd', 'v', 'r', 'k']
print(list(itertools.dropwhile(vowel, 'Aardvark')))
# output: ['r', 'd', 'v', 'a', 'r', 'k']
print(list(itertools.takewhile(vowel, 'Aardvark')))
# output: ['A', 'a']
print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
# output: ['A', 'r', 'd', 'a']
print(list(itertools.islice('Aardvark', 4)))
# output: ['A', 'a', 'r', 'd']
print(list(itertools.islice('Aardvark', 4, 7)))
# output: ['v', 'a', 'r']
print(list(itertools.islice('Aardvark', 1, 7, 2)))
# output: ['a', 'd', 'a']
