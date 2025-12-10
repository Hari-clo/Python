num=[1,2,3,4,5,6]

squ=[i**2 for i in num]
print(squ)

#square the numbers which are even
squ_eve=[i**2 for i in num if i%2 == 0]
print(squ_eve)
