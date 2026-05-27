mark=[]
for i in range(5):
    score=int(input("enter your mark:"))
    mark.append(score)
print("mark",mark)
print("highest mark", max(mark))
print("lowest mark",min(mark))
average=sum(mark)/len(mark)
print(average)
for i in mark:
  if i>=40:
     print("passed")
  else:
    print("failed")
