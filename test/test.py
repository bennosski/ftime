import time
from profiler import timed

@timed
def f(x):
    time.sleep(0.1)
    return x

@timed
def g(x):
    time.sleep(0.2)
    return x**2


f(1)
f(2)
g(3)
