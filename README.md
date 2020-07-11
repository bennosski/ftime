# profile

A decorator to profile function performance. 
Simply add the ```@timed``` decorator to any function or class methods for which to measure runtime. 
Call timed.results() to print detailed timing information to the console including:
   - number of function calls
   - total runtime for each function
   - average runtime for each function
   - total runtime of the program
   
```ruby
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
```

output: 
```
 --------------------------------------------- 
|               Runtime Profile               |
|---------------------------------------------|
| name      |   %   | total time | time/call  |
|---------------------------------------------|
| g    (x1) | 75.0% | 3.009e-01s |            |
| f    (x2) | 50.0% | 2.008e-01s | 1.004e-01s |
|---------------------------------------------|
| program           | 4.012e-01s |            |
 --------------------------------------------- 
```
