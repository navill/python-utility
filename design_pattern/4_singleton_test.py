# 1: TypeError: getinstance() takes 1 positional argument but 4 were given
# 두 번째 객체 생성 시 에러 발생(why???????)
class SingletonInstance:
    __instance = None

    @classmethod
    def getinstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kwargs):
        cls.__instance = cls(*args, **kwargs)
        cls.instance = cls.getinstance
        return cls.__instance


class MainClass(SingletonInstance):
    # 새로운 객체를 생성하더라도 정체성이 변하지 않지만,
    # 초기화된 값 또한 변하지 않기 떄문에 주의
    # 함수를 실행하기 위한 목적으로 사용
    def __init__(self, a, b, c):
        self.result = a + b + c


# a = MainClass.instance(1, 2, 3)
# print(a.result)  # 6
# print(id(a))  # 4565035048
# b = MainClass.instance(2, 3, 4)
# print(b.result)  # 6
# print(id(b))  # 4565035048


# 2: 새로운 객체 생성 -> init을 포함한 객체가 _instances에 할당
# -> 새로운 객체에 의해 생성된 초기화값은 무시됨
class SingletonType(type):
    # _instances: 초기화된 MainClass가 들어가기 때문에 동일한 클래스로
    # 객체 생성 시, 새로운 값으로 초기화되지 않는다.
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MainClass(metaclass=SingletonType):
    # 새로운 객체를 생성하더라도 정체성이 변하지 않지만,
    # 초기화된 값 또한 변하지 않기 떄문에 주의
    # 함수를 실행하기 위한 목적으로 사용
    def __init__(self, a, b, c):
        self.result = a + b + c


a = MainClass(1, 2, 3)
print(a.result)  # 6
print(id(a))  # 4565035048
b = MainClass(3, 4, 5)
print(b.result)  # 6
print(id(b))  # 4565035048


# 3: 새로운 객체 생성 시, 정체성(id)는 바뀌지 않지만 초기화(__init__)은 반영
class Singleton:
    _instance = None

    def __new__(cls, *args):
        if not isinstance(cls._instance, cls):
            # 객체 생성 후 아래의 MainClass에서 초기화가 이루어지기 때문에
            # 새로운 객체의 초기화값은 반영된다.
            cls._instance = object.__new__(cls)
        return cls._instance


class MainClass(Singleton):
    def __init__(self, a, b, c):
        self.result = a + b + c


a = MainClass(1, 2, 3)
print(a.result)  # 6
print(id(a))  # 4565035664
b = MainClass(3, 4, 5)
print(b.result)  # 12
print(id(b))  # 4565035664


# 4(from sourcemaking): 2번과 동일한 결과
class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        print(name, bases, attrs)
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MainClass(metaclass=Singleton):
    def __init__(self, a, b, c):
        self.result = a + b + c


a = MainClass(1, 2, 3)
print(a.result)  # 6
print(id(a))  # 4545081528
b = MainClass(3, 4, 5)
print(b.result)  # 6
print(id(b))  # 4545081528
