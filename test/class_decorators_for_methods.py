# This part works as expected.

print('---------------')
print('Test1\n')

def timed(f):
    def wrap(*args):
        print('inside wrapper for {}'.format(f.__name__))
        print('len of args: {}'.format(len(args)))
        return f(*args)
    return wrap

class obj:
    @timed
    def method(self, x):
        print(x)

x = obj()
x.method(4)

# This part sadly doesn't work. I've just rewritten my function decorator as a class instead.

print('---------------')
print('Test2\n')

class timed:
    def __init__(self, f):
        self.f = f
        
    def __call__(self, *args, **kwargs):
        print('inside wrapper for {}'.format(self.f.__name__))
        print('len of args: {}'.format(len(args)))
        return self.f(*args, **kwargs)
    
class obj:
    @timed
    def method(self, x):
        print(x)
        
x = obj()
try:
    x.method(4)
except Exception as e:
    print('\nClass decorator did not work!')
    print(e)
    print('')

    
# Some workarounds I've found so far but don't like that much:
#
# - pass self or the class explicitly as:
#       x.method(x, 4) or x.method(obj, 4)
#
# - add @classmethod above @timed

print('---------------')
print('Workaround\n')

# Best workaround

class timed:
    def __init__(self, f):
        self.f = f
        
    def __get__(self, instance, owner):
        self.obj = instance
        return self.__call__

    def __call__(self, *args, **kwargs):
        print('inside wrapper for {}'.format(self.f.__name__))
        print('len of args: {}'.format(len(args)))
        if hasattr(self, 'obj'):
            return self.f(self.obj, *args, **kwargs)
        else:
            return self.f(*args, **kwargs)
                
class obj:
    @timed
    def method(self, x):
        print(x)
        
x = obj()
x.method(4)

# test it on a regular function

@timed
def g(x):
    print(x)

g(5)





