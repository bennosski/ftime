# profile

A decorator to profile function performance. 
Simply add the ```@timed``` decorator to any function or class methods for which to measure runtime. 
Upon exit of your program, detailed timing information is neatly printed to the console including:
   - number of function calls
   - total runtime for each function
   - average runtime for each function
   - total runtime of the program
   
```ruby
from profile import timed

@timed
def f():
    print('hi')

@timed
def g():
    print('there')

f()
f()
g()
```

output: 
```
 ---------------------------------------------
|               Runtime Profile               |
|---------------------------------------------|
| name      |   %   | total time | time/call  |
|---------------------------------------------|
| f    (x2) | 29.6% | 1.402e-04s | 7.010e-05s |
| g    (x1) | 06.3% | 2.980e-05s |            |
|---------------------------------------------|
| program           | 4.742e-04s |            |
 ---------------------------------------------
```
