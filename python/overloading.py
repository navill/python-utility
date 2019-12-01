import html
import numbers
from collections import abc
from functools import singledispatch

"""
@singledispatch를 이용해 함수 오버로딩을 구현 - fluent python
mainfunction에 @singledispatch 데코레이터를 이용하고 
이후 오버로딩할 메서드 또는 함수에 @mainfunction.register(type) 데코레이트 한다.
type: 구상 클래스인 int, tuple 보다 추상 클래스인 numbers.Integral, abc.MutableSequence를 사용하는 것이 좋다
-> 호환되는 자료형을 폭넓게 지원할 수 있다.

# main function -> generic function
@singledispatch
def mainfunction(obj):
    do_stuff...
    return obj

# string
@mainfunction.register(str)
def _(text):
    do_stuff...
    return text

# integer
@mainfunction.register(numbers.Integral)
def _(num):
    do_stuff...
    return num 
"""


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize({1, 2, 3}))  # <pre>{1, 2, 3}</pre>
print(htmlize(abs))  # <pre>&lt;built-in function abs&gt;</pre>
print(htmlize('Heimlich & Co.\n- a game'))  # <p>Heimlich &amp; Co.<br> - a game</p>
print(htmlize(42))  # <pre>42 (0x2a)</pre>
print(htmlize(['alpha', 66, {3, 2, 1}]))
# <ul>
# <li><p>alpha</p></li>
# <li><pre>66 (0x42)</pre></li>
# <li><pre>{1, 2, 3}</pre></li>
# </ul>
