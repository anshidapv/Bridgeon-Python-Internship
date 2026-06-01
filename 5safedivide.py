def divide(a,b):
    try:
        result=a/b 
        print("result=", result)
    except ZeroDivisionError:
        print("cannot divided by zero")
divide(10,2)
divide(10,0)