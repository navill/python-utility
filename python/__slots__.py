"""
몇 개의 속성을 포함한 많은 수의 객체를 생성할 때 __slots__을 이용하여 메모리 소모를 줄일 수 있다.
"""


# slot을 이용한 클래스
class ClassA:
    __slots__ = ('a', 'b', 'c')

    def __init__(self, a1, b1, c1):
        self.a = a1
        self.b = b1
        self.c = c1
