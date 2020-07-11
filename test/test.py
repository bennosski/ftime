import time
from profiler import timed

@timed
def f():
    time.sleep(0.1)

@timed
def g():
    time.sleep(0.2)
    f()
    
f()
g()

# print the profiler results to the screen
timed.results()