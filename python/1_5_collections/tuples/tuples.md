## **What is a tuples**

- It is an ordered immutable sequence of elements
- It is like a list but ones created, it contents cannot be changed.
  Defined with parentheses(.....) or simply commas
- Example: Syntax & Creation:

```js
# With parentheses
empty_tuple = ()
point = (3, 5)

# Without parentheses (comma makes the tuple)
colors = "red", "green", "blue"

# Single-element tuple needs a trailing comma!
single = (42,)
also_single = 42,

```

# Accessing Elements

- Indexing (0-based) same as lists:

```js
point = (3, 5)
x = point[0]    # 3
y = point[1]    # 5
```

- Slicing returns a new tuple:

```py
nums = (1, 2, 3, 4)
sub = nums[1:3]   # (2, 3)

```

- Tuple Unpacking
- Assign elements directly to variables:
