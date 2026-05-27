marks=[10,20,30,40,50,60,70,80,90,100]
print("highest:",max(marks))
print("lowest:",min(marks))
average=sum(marks)/len(marks)
print("average:",average)
unique=list(set(marks))
print(unique)
marks2=[]
for m in marks:
    if m>average:
        marks2.append(m)
        print("above average mark:",marks2)