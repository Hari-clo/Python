l=[1,2,3,4,5]
print(l[2])#indexing it assigns value for each value in a list starting with zero

#methods used in list

print(len(l))#length of the list

l.append(6)#adding values at the end of the list
print(l)#[1,2,3,4,5,6]

l.insert(0,0)#inserting values anywhere by using index value
print(l)#[0,1,2,3,4,5,6]

l.sort()#ascending order
print(l)

l.sort(reverse=True)#decending order
print(l)

#maximum and minimum
print("Maximum value in the list is ",max(l),"Minimum value in the list is ",min(l))

#sum
print("suum of values: ",sum(l))

#extend
l.extend([6,7,8,9,10])
print(l)

#count
print("count of 6: ",l.count(6))

#find the element position
print("the 7 is at",l.index(7))

#delete a value using index
l.pop(0)#removes by using index value
print(l)

#remove a element
l.remove(10)#remove by mentioning value
print(l)

