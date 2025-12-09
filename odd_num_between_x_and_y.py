x=int(input("enter the starting number"))
y=int(input("enter the ending number"))

for i in range(x,y+1):
    if i%2==1:
        print(i,end=" ")
