#Iterative statements
#for loop
for i in range(6):
    print(f"to print value {i} times")#0to5
print("\n")
for i in range(1,6):#(start,stop)
    print(f"to print value {i} times")#1 to 5
print("\n")
for i in range(1,10,2):#(start,stop,step)
    print(f"to print value {i} times")#it prints odd numbers 1,3,5,7 since it moves 2 step

#while loop
a=10
while a>0:
    print("hi")
    a=a-1

#nested loop
for i in range(10):
    for j in range(2):
        print(i,j)
i=1
while i<3:
    j=i+1
    while(j<3):
        print(i,j)
        j+=1
    i+=1
