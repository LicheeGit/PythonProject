# _author_= Lichee
import re

m = re.match('foo', "foo.")
if m is not None:
    print(m.group())
print(m)

m = re.match('foo', "bar")
if m is not None:
    print(m.group())
print(m)

m = re.match('foo', 'food on the table')
print(m.group())

print(re.match('food', 'food on the table').group())
