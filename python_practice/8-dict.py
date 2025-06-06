my_dict = {"name" : "Hyma", "phone" : "9876543210", "address" : "pasupugallu"}
print(type(my_dict))
keys = my_dict.keys()
print("list of keys: ", list(keys))
values = my_dict.values()
print("list of values: ", list(values))
items = my_dict.items()
print("list of items: ", list(items))
name = my_dict["name"]
print("name: ", name)
phone = my_dict.get("phone")
print("phone: ", phone)
popped_value = my_dict.pop("phone")
print("popped_value: ", popped_value)
print("After pop: ", my_dict)
salary = my_dict.get("salary", "Not Avaialble")
print("Salary: ", salary)
my_dict["occupation"] = "Engineer"
print("After adding: ", my_dict)
my_dict.clear()
print("After clear: ", my_dict)
new_dict = {'a' : 1, 'b' : 2}
copied_dict = new_dict.copy()
print("copied dict: ", copied_dict)
