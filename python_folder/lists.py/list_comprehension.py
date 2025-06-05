# print indices of a same number located at different positions
indhu=[1,3,2,5,6,3,2,0,1,2,7,8,2]
for i in range(len(indhu)):
    if indhu[i]==2:
        print(i)

# replace a number with another number wherever it is placed

neha=[1,5,21,32,67,19,87,12,5,32]
for j in range(len(neha)):
    if neha[j]==32:
        neha[j]=25
print(neha)

# list comprehension example-1

print(["EVEN" if i%2==0 else "ODD" for i in range(1,20)])

# print sqaure numbers
print([x**2 for x in range(1,10)])

# cube numbers
print([y**3 for y in range(1,10)])

# print only the first letters of the words

print([word[0] for word in ["apple","banana","orange","mango"]])

# create a list with only positive numbers

print([num for num in [-2,-10,0,1,4,-5,6,9] if num>0])

#how to remove multiple elements in the list
hema=[2,4,6,-2,98,34,56,82,21,45]
num_to_remove=[-2,34,21,45]
print([i for i in hema if i not in num_to_remove])

#how to remove same element placed in different positions
sravya=[2,4,6,3,7,9,2,0,1,4,2,2]
nums_to_remove=[2]
print([j for j in sravya if j not in nums_to_remove])