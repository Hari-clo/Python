def addi():
    ans=a+b
    print("Answer: ",ans)
a=int(input("enter first number: "))
b=int(input("enter second number: "))
addi()

#types of functions

#builtin function
aaa=(1,2,3,4)
print(len(aaa))


#user defined function
#void function
def greet():
    name=input("enter your name ")
    print("Good morning ",name)
print(greet())#None

#non-void function
def greet():
    name=input("enter your name ")
    return "Good morning "+name
print(greet())#None

#Parameterized function
def addii(c,d):#parameters(c,d)
    return c+d
anss=addii(4,5)#arguments(4,5)
print("answer",anss)

#types of arguments

def are(l=10,w=1):#default arguments
    return l*w
rec=are(5,3)#keyword arguments
print("Area of rectangle",rec)
