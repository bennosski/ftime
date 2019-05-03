import time
from profiler import timed


@timed
def f():
    print('hi')

@timed
def g():
    print('there')

f()
f()
g()
