my_set = {1,3,5,7,2,4,6,9}
my_set.add(10)
print("After add: ", my_set)
my_set.remove(9)
print("After remove: ", my_set)
popped_element = my_set.pop()
print("Popped element: ", popped_element)
my_set.clear()
print("After clear: ", my_set)
set_a = {1,2,3}
set_b = {3,4,5}
union_set = set_a.union(set_b)
print("Union set: ", union_set)
intersection_set = set_a.intersection(set_b)
print("Intersection set: ", intersection_set)
difference = set_a.difference(set_b)
print("difference set: ", difference)
