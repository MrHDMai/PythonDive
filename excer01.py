print("Hello world")
print(45)
print(5.5)
#this is a comment

# this is a multiple line comment
# we will declare it as so

# mathematical functions
x = 7
y = 1
sum = x + y
dif = x - y
quotient = x/y
mod = x%y
print("Sum is: ",sum, "Different is: ", dif, "qoutient is: ", quotient, "modules is: ", mod) 
# print(sum)

# #input output
# num = int(input("Enter a num "))
# print("Computing odd or even")
# if num%2 == 0: 
#     print("Num is even")
# else:
#     print("Num is not even")

# age = int(input("Please enter your age "))
# name = input("Please enter your name ")
# print("Hi", name, "you are", age, ". It is nice to meet you.")

#data type: 
#string declare as str
n = "This is a string"
type(n)
print(type(n))

i = 1j
print(type(1j))

d = 1.3
print(type(d))

r = range(8)
print(r)
print(type(r))

m = {'a' : '1', 'b' : '2', 'c': '3'}
print(n)
print(type(m))

#unordered
#mutable - can change
#May contain duplicates
#can be indexed
s = {'x','y','z'}
print(s)
print(type(s))

#ordered
#mutable - immutable/fixed
#May contain duplicates
#can be indexed
l = ['a','b','c','d']
print(l)
print(type(l))

#ordered
#can add or remove
#cannot include duplicate
#cannot be indexed
t = ('k','l','m')
print(t)
print(type(t))

#unorder
#immutable
#cannot contain duplicates
#support set operation but not indexing
f = frozenset({'g','h','i'})
print(f)
print(type(f))

#boolean
bol = True
print(type(bol))

#byte
z = b"100"
print(z)
print(type(z))

ba = bytearray(8)
print(ba);
print(type(ba))

mb = memoryview(bytes(100))
print(mb)
print(type(mb))