import hello
import fib

if __name__ == '__main__':
    #  cookbook:  https://python3-cookbook.readthedocs.io/zh_CN/latest/c15/p01_access_ccode_using_ctypes.html
    #  https://en.wikibooks.org/wiki/Python_Programming/Extending_with_C
    #  使用swig更简单[pure c代码]
    #  使用CFFI
    hello.say_hello('lwz')
    fib.fib(10)


