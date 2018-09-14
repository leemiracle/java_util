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


def _introduction_constants():
    pass
    """
    NotImplemented: 用于被特定二元方法，被返回的特殊值
    Ellipsis：　用户自定义的容器类型［扩展ｓｌｉｃｉｎｇ语法］
    __debug__
    
    site模块［python包安装的位置Site-specific configuration hook］:　解析器初始话的时候，被使用
        quit
        exit
        license
    """


def _introduction_types():
    pass
    """numerics数字, sequences序列, mappings映射, classes类, instances实例 and exceptions异常.
    真值比较：__bool__(), __len__()
    Boolean操作
    比较: 等于[ __eq__(), __lt__(), __le__(), __gt__(), __ge__()], is [object identity: id(object值相同,则is是相同的)]
    
    numerics数字: int[Booleans 是int的子类, bit操作], float, complex
    Iterator Types: __iter__(), __next__()
    Sequence Types — list, tuple, range
    Text Sequence Type — str: 单引号,双引号,三引号[printf-style String Formatting]
    Binary Sequence Types — bytes, bytearray, memoryview
    Set Types — set, frozenset
    Mapping Types — dict
    Context Manager Types: with 声明[__enter__()/__exit__()方法]
    
    Modules:只开放了name属性, 每个模块都有特殊属性 __dict__
    Classes and Class Instances:
    Functions
    Methods
    Code Objects
    Type Objects
    The Null Object
    The Ellipsis Object
    The NotImplemented Object
    Boolean Values
    Internal Objects
    
    特殊的属性
    __mro__: 查找基类
    __subclasses__(): 查找子类
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


def _introduct_Exceptions():
    pass
    """异常处理: 基础数据类型异常 / 操作系统的异常
    
    Base classes: BaseException / Exception / ArithmeticError除0, 溢出等 / BufferError 操作buff / LookupError 找key,index, mapping等
    Concrete exceptions 常用:
    OS exceptions: OSError的子类
    
    Warnings 警告:
    """


def TextProcessingServices():
    pass
    '''文字处理: 字符串操作 / 正则 / 文本对比 / 字符编码 / buff / 文本读写
    
    
    string — 常用字符串操作: 常量/字符串定制格式化[format/Template]/ 第一个字符大写
    re — Regular expression operations: 语法[re.compile("规则")变为pattern]/ several functions, constants, and an exception / 对象[正则/Match/]
    difflib — Helpers for computing deltas : 对比字符串的异同
    textwrap — Text wrapping and filling: 连接函数[用来填充词/ 缩进 对齐]
    unicodedata — Unicode Database: the Unicode Character Database (UCD):处理Unicode字符串，需要确保所有字符串在底层有相同的表示, unicodedata.normalize('NFC', s2) 测试字符类的工具函数
    stringprep — Internet String Preparation 互联网字符集[判断字符是不是在一个table内]
    readline — GNU readline interface: 方便Python编译器 读/写 历史文件[Init file / Line buffer / History file / History list / Startup hooks / Completion]
    rlcompleter — Completion function for GNU readline
    '''


def BinaryDataServices():
    pass
    """ 二进制数据: Python的bytes,以及c 的structs
    struct: 将python的值 通过Python的bytes对象, 和c的structs 的相互转换
    codecs: 访问Python编译器的 [编解码器注册表][语言汉字编码]
    """


def DataTypes():
    pass
    """数据类型: 日期 / 容器[队列等] / types / weakref弱引用 / 枚举类型  
    datetime — Basic date and time types[timedelta\时区信息:tzinfo(抽象基础类), timezone]
    calendar — General calendar-related functions
    collections — Container datatypes容器数据类型[]
        namedtuple() 有fieldname的元组
        deque 双端队列,类似list
        ChainMap mapps属性是个list类型append了map对象,dict-like class for creating a single view of multiple mappings
        Counter	将了hash值相同的对象 dict subclass for counting hashable objects
        OrderedDict	有顺序的字典 dict subclass that remembers the order entries were added
        defaultdict	为字典默认类型 dict subclass that calls a factory function to supply missing values
        UserDict 在dic包装了层 wrapper around dictionary objects for easier dict subclassing
        UserList	wrapper around list objects for easier list subclassing
        UserString	wrapper around string objects for easier string subclassing
    collections.abc — 类中特定的接口 Abstract Base Classes for Containers容器的基础抽象类
    heapq — Heap queue algorithm 堆队列算法
    bisect — 比较算法 Array bisection algorithm 二分法
        >>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        ...     i = bisect(breakpoints, score)
        ...     return grades[i]
        ...
        >>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
        ['F', 'A', 'C', 'C', 'B', 'A', 'A']
    array — Efficient arrays of numeric values 高效的数值类数组
    weakref — Weak references 弱引用
    types — Dynamic type creation and names for built-in types 在内置的类型上创建动态类型
    copy — Shallow and deep copy operations 浅复制,或者深复制
    pprint — Data pretty printer打印
    reprlib — Alternate repr() implementation替代repr
    
    enum — Support for enumerations枚举/支持枚举
    """


def NumericMathematicalModules():
    pass
    """数值计算模块
    numbers — Numeric abstract base classes
    math — Mathematical functions
    cmath —复数Mathematical functions for complex numbers
    decimal — Decimal fixed point and floating point arithmetic
    fractions — 有理数 Rational numbers
    random — 随机数 Generate pseudo-random numbers
    statistics — 数学统计算法Mathematical statistics functions
    """

def FunctionalProgrammingModules():
    pass
    """函数式编程: 迭代器 / 函数 / 加减乘除等操作
    itertools — 高效循环[代数方法]Functions creating iterators for efficient looping
    functools — 包装现有的函数 Higher-order functions and operations on callable objects
    operator — 比内置的操作更快(加减乘除等)Standard operators as functions
    """

def FileDirectoryAccess():
    pass
    """操作 文件/目录
    pathlib — Object-oriented filesystem paths
    os.path — 路径名操作Common pathname manipulations
    fileinput — 读写文件 Iterate over lines from multiple input streams
    stat — 获取解释器的state Interpreting stat() results
    filecmp — 文件和目录的对比 File and Directory Comparisons
    tempfile — 生成临时文件或目录 Generate temporary files and directories
    glob — pattern查找文件路径 Unix style pathname pattern expansion
    fnmatch — unix风格的pattern匹配/ re的pattern Unix filename pattern matching
    linecache — [缓存读取的line] Random access to text lines
    shutil — High-level file operations
    macpath — Mac OS 9 path manipulation functions
    """

def DataPersistence():
    pass
    """ 数据持久化:保存数据
    12.1. pickle — 序列化[保存 数据结构或状态 转换成可取用格式] Python object serialization
    12.2. copyreg — Register pickle support functions
    12.3. shelve — python对象序列化 Python object persistence
    12.4. marshal — 二进制层面 读写Python值 Internal Python object serialization
    12.5. dbm — 读取DBM数据库[存储相对比较静态的索引数据] Interfaces to Unix “databases”
    12.6. sqlite3 —小型的db数据库 DB-API 2.0 interface for SQLite databases
    """

def DataCompressionArchiving():
    pass
    """ 数据压缩
    13.1. zlib — Compression compatible with gzip
    13.2. gzip — Support for gzip files
    13.3. bz2 — Support for bzip2 compression
    13.4. lzma — Compression using the LZMA algorithm
    13.5. zipfile — Work with ZIP archives
    13.6. tarfile — Read and write tar archive files
    """


def FileFormats():
    pass
    """ 不同的文件类型
    14.1. csv — CSV File Reading and Writing
    14.2. configparser — Configuration file parser
    14.3. netrc — [FTP配置] netrc file processing
    14.4. xdrlib — [xdr外部数据表示标准]Encode and decode XDR data
    14.5. plistlib — Generate and parse Mac OS X .plist files
    """

def CryptographicServices():
    pass
    """
    15.1. hashlib — Secure hashes and message digests
    15.2. hmac — Keyed-Hashing for Message Authentication
    15.3. secrets — Generate secure random numbers for managing secrets
    """


def GenericOperatingSystemServices():
    pass
    """
    16.1. os — Miscellaneous operating system interfaces
    16.2. io — Core tools for working with streams
    16.3. time — Time access and conversions
    16.4. argparse — Parser for command-line options, arguments and sub-commands
    16.5. getopt — C-style parser for command line options
    16.6. logging — Logging facility for Python
    16.7. logging.config — Logging configuration
    16.8. logging.handlers — Logging handlers
    16.9. getpass — Portable password input
    16.10. curses — Terminal handling for character-cell displays
    16.11. curses.textpad — Text input widget for curses programs
    16.12. curses.ascii — Utilities for ASCII characters
    16.13. curses.panel — A panel stack extension for curses
    16.14. platform — Access to underlying platform’s identifying data
    16.15. errno — Standard errno system symbols
    16.16. ctypes — A foreign function library for Python
    """


def ConcurrentExecution():
    pass
    """
    17.1. threading — Thread-based parallelism
    17.2. multiprocessing — Process-based parallelism
    17.3. The concurrent package
    17.4. concurrent.futures — Launching parallel tasks
    17.5. subprocess — Subprocess management
    17.6. sched — Event scheduler
    17.7. queue — A synchronized queue class
    17.8. _thread — Low-level threading API
    17.9. _dummy_thread — Drop-in replacement for the _thread module
    17.10. dummy_threading — Drop-in replacement for the threading module
    """


def ContextVariables():
    pass
    """
    contextvars — Context Variables
    18.1. Context Variables
    18.2. Manual Context Management
    18.3. asyncio support
    """


def InterprocessCommunicationNetworking():
    pass
    """
    19.1. socket — Low-level networking interface
    19.2. ssl — TLS/SSL wrapper for socket objects
    19.3. select — Waiting for I/O completion
    19.4. selectors — High-level I/O multiplexing
    19.5. asyncio — Asynchronous I/O, event loop, coroutines and tasks
    19.6. asyncore — Asynchronous socket handler
    19.7. asynchat — Asynchronous socket command/response handler
    19.8. signal — Set handlers for asynchronous events
    19.9. mmap — Memory-mapped file support
    """

def InternetDataHandling():
    pass
    """
    20.1. email — An email and MIME handling package
    20.2. json — JSON encoder and decoder
    20.3. mailcap — Mailcap file handling
    20.4. mailbox — Manipulate mailboxes in various formats
    20.5. mimetypes — Map filenames to MIME types
    20.6. base64 — Base16, Base32, Base64, Base85 Data Encodings
    20.7. binhex — Encode and decode binhex4 files
    20.8. binascii — Convert between binary and ASCII
    20.9. quopri — Encode and decode MIME quoted-printable data
    20.10. uu — Encode and decode uuencode files
    """


def StructuredMarkupProcessingTools():
    pass
    """
    21.1. html — HyperText Markup Language support
    21.2. html.parser — Simple HTML and XHTML parser
    21.3. html.entities — Definitions of HTML general entities
    21.4. XML Processing Modules
    21.5. xml.etree.ElementTree — The ElementTree XML API
    21.6. xml.dom — The Document Object Model API
    21.7. xml.dom.minidom — Minimal DOM implementation
    21.8. xml.dom.pulldom — Support for building partial DOM trees
    21.9. xml.sax — Support for SAX2 parsers
    21.10. xml.sax.handler — Base classes for SAX handlers
    21.11. xml.sax.saxutils — SAX Utilities
    21.12. xml.sax.xmlreader — Interface for XML parsers
    21.13. xml.parsers.expat — Fast XML parsing using Expat
    """

def InternetProtocolsSupport():
    pass
    """
    22.1. webbrowser — Convenient Web-browser controller
    22.2. cgi — Common Gateway Interface support
    22.3. cgitb — Traceback manager for CGI scripts
    22.4. wsgiref — WSGI Utilities and Reference Implementation
    22.5. urllib — URL handling modules
    22.6. urllib.request — Extensible library for opening URLs
    22.7. urllib.response — Response classes used by urllib
    22.8. urllib.parse — Parse URLs into components
    22.9. urllib.error — Exception classes raised by urllib.request
    22.10. urllib.robotparser — Parser for robots.txt
    22.11. http — HTTP modules
    22.12. http.client — HTTP protocol client
    22.13. ftplib — FTP protocol client
    22.14. poplib — POP3 protocol client
    22.15. imaplib — IMAP4 protocol client
    22.16. nntplib — NNTP protocol client
    22.17. smtplib — SMTP protocol client
    22.18. smtpd — SMTP Server
    22.19. telnetlib — Telnet client
    22.20. uuid — UUID objects according to RFC 4122
    22.21. socketserver — A framework for network servers
    22.22. http.server — HTTP servers
    22.23. http.cookies — HTTP state management
    22.24. http.cookiejar — Cookie handling for HTTP clients
    22.25. xmlrpc — XMLRPC server and client modules
    22.26. xmlrpc.client — XML-RPC client access
    22.27. xmlrpc.server — Basic XML-RPC servers
    22.28. ipaddress — IPv4/IPv6 manipulation library
    """


def MultimediaServices():
    pass
    """
    23.1. audioop — Manipulate raw audio data
    23.2. aifc — Read and write AIFF and AIFC files
    23.3. sunau — Read and write Sun AU files
    23.4. wave — Read and write WAV files
    23.5. chunk — Read IFF chunked data
    23.6. colorsys — Conversions between color systems
    23.7. imghdr — Determine the type of an image
    23.8. sndhdr — Determine type of sound file
    23.9. ossaudiodev — Access to OSS-compatible audio devices
    """

def Internationalization():
    pass
    """
    24.1. gettext — Multilingual internationalization services
    24.2. locale — Internationalization services  
    """

def ProgramFrameworks():
    pass
    """
    25.1. turtle — Turtle graphics
    25.2. cmd — Support for line-oriented command interpreters
    25.3. shlex — Simple lexical analysis
    """

def GraphicalUserInterfaceswithTk():
    pass
    """
    26.1. tkinter — Python interface to Tcl/Tk
    26.2. tkinter.ttk — Tk themed widgets
    26.3. tkinter.tix — Extension widgets for Tk
    26.4. tkinter.scrolledtext — Scrolled Text Widget
    26.5. IDLE
    26.6. Other Graphical User Interface Packages
    """

def DevelopmentTools():
    pass
    """
    27.1. typing — Support for type hints
    27.2. pydoc — Documentation generator and online help system
    27.3. doctest — Test interactive Python examples
    27.4. unittest — Unit testing framework
    27.5. unittest.mock — mock object library
    27.6. unittest.mock — getting started
    27.7. 2to3 - Automated Python 2 to 3 code translation
    27.8. test — Regression tests package for Python
    27.9. test.support — Utilities for the Python test suite
    27.10. test.support.script_helper — Utilities for the Python execution tests
    """

def DebuggingandProfiling():
    pass
    """
    28.1. bdb — Debugger framework
    28.2. faulthandler — Dump the Python traceback
    28.3. pdb — The Python Debugger
    28.4. The Python Profilers
    28.5. timeit — Measure execution time of small code snippets
    28.6. trace — Trace or track Python statement execution
    28.7. tracemalloc — Trace memory allocations
    """

def SoftwarePackagingAndDistribution():
    pass
    """
    29.1. distutils — Building and installing Python modules
    29.2. ensurepip — Bootstrapping the pip installer
    29.3. venv — Creation of virtual environments
    29.4. zipapp — Manage executable python zip archives
    """

def PythonRuntimeServices():
    pass
    """
    30.1. sys — System-specific parameters and functions
    30.2. sysconfig — Provide access to Python’s configuration information
    30.3. builtins — Built-in objects
    30.4. __main__ — Top-level script environment
    30.5. warnings — Warning control
    30.6. dataclasses — Data Classes
    30.7. contextlib — Utilities for with-statement contexts
    30.8. abc — Abstract Base Classes
    30.9. atexit — Exit handlers
    30.10. traceback — Print or retrieve a stack traceback
    30.11. __future__ — Future statement definitions
    30.12. gc — Garbage Collector interface
    30.13. inspect — Inspect live objects
    30.14. site — Site-specific configuration hook
    """

def CustomPythonInterpreters():
    pass
    """
    31.1. code — Interpreter base classes
    31.2. codeop — Compile Python code
    """

def ImportingModules():
    pass
    """
    32.1. zipimport — Import modules from Zip archives
    32.2. pkgutil — Package extension utility
    32.3. modulefinder — Find modules used by a script
    32.4. runpy — Locating and executing Python modules
    32.5. importlib — The implementation of import
    """

def PythonLanguageServices():
    pass
    """
    33.1. parser — Access Python parse trees
    33.2. ast — Abstract Syntax Trees
    33.3. symtable — Access to the compiler’s symbol tables
    33.4. symbol — Constants used with Python parse trees
    33.5. token — Constants used with Python parse trees
    33.6. keyword — Testing for Python keywords
    33.7. tokenize — Tokenizer for Python source
    33.8. tabnanny — Detection of ambiguous indentation
    33.9. pyclbr — Python class browser support
    33.10. py_compile — Compile Python source files
    33.11. compileall — Byte-compile Python libraries
    33.12. dis — Disassembler for Python bytecode
    33.13. pickletools — Tools for pickle developers
    """

def MiscellaneousServices():
    pass
    """
    34.1. formatter — Generic output formatting
    """

def MSWindowsSpecificServices():
    pass
    """
    35.1. msilib — Read and write Microsoft Installer files
    35.2. msvcrt — Useful routines from the MS VC++ runtime
    35.3. winreg — Windows registry access
    35.4. winsound — Sound-playing interface for Windows
    """

def UnixSpecificServices():
    pass
    """
    36.1. posix — The most common POSIX system calls
    36.2. pwd — The password database
    36.3. spwd — The shadow password database
    36.4. grp — The group database
    36.5. crypt — Function to check Unix passwords
    36.6. termios — POSIX style tty control
    36.7. tty — Terminal control functions
    36.8. pty — Pseudo-terminal utilities
    36.9. fcntl — The fcntl and ioctl system calls
    36.10. pipes — Interface to shell pipelines
    36.11. resource — Resource usage information
    36.12. nis — Interface to Sun’s NIS (Yellow Pages)
    36.13. syslog — Unix syslog library routines
    """


def SupersededModules():
    pass
    """
    37.1. optparse — Parser for command line options
    37.2. imp — Access the import internals
    """

def UndocumentedModules():
    pass
    """
    38.1. Platform specific modules
    """

def main():
    # breakpoint()
    # import sys
    # sys.breakpointhook()/
    # test_buidin_func()
    # print(__dict__)
    import datetime
    pass


def define_abstract_class():
    from typing import (
        AnyStr, Optional, SupportsAbs, Tuple, Union, overload,
        ClassVar,
    )
    import datetime

    class tzinfo:
        def tzname(self, dt: Optional[datetime]) -> str: ...
        def utcoffset(self, dt: Optional[datetime]) -> Optional[datetime.timedelta]: ...
        def dst(self, dt: Optional[datetime]) -> Optional[datetime.timedelta]: ...
        def fromutc(self, dt: datetime) -> datetime: ...

if __name__ == '__main__':
    main()
