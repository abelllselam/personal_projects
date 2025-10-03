**1.2 Variables & Data Types - deep dive**

- variable is a name that refers to a value in memory.
- In python we dont assign a type python figures it out at runtime (dynamic typing).

```py
x = 10           # name x refers to integer 10
name = "Abel"    # name refers to a string

```

- Naming rules & conventions
  - Must start with a letter (a–z, A–Z) or underscore \_.
  - Can contain letters, digits, and underscores: my_var2.
  - Case-sensitive: age ≠ Age.
  - Use snake_case for variables: user_name, total_amount.
  - Avoid names of built-in types/functions (list, str, id, etc.).
  - Constants (by convention): use ALL_CAPS for values you intend not to change:PI = 3.14159

\***\*Core built-in types your'll use immediately\*\***

1. int - integer - whole numbers, positive/negative, no decimal: a= 42 and b = -7
2. float - floating point numbers - numbers with decimal point: pi = 3.14159
3. str - string (text) - text enclosed in single or double quotes or triple quotes for multiple lines:

```py
s1 = "Hello"
s2 = 'world'
s3 = """multi
line"""

```

    - Strings are sequences (iterable) - you can index and slice them like lists.

4. bool - booleans - Logical values True or False (capitalized!): is_ready = True or has_items = False
5. None - the null-like value - used to represent "no value"/"unknown" - result = None

**Check a value's type**

- Use type() to inspect the runtine type:

```py
>>> x = 5
>>> type(x)
<class 'int'>

>>> y = "hi"
>>> type(y)
<class 'str'>

```

**Dynamic typing & reassignment**

- You can reassign a variable to a different type: This is allowed but be mindful - changing types unexpectedly can create bugs.

```py
x = 10        # int
x = "ten"     # now str
```

**Multiple assignment & swapping**

- Assign several variables at once

```py
x, y, z = 1, 2, 3

```

- Swap two variables without a temp:

```py
a, b = 5, 10
a, b = b, a   # a becomes 10, b becomes 5

```

**Converting between types (casting)**

- common conversions

```py
int("42")      # -> 42
float("3.14")  # -> 3.14
str(100)       # -> "100"
bool(0)        # -> False
bool("")       # -> False
```

- Be careful converting invalid strings raises ValueError

```py
int("abc")   # ValueError

```
