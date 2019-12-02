## 유용한 제너레이터 함수

predicate - 인수 하나를 받는 불리언형 함수

### Filtering

**`itertools.compress(it, selector_it)`** : 두 개의 반복형을 병렬로 소비. it에 대응되는 selector_it이 참일 경우 it 항목 생성

**`itertools.dropwhile(predicate, it)`** : predicate가 참일 동안 it을 **소비**한 후 남아있는 항목 모두 생성

**`filter(predicate, it)` :** predicate(it)이 참일 경우 각 항목 생성, predicate가 None일 경우(더 이상 항목이 없을 경우) 참인 항목 모두 생성

**`itertools.filterfalse(predicate, it)`** : filter의 반대 논리

**`itertools.islice(it.stop) or .islice(it, start, stop, step=1)`** : s[:stop], s[start:stop:step]과 유사한 슬라이싱의 느긋한 연산

**`itertools.takewhile(predicate, it)`** : predicate가 참일 동안 모든 항목을 생성하고 항목이 없을 경우 중단

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

### Mapping

두 개 이상의 반복형을 입력 받는 경우, 하나라도 소진되면 출력 중단

**`itertools.accumulate(it, [func])`** : 누적된 합계 출력. func을 제공할 경우, 처음 두 개의 항목에 func를 적용한 결과를 첫 번째 값으로 생성하면서 it 순환

**`enumerate(it, start=0)`** : (index, value) 형태의 튜플 생성.

**`map(func, it1, [it2, ..., itN])`** : func을 각 it에 적용해 결과 생성. func은 N개의 인수를 받을 수 있어야한다(병렬 소비).

**`itertools.starmap(func, it)`** : it의 각 항목에 func를 적용해 결과 생성. it는 iit 항목을 생성하고 func(*iit) 형태로 호출된다.

    import itertools
    import operator
    
    
    # itertools.accumulate 예제
    sample=[5,4,2,8,7,6,3,0,9,1] 
    
    list(itertools.accumulate(sample)) # [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
    list(itertools.accumulate(sample, min)) # [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
    list(itertools.accumulate(sample, max)) # [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
    
    
    list(itertools.accumulate(sample, operator.mul)) # [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
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

### Merge

여러 반복형을 입력받아 항목 생성. 보통 반복형 생성자의 인수(예:  list(itertools.chain))로 사용한다.

- 순차 소비
    - **`itertools.chain(it1, [... , itN])`** : it1의 모든 항목 생성 후 나머지 반복형을 차례대로 생성.
    - **`itertools.chain.from_iterable(it)`** : it에서 생성된 반복형 객체의 모든 항목 생성.

            import itertools
            
            print(list(itertools.chain('ABC', range(2)))) 
            # ['A', 'B', 'C', 0, 1]
            print(list(itertools.chain(enumerate('ABC')))) 
            # [(0, 'A'), (1, 'B'), (2, 'C')]
            print(list(itertools.chain.from_iterable(enumerate('ABC')))) 
            # [0, 'A', 1, 'B', 2, 'C']

- 병렬 소비
    - **`itertools.product(it1, [... , itN, repeat=1])`** : (느긋한)데카르트 곱 연산. 각 it 항목을 이용해서 중첩된 for 루프를 생성하듯이 N-튜플을 생성. repeat은 it이 두 번 이상 소비되도록(반복) 허용.

            import itertools
            
            print(list(itertools.product('ABC', range(2))))
            # [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
            suits = 'spades hearts diamonds clubs'.split()
            print(list(itertools.product('AK', suits)))
            # [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'), 
            # ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
            print(list(itertools.product('ABC')))
            # [('A',), ('B',), ('C',)]
            print(list(itertools.product('ABC', repeat=2))) #
            # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
            # ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
            print(list(itertools.product(range(2), repeat=3)))
            # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
            rows = itertools.product('AB', range(2), repeat=2)
            for row in rows:
            		print(row)
            # output
            ('A', 0, 'A', 0)
            ('A', 0, 'A', 1)
            ('A', 0, 'B', 0)
            ('A', 0, 'B', 1)
            ('A', 1, 'A', 0)
            ('A', 1, 'A', 1)
            ('A', 1, 'B', 0)
            ('A', 1, 'B', 1)
            ('B', 0, 'A', 0)
            ('B', 0, 'A', 1)
            ('B', 0, 'B', 0)
            ('B', 0, 'B', 1)
            ('B', 1, 'A', 0)
            ('B', 1, 'A', 1)
            ('B', 1, 'B', 0)
            ('B', 1, 'B', 1)

    - **`zip(it1, [..., itN])`** :각 it의 항목을 병렬로 소비해서 N-튜플 생성. 어느하나의 it가 모두 소모되면 중단.
    - **`itertools.zip_longe(it1, [..., itM, fillvalue=None])`** : zip과 유사. 최종 it이 모두 소모될 때 까지 빈 칸을 fillvalue로 채워가며 생성.

            import itertools
            
            print(list(zip('ABC', range(5)))) 
            # [('A', 0), ('B', 1), ('C', 2)]
            print(list(zip('ABC', range(5), [10, 20, 30, 40]))) 
            # [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
            print(list(itertools.zip_longest('ABC', range(5)))) 
            # [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
            print(list(itertools.zip_longest('ABC', range(5), fillvalue='?'))) 
            # [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]

