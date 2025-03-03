from keyword import kwlist, softkwlist

def display_keywords() -> None:
    print("Keywords:")
    for i, kw in enumerate(kwlist, start=1):
        print(f"{i:2}: {kw}")

    print("Soft keywords:")
    for i, skw in enumerate(softkwlist, start=1):
        print(f'{i:2}: {skw}')


def main() -> None:
    display_keywords()

if __name__ == '__main__':
    main()

# 1: False Keyword 
has_money: bool = False
print(has_money)
print(int(False))

# 2: None keyword
from typing import Any
data: Any = None
print(data)

# 3: True keyword
has_money: bool = True
print(has_money)
print(int(True))

# 4: and keyword
a, b, c = 10, 20, 30

if c > b and c > a:
    print("Both conditions are true")


# 5: as keyword
import math as m 
m.cos(10)

# 6: assert keyword
limit :int = 10
n: int = 2

assert n < limit, "n is greater than limit"

# 7: async keyword
import asyncio

async def main() -> None:
    print("I am an async function")

if __name__ == '__main__':
    asyncio.run(main=main())

# 8: await keyword
import asyncio

async def say_hello():
    await asyncio.sleep(1)  # Simulating an async operation
    print("Hello, Async World!")

async def main():
    await say_hello()

asyncio.run(main())


# 9: break keyword
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2


# 10: class keyword
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)  # Output: Alice


# 11: continue keyword
for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0, 1, 3, 4


# 12: def keyword
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))


# 13: del keyword
numbers = [1, 2, 3, 4]
del numbers[2]
print(numbers)  # Output: [1, 2, 4]

# 14: elif keyword
x = 10
if x < 5:
    print("Small")
elif x == 10:
    print("Exactly 10")  # Output: Exactly 10
else:
    print("Large")


# 15: else keyword
if False:
    print("Won't print")
else:
    print("Else block executed")  # Output: Else block executed


# 16: except keyword
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")  # Output: Cannot divide by zero

# 17: finally keyword
try:
    print("Try block")
except:
    print("Except block")
finally:
    print("Finally block")  # Output: Finally block

# 18: for keyword
for i in range(3):
    print(i)  # Output: 0, 1, 2

# 19: from keyword
from math import sqrt
print(sqrt(16))  # Output: 4.0

# 20: global keyword
x = 10

def modify():
    global x
    x = 20

modify()
print(x)  # Output: 20

# 21: if keyword
x = 5
if x > 0:
    print("Positive")  # Output: Positive

# 22: import keyword
import math
print(math.pi)  # Output: 3.141592653589793

# 23: in keyword
nums = [1, 2, 3]
print(2 in nums)  # Output: True

# 24: is keyword
a = [1, 2, 3]
b = a
print(a is b)  # Output: True

# 25: lambda keyword
square = lambda x: x * x
print(square(4))  # Output: 16

# 26: nonlocal keyword
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)  # Output: 20

outer()

# 27: not keyword
x = False
print(not x)  # Output: True

# 28: or keyword
x = False
y = True
print(x or y)  # Output: True

# 29: pass keyword
def function():
    pass  # Does nothing

# 30: raise keyword
raise ValueError("An error occurred")

# 31: return keyword
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5

# 32: try keyword
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error!")  # Output: Error!

# 33: while keyword
x = 3
while x > 0:
    print(x)
    x -= 1  # Output: 3, 2, 1

# 34: with keyword
with open("test.txt", "w") as f:
    f.write("Hello, World!")

# 35: yield keyword
def count():
    for i in range(3):
        yield i

for num in count():
    print(num)  # Output: 0, 1, 2