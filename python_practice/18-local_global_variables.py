#Global variables

x = 10
y = 15

def add():
    x = 5  #local variables
    y = 6
    print(f"local variable x: {x}")
    print(f"local variable y: {y}")
    print(f"Sum of x and y is {x + y}") #local
add()
print(f"Sum of x and y is {x + y}") # global
print(f"global variable x: {x}")
print(f"global variable y: {y}")