import datetime
from functools import reduce

from django.utils import timezone

from django.test import TestCase

# Create your tests here.
from polls.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test(self):
        time = timezone.now()
        print(time)
        time = timezone.now() + datetime.timedelta(days=30)
        print(time)
        time = timezone.now() + datetime.timedelta(days=-1)
        print(time)


def func_param(p1, p2=3, p3=3):
    print('p1:', p1)
    print('p2:', p2)
    print('p3:', p3)


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


class Test(TestCase):
    def test_func(self):
        func_param(1)
        print('===================')
        func_param(1, 2)
        print('===================')
        func_param(1, 2, 11)

    def test_测试可变参数(self):
        print(calc(1))
        print('===================')
        print(calc(2))

    def test_关键字参数(self):
        person('NOHI', 35)
        person('NOHI', 35, city='NJ')
        person('NOHI', 35, job='code')
        person('NOHI', 35, city='NJ', job='code')

    #


def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 3


class Test生成器械(TestCase):
    def test_fib1(self):
        fib1(6)

    def test_生成器(self):
        f = fib2(6)
        for n in f:
            print(n)

    def test_Generate(self):
        f = odd()
        print(next(f))
        print(next(f))
        print(next(f))
        print(next(f))


def triangles():
    L = [1]
    yield L
    L = [1, 1]
    yield L
    while True:
        TMP = [1]
        for i, value in enumerate(L):
            if i == (len(L) - 1):
                TMP.append(value)
            else:
                TMP.append(value + L[i + 1])
        L = TMP
        yield L


class TestGenerator(TestCase):
    def test_triangles(self):
        f = triangles()
        print(next(f))
        print(next(f))
        print(next(f))
        print(next(f))
        print(next(f))
        print(next(f))
        print(next(f))

    def test_1(self):
        n = 0
        results = []
        for t in triangles():
            results.append(t)
            n = n + 1
            if n == 10:
                break

        for t in results:
            print(t)

        if results == [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        ]:
            print('测试通过!')
        else:
            print('测试失败!')


def add(x, y):
    return x * 10 + y


class TestFunctionPrograme(TestCase):
    def test_num(self):
        v = reduce(add, [1, 3, 5, 7, 9])
        print(v)
