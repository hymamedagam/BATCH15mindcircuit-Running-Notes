#list methods
# append(), extend(), copy(), count(), sort(), remove(), pop(), clear(), insert(), index(),reverse()

rekha=[1,3,2,4,2,6,7,4,5,6]
rekha.append(9)
print("after append:", rekha)
rekha.extend([12,19,18])
print("after extend:", rekha)
print(rekha.count(6))
print(rekha.index(3))
rekha.insert(1,2)
print("After insert:", rekha)
v=rekha.copy()
print(v)
rekha.sort()
print("After sort:", rekha)
rekha.reverse()
print("After reverse:", rekha)
rekha.remove(7)
print("After remove:", rekha)
popped_element=rekha.pop(1)
print("popped element:", popped_element)
print("After pop:", rekha)
rekha.sort(reverse=True)
print(rekha)
rekha.sort(reverse=False)
print(rekha)
rekha.clear()
print(rekha)
