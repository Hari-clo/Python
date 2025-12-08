#Conditional Statement
#IF statement
salary=100000
if salary>50000:
    print("High salary")

#if else statement
salary=100000
if salary>=100000:
    print("High salary")
else:
    print("Low salary")

#with ternary operator
high="high salary" if salary>=100000 else "low salary"

#elseif statement(elif)
a=int(input("enter a number : "))
if a>0:
    print("it is positive")
elif a==0:
    print("it is zero")
else:
    print("it is negative")

#nested if statement
age=int(input("enter your age : "))
if age>18:
    vote=input("do you have a voter id")
    if vote=="yes":
        print("fit to vote")
    else:
        print("get a voter id to vote")
else:
    print("not fit to vote")
