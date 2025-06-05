#int,float,bool,complex
a=10
b=3.2
c=True
d=2+3j
print(a,type(a),b,type(b),c,type(c),d,type(d))


#type conversion
#implicit type conversion (without data loss)
a=10
print(float(a))

#explicit conversion  (with some loss of data)
b=10.5
print(int(a))

# input function
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print(x*y)