# ftime

A decorator to profile function performance. 
Simply add the ```@timed``` decorator to any function or class method for which to measure runtime. 
Call ```timed.results()``` to neatly print detailed timing information to the console including:
   - number of function calls
   - total runtime of each function
   - average runtime of each function
   - total runtime of the program
   - total runtime of each function as a percentage of the total runtime of the program
   
```ruby
from ftime import timed

@timed
def f():
    return [i*j for i in range(1000) for j in range(1000)]
    

@timed
def g():
    f()
    return [i**i for i in range(1000)]

    
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
| name      | total time | time/call  |   %   |
|---------------------------------------------|
| f    (x2) | 3.593e-01s | 1.796e-01s | 87.0% |
| g    (x1) | 1.882e-01s |            | 45.6% |
|---------------------------------------------|
| program   | 4.128e-01s |                    |
 --------------------------------------------- 
```

Note: in this example ```f()``` is called from within ```g()``` so the percentages may add to over 100% because both functions were running at the same time (the runtime of ```f()``` was part of the runtime for ```g()```). The percentage represents total runtime of the function as a fraction of the total program runtime. 
