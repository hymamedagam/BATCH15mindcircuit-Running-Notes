#slicing: get some part of elements in the list from where to where u want.
# [start:stop:skip]

rani=[20,3,1,5,9,4,2,6,7,12,32]
print(rani[0:5]) # displays elements from index 0 to index 4 
print(rani[0:11:2]) # displays elements from index 0 to index 10 by skipping one value
print(rani[:]) # displays the list as it is
print(rani[::]) # displays the list as it is
print(rani[1:]) #displays elements from index 1 to last.
print(rani[4:]) #displays elements from index 4 to last.
print(rani[:8]) #displays elements from start to index 7.
print(rani[2:2]) # same index displays empty list
print(rani[-7:-1]) # displays elements from index -7 to index -2
print(rani[-1:-6]) # we can't give higher number first, it will display empty list
print(rani[::-1]) # display list in reverse order
print(rani[::-2]) # display list in reverse order by skipping one value