### Expand

입력된 항목 하나마다 하나 이상의 값을 생성하는 제너레이터 함수

- 순열 조합(combinatoric generator)
    - **`itertools.combinations(it, out_len)`**: it에 대한 out_len개의 조합 생성. → 생성된 튜플 내에 순서가 없음.
    - **`itertools.combinations_with_replacement(it, out_lne)`**: **반복된 항목들의 조합을 포함**하고, it으로 생성된 항목에서 out_len개의 조합 생성. → 항목 내 중복 허용(단, 교차 중복은 허용하지 않는다.)
    - **`itertools.permutations(it, out_len=None)`**: it으로 생성된 항목에서 out_len 개 항목의 조합 생성. 기본적으로 out_len은 len(list(it). → 생성된 튜플 내에 순서가 존재함.

            list(itertools.combinations('ABC', 2)) # 중복 X
            # [('A', 'B'), ('A', 'C'), ('B', 'C')]
            list(itertools.permutations('ABC', 2)) # 항목들 간에 순서 O
            # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
            list(itertools.combinations_with_replacement('ABC', 2)) # 중복 O, 교차 허용 X
            # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
            list(itertools.product('ABC', repeat=2)) # 중복 O, 교차 허용 O
            # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

- **`itertools.count(start=0, step=1)`**: start 에서 시작해서 step만큼 증가시키며 숫자를 무한이 생성.
- **`itertools.cycle(it)`**: 각 항목의 **사본을 저장**한 후, 항목을 무한히 반복.
- **`itertools.repeat(item, [times])`**: (times만큼) 주어진 item을 무한히 반복.

        ct = itertools.count()  
        next(ct)  # 0
        # 튜플을 생성하는 것은 ()가 아니라 쉼표(,)를 기준으로 생성
        next(ct), next(ct), next(ct)
        # (1, 2, 3)
        list(itertools.islice(itertools.count(1, .3), 3))
        # [1, 1.3, 1.6]
        cy = itertools.cycle('ABC')  
        next(cy)
        # 'A'
        list(itertools.islice(cy, 7))  
        # ['B', 'C', 'A', 'B', 'C', 'A', 'B']
        rp = itertools.repeat(7)  
        next(rp), next(rp)
        # (7, 7)
        list(itertools.repeat(8, 4))  
        # [8, 8, 8, 8]
        list(map(operator.mul, range(11), itertools.repeat(5)))
        # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

### Rearrange

입력받은 반복형 안의 항목의 순서를 변경하고 새로 생성

- **`itertools.groupby(it, key=None)`:**(\<key>, \<group>) 형태의 튜플 생성. \<key>는 그룹화 기준이 되고, \<group>은 그룹 안의 항목을 생성하는 제너레이터. **정렬되어 있거나 군집화** 되어 있어야 한다.
- **`reversed(seq)`:** seq 안의 항목을 역순으로 생성. seq는 sequence 객체 이거나 **\_\_reversed\_\_()** 특별 메서드를 구현해야 한다.

        list(itertools.groupby('LLLLAAGGG'))  
        # [('L', <itertools._grouper object at 0x103084c18>), 
        # ('A', <itertools._grouper object at 0x103084e48>), 
        # ('G', <itertools._grouper object at 0x103084e80>)]
        
        for char, group in itertools.groupby('LLLLAAAGG'):  
            print(char, '->', list(group))
        # L -> ['L', 'L', 'L']
        # A -> ['A', 'A']
        # G -> ['G', 'G', 'G', 'G']
        
        animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
        animals.sort(key=len)
        print(animals)
        
        for length, group in itertools.groupby(animals, len):
            print(length, '->', list(group))
        # 3 -> ['rat', 'bat']
        # 4 -> ['duck', 'bear', 'lion']
        # 5 -> ['eagle', 'shark']
        # 7 -> ['giraffe', 'dolphin']
        
        for length, group in itertools.groupby(reversed(animals), len):
            print(length, '->', list(group))
        # 7 -> ['dolphin', 'giraffe']
        # 5 -> ['shark', 'eagle']
        # 4 -> ['lion', 'bear', 'duck']
        # 3 -> ['bat', 'rat']

- **`itertools.tee(it, n=2)`**: n개의 제너레이터로 구성된 튜플 하나 생성. 각 제너레이터는 입력된 it을 독립적으로 생성

        list(itertools.tee('ABC'))
        # [<itertools._tee object at 0x102f77548>, 
        # <itertools._tee object at 0x103097448>]
        g1, g2 = itertools.tee('ABC')
        next(g1)  # 'A'
        next(g2)  # 'A'