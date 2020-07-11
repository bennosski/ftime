# ftime

A decorator to profile function performance. 
Simply add the ```@timed``` decorator to any function or class method for which to measure runtime. 
Call ```timed.results()``` to neatly print detailed timing information to the console including:
   - number of function calls
   - total runtime for each function
   - average runtime for each function
   - total runtime of the program
   
```ruby
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
```

output: 
```
 --------------------------------------------- 
|               Runtime Profile               |
|---------------------------------------------|
| name      |   %   | total time | time/call  |
|---------------------------------------------|
| g    (x1) | 80.5% | 1.175e-01s |            |
| f    (x1) | 10.4% | 1.525e-02s |            |
|---------------------------------------------|
| program           | 1.460e-01s |            |
 --------------------------------------------- 
```
