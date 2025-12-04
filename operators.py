#Arithematic Operators
a=12
b=2
print(a+b) #14 addition
print(a-b)#10 subraction
print(a/b)#6.0 division (decimal)
print(a//b)#6 division (whole number)
print(a%b)#0 remainder
print(a**b)#144 square

#Operator Precedence Python uses BODMAS rule
print(20-12/5+2)#19.6

#if same operator it goes from right to left
print(2**3**(2%10))#512

#Membership Operators
c="One Piece"
print('i' in c)#True
print('o' in c)#False since O is in caps
print('z' not in c)#True

#Relational Operators
n1=5
n2=3
n3=5
print(n1 > n2)#True
print(n1 > n3)#False
print(n1 < n2)#False
print(n1 >= n2)#True
print(n1 <= n2)#False
print(n1 != n2)#True
print(n1 == n2)#False

#Assignment Operators
num=2
num+=2
print(num)#4 increment
num1=2
num1-=2
print(num1)#0 decrement
num2=2
num2*=2
print(num2)#4 2*2
num3=2
num3/=2
print(num3)#1.0 2/2

#Logical Operators (AND,OR,NOT)

#NOT gives the opppsite of the result
print(not(5>2))#False
print(not 0)#True since 0 is always false and in string empty string is flase

#AND ,when only both value is true the result will be true
print((5==5) and (2==2))#True
print(False and True)#False

#OR ,when any one value or both values are true the result will be true
print((5==5) or (2==1))#True
print((5==4) and (1==2))#False

#bitwise operator & | ~

#AND &
a = 12  # In binary: 1100
b = 5   # In binary: 0101
result = a & b  # Result in binary: 0100 (which is 4 in decimal)
print(result)  # Output: 4

#OR |
a = 12  # In binary: 1100
b = 5   # In binary: 0101
result = a | b  # Result in binary: 1101 (which is 13 in decimal)
print(result)  # Output: 13

#NOT ~
a = 12  # In binary: 0000 1100
result = ~a  # Result in binary: 1111 0011 (which is -13 in decimal due to two's complement)
print(result)  # Output: -13

#Identity Operator (it compares the memory location)
n=5
nu=4
print(n is nu)#False
