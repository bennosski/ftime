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
    return [0 for i in range(10000)]

@timed
def g():
    f()
    return [0 for i in range(10000)]
    
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
| f    (x2) | 60.5% | 1.581e-03s | 7.907e-04s |
| g    (x1) | 22.4% | 5.858e-04s |            |
|---------------------------------------------|
| program           | 2.612e-03s |            |
 ---------------------------------------------
```
