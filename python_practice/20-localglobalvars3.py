#Global variables

x = 10
y = 20
z =5

def add():
    x = 5  #local variables
    y = 4
    print(f"sum of local variables x=5, y=4 & global z=5 is: {x+y+z}") #local

def sub():
    global x
    x = 35
    y = 20
    print(f"subtraction of local variables x=35 & y=20 is: {x-y}") #local
add()
sub()
print(f"printing modified global variable -x {x}")
print(f"printing global variable -y {y}")


#Note: if we keep global x inside a function, then the global x can display the value of inside function x value.