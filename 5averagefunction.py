def average(*marks):
    if len(marks)==0:
        print("no marks entered")
    else:
        avg=sum(marks)/len(marks)
        print("average=", avg)
average(10,20,30,40,50)
average()