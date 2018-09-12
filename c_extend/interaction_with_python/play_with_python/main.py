# -*- coding: utf-8 -*-

"""
@Time    : 18-9-11
@Author  : leemiracle
"""
import time


def _introduction_build_in_func():
    pass
    """
    abs():绝对值,浮点/int时,返回整值. 复数complex(a, b)则返回它的模
    delattr():删除class类中的属性
    hash():得到字典key的hash值(1和1.0的值是一样的,复写__hash__():使用hash函数是调用)
    memoryview():在bytes上包装了一层[a bytes view on another object (PyMemory)]
    set()
    all():判断可遍历对象的元素 bool(element)
    dict(): 创建一个新的字典,可以用以下几个类型 dict(zip(['one', 'two', 'three'], [1, 2, 3])) dict([('two', 2), ('one', 1), ('three', 3)])  dict({'three': 3, 'one': 1, 'two': 2})
    help()
    min()
    setattr()
    any():类似all,但只要bool(e)则为True
    dir(): 返回对象的可用属性[最相关的/而不是最全的]/没有参数会返回当前local范围内的变量名[ __dir__()可定义该函数返回的类型\也可自定义 __getattr__()/__getattribute__()来修改]
    hex()
    next():调用__next__() 
    slice():返回slice对象
    ascii(): 类似repr(),用\\u表示非ascii码
    divmod(): divmod(num1, num2), 返回元组(商, 余数)
    id()
    object():无特征的对象
    sorted(): 被排序
    bin(): 数字转换为二进制表示[字符串]
    enumerate():返回可枚举对象, 调用__next__()会返回元组
    input()
    oct():将int的10进制变成8进制
    staticmethod():无任何绑定以及无隐式参数[classmethod绑定在类上,并第一个参数隐式传递类型,派生类是将自己的类传递] 以及无修饰词的方法,相比, 
    bool():判断对象的bool值
    eval(): 执行表达式,[可以和 globals以及locals变量交互]
    int()
    open():打开文件返回file对象(path-like 对象),mode中有 'x'[独创模式]
    str(): 字符串类型,  __str__()
    breakpoint():拉到debug定义点[python 3.7], 类似pdb的调试
    exec(): Python代码的动态执行[可以是字符串/code对象]
    isinstance(): 判断对象是否是类的实例[Abstract Base Classes:抽象基类(abc)/有大量的抽象方法][https://docs.python.org/3/library/collections.abc.html]
    ord():将Unicode转为int 
    sum(): 可定义类似slice的位置信息, 要更高精度则用 math.fsum(),  串联一系列iterables 使用 itertools.chain()
    bytearray():是可以更改的bytes类型
    filter()
    issubclass():是否是子类
    pow(): x的y次方%z pow(x, y) % z)
    super(): 返回 委托给父类或兄弟类型 的"代理对象":常用的 super('cls', self).method(args),  __mro__返回类型搜索顺序[和getattr一致]
    bytes():是不可更改的bytes,类似string
    float()
    iter(): 返回 iterator类型对象, [没有 哨兵对象则需要 支持iteration协议或sequence协议.][有,只需要第一个参数是callable对象就可以]
    print()
    tuple(): 元组类型
    callable():是否callable,也就是obj是否有 __call__() 方法
    format()
    len():返回 序列或者容器的 长度
    property():将函数包装成属性, 且改属性可以用setter/deleter包装
    type(): 检查类型, 或定义类type(name, bases, dict)  [用代码产生代码：装饰器、类装饰器和元类, 以及包括签名对象、使用 exec() 执行代码以及对内部函数和类的反射技术等]
    chr():将int转换成Unicode码(字符看着相同,但Unicode码不一样)
    frozenset(): set必须是能被hash的, 而frozenset只需要元素是可遍历的, 要表达set类型的set,则内部的set必须是frozenset
    list(): 可修改的序列
    range()不可更改的序列类型
    vars():　返回__dict__ 属性值
    classmethod()
    getattr():获取class类中的属性,类似object.food 
    locals():返回当前本地的变量
    repr():包含一个可以被打印的 字符串[复写__repr__()]
    zip()：制作一个迭代器来聚合　其他迭代器的值
    compile():将source编译, eval\single\exec[字节码][a = compile('bool(1)', 'test_comple', 'eval')], 之后就可以执行[eval(a)]
    globals()
    map(): 返回iterator类型对象[对每项执行了func后的结果]
    reversed():逆序的iterator, 覆写__reversed__()
    __import__()
    complex(): 复数
    hasattr()
    max(): 在iterable或多个args参数中,返回最大的值[可定义key参数:类似list.sort()]
    round():返回 数的四舍五入结果
    :return:
    """




def test_buidin_func():
    source = """for i in range(0, 10): print(i) print(i**2)"""
    class A(object):
        def __init__(self, name):
            self.name = name
            print("A: {}".format(name))
            print("A:class class_foo {}".format(A.class_foo())) # 传入A类型
            print("A:obj class_foo {}".format(self.class_foo())) # 会传入self的类型[有可能是派生类]

        def foo(self):
            print(self)

        @classmethod
        def class_foo(cls):
            print("A class_foo is invoked : {}".format(cls.__name__))

        @staticmethod
        def static_foo():
            print("hhhhh")

    # class C(A):
    #     def __init__(self, name):
    #         super().__init__(name)

    class D(object):
        pass

    class B(A, D):
        def __init__(self, name):
            super(B, self).__init__(name) # 将self[B类型]传入A中
            B.class_foo()
            B.static_foo()
            print(B.__mro__)  # 打印类型的搜索顺序
    b = B('调皮')
    import sys
    sys.stdout.flush()
    for i in range(0, 10):  # 覆盖打印值
        # print(str(i), end='')
        # print('\r', end='')
        time.sleep(0.7)
        sys.stdout.write("%d \r" % i, )
        sys.stdout.flush()
    print('\n')


def _introduction_for_module():
    import unicodedata
    """
    the Unicode Character Database (UCD):处理Unicode字符串，需要确保所有字符串在底层有相同的表示
    unicodedata.normalize('NFC', s2) 测试字符类的工具函数
    """


def main():
    # breakpoint()
    # import sys
    # sys.breakpointhook()/
    import math
    math.log(11, 9)
    test_buidin_func()


if __name__ == '__main__':
    main()
