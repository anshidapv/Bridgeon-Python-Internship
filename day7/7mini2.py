def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"function: {func.__name__}")
        print(f"arguments: {args}")
        return func(*args, **kwargs)
    return wrapper
@log_call
def add(a,b):
    return a+b
@log_call
def greet(name):
    print(f"hello {name}")
@log_call
def multiply(x,y):
    return x*y
print(add(10,20))
greet("alice")
print(multiply(5,6))
