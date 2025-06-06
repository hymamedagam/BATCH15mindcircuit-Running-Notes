my_string = "Hello, welcome to AWS Devops world"
print("Length of the string: ", len(my_string))
print("Upper case: ", my_string.upper())
print("Lower case: ", my_string.lower())
print("Title case: ", my_string.title())
print("My string starts with: ", my_string.startswith("Hello"))
print("My string ends with: ", my_string.endswith("world"))
substring = "welcome"
print(f"count of welcome: ", {my_string.count(substring)})
print("Index of world: ", my_string.find("world"))
print("split my string: ", my_string.split())
new_string = my_string.replace("AWS", "Cloud")
print("original string: ", my_string)
print("Modifies string: ", new_string)
alphanumericstring = "Python123"
print("is alphanumeric: ", alphanumericstring.isalnum())
