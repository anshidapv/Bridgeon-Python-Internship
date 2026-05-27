for i in range(1,51):
    if i%4==0 and i%7==0:
       print("fizzbuzz")
    elif i%4==0:
       print("fizz")
    elif i%7==0:
       print("buzz")
    else:
       print(i)
