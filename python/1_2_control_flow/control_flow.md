**Control Flow**

# Logical Operators

- Combine multiple comparisons:
  - and: true if both operands are true
  - or: true if either operand is true
  - not: negates a Boolean

# Truthy & Falsy Values

- In Python, non-Boolean types can act as conditions:
  - Falsy values (act like False):
    - 0, 0.0, "" (empty string), [] (empty list), {} (empty dict), None
  - Truthy: almost everything else

```py
items = []
if items:
    print("We have items")
else:
    print("List is empty")  # this branch runs

```

# if Statements

```py
if condition:
    # code when condition is True
elif other_condition:
    # code when other_condition is True
else:
    # code when all conditions are False

```

# for loop:

- this iterates over any sequence(list,string, range, etc)
- Example of for loop:

```py
for <variable> in <sequence>:
    # block: runs once per element in <sequence>

```

## Common Iterables:

- List:

```py
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)~
```

- String (Iterates over characters)

```py
for ch in "Hello":
    print(ch)
```

- range() (generates a sequence of numbers)

```py
# for range(start, stop, step)
for i in range(5):      # i goes 0,1,2,3,4
    print(i)

```

# Loop Control: break and continue

- break: Immediately exit the loop.
- Continue: Skip the rest of the current iteration and move to the next.

```py
for num in range(1, 10):
    if num == 5:
        break            # stops loop when num is 5
    print(num)

for num in range(1, 6):
    if num % 2 == 0:
        continue         # skip even numbers
    print(num)           # prints only odd numbers

```

# Accessing Index and Value

- To get both the index and value, use enumerate():

```py
colors = ["red", "green", "blue"]
for idx, color in enumerate(colors, start=1):
    print(idx, color)
# start=1 makes the index begin at 1 instead of 0 (default).
```

# Iterate over dictionaries:

When looping a dictionary, you can access keys, values, or both:

```py
user = {"name": "Alice", "age": 30}

# Keys only
for key in user:
    print(key)

# Values only
for value in user.values():
    print(value)

# Key-Value pairs
for key, value in user.items():
    print(key, "→", value)

```

# While loops

- A while loop repeatedly executes a block of code as long as a given condition remains true.
- Syntax & Structure

```py
while <condition>:
    # block: runs as long as <condition> is True
else:
    # optional: runs once when the loop exits normally (condition becomes False)

```

- The else block is optional and runs only if the loop ends without encountering a break.
- Indentation defines the loop’s body.
- Basic Example:

```py
count = 1
while count <= 5:
    print(f"Count is {count}")
    count += 1
else:
    print("Loop has completed normally.")

//output
Count is 1
Count is 2
Count is 3
Count is 4
Count is 5
Loop has completed normally.

```

# Using break & continue:

- break: Immediately exit the while loop(skips the else block).
- continue: Skip the rest of the current iteration and re-check the condition.

```py
n = 0
while True:
    n += 1
    if n % 2 == 0:
        continue      # skip printing even numbers
    if n > 7:
        break         # exit loop when n exceeds 7
    print(n)
else:
    # This else will NOT run because of the break above
    print("Finished without break")

//output
1
3
5
7

```

# Avoiding Infinite loops

- A while True: loop without a break or changing condition will never end. Always ensure:
  - The loop's condition will eventually become False, or
  - There's a reachable break statement.

```py
# Bad: infinite loop
while True:
    print("This never ends!")

# Good: changes the condition
x = 3
while x > 0:
    print(x)
    x -= 1

```
