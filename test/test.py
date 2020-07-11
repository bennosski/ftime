from ftime import timed

@timed
def f():
    return [i**i for i in range(1000)]

@timed
def g():
    return [i*j for i in range(1000) for j in range(1000)]
    
    
f()
g()

# print the profiler results to the screen
timed.results()
