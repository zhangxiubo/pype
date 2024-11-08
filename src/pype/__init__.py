
from dataclasses import dataclass
import itertools


@dataclass(frozen=True)
class Box:
    value: object

class Infix:

    def __init__(self, op):
        self.op = op

    def __ror__(self, arg):
        assert isinstance(arg, Box)
        return Infix(lambda f: self.op(arg.value, f))

    def __or__(self, f):
        if f is unwrap:
            return self.op(f)
        return Box(self.op(f))


def begin(x):
    return Box(x)

def unwrap(x):
    return x

def end():
    return unwrap

@Infix
def pipe(x, f):
    return f(x)

@Infix
def pipex(x, f):
    return f(*x)

@Infix
def pipexx(x, f):
    return f(**x)

@Infix
def map(xs, f):
    yield from (f(x) for x in xs)

@Infix
def mapx(xs, f):
    yield from (f(*x) for x in xs)

@Infix
def mapxx(xs, f):
    yield from (f(**x) for x in xs)

@Infix
def flatmap(xs, f):
    yield from itertools.chain.from_iterable(f(x) for x in xs)

@Infix
def flatmapx(xs, f):
    yield from itertools.chain.from_iterable(f(*x) for x in xs)

@Infix
def flatmapxx(xs, f):
    yield from itertools.chain.from_iterable(f(**x) for x in xs)


def head(count: int):
    return lambda x: list(x)[:count]


def tail(count: int):
    return lambda x: list(x)[-count:]


def sortx(key_func):
    return lambda seq: sorted(seq, key=lambda e: key_func(*e))


def filterx(pred_func):
    return lambda seq: filter(lambda e: pred_func(*e), seq)



class Tee:

    def __init__(self) -> None:
        self.value = None

    def __call__(self, value):
        self.value = value
        return value

def tee():
    return Tee()


def sliding(iterable, window_size, stride):
    yield from zip(*(itertools.islice(iterable, i, None, stride) for i in range(window_size)))


from pype.partitioner import all_partitions 
