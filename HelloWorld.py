# coding=utf-8
print("Hello World")
x = 1
if x == 1:
    print("x is 1")
myint = 7
myfloat = 7.0
myfloat2 = float(7)
mystring = 'hello'
mystring2 = "world"

one = 1
two = 2
three = one + two
helloworld = mystring + " " + mystring2
a, b = 3, 4

mylist = [myfloat, myfloat2, myint]
print(mylist[0])
print(mylist[1])
print(mylist[2])
for x in mylist:
    print(x)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

lotsofhellos = "hello" * 10
print(lotsofhellos)

name = "Lichee"
# print ("Hello,%s!") %(name)
print(len(name))
print(name.index("e"))
print(name.upper())
print(name.lower())
age = 23
print(x == 23)
print(x == 2)
print(x < 25)
# print("%s is %d years old.") %(name,age)
if name == "Lichee" and age == 23:
    print("Your name is Lichee,and you are also 23 years old.")
if name == "Lichee" or name == "Wong":
    print("Your name is either Lichee or Wong.")
if name in ["Lichee", "Wong"]:
    print("Your name is either Lichee or Wong.")

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
for x in range(5):
    print(x)
for x in range(3, 6):
    print(x)
for x in range(3, 8, 2):
    print(x)

count = 0
while count < 5:
    print(count)
    count += 1
# print ("A list:%s") %mylist
# %s-String %d-Integers %f-Floating point number %x%X- Integers in hex representation
a = 0
while True:
    print(a)
    a += 1
    if a >= 5:
        break
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)


def my_function():
    print("Hello From My Function!")


my_function()
