#pattern printing
"""
0
0 1
0 1 2
0 1 2 3
"""
n=int(input("enter number of lines"))
for  i in range(0,n+1):
    for j in range(i+1):
        print(j,end=" ")
    print()
