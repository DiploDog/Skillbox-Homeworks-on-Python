import random

exc_list = [
    BaseException, SystemExit, KeyboardInterrupt, GeneratorExit,
    Exception, StopIteration, ArithmeticError, FloatingPointError,
    OverflowError, ZeroDivisionError, AssertionError, AttributeError,
    BufferError, EOFError, ImportError, LookupError, IndexError,
    KeyError, MemoryError, NameError, UnboundLocalError, Warning,
    OSError, BlockingIOError, ChildProcessError, ConnectionError,
    BrokenPipeError, ConnectionAbortedError, ConnectionRefusedError,
    ConnectionResetError, FileExistsError, FileNotFoundError,
    InterruptedError, IsADirectoryError, NotADirectoryError,
    PermissionError, ProcessLookupError, TimeoutError, ReferenceError,
    RuntimeError, NotImplementedError, SyntaxError, IndentationError,
    TabError, SystemError, TypeError, ValueError, UnicodeError,
    UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError
]

num_sum = 0
while num_sum < 777:
    num_rand = random.randint(1, 13)
    if num_rand == 1:
        raise random.choice(exc_list)
    num = int(input('Введите число: '))
    num_sum += num

print('Сумма чисел:', num_sum)

