"""
여러개의 속성을 포함한 많은 수의 객체를 생성할 때 __slots__을 이용하여 메모리 소모를 줄일 수 있다.
https://www.notion.so/afmadadans/Chapter-9-5549dcf350224b7285197067dda875de#095c1cd6ed0943e098d02db41f25a2e6
"""


# slot을 이용한 클래스
class ClassA:
    __slots__ = ('a', 'b', 'c')

    def __init__(self, a1, b1, c1):
        self.a = a1
        self.b = b1
        self.c = c1
