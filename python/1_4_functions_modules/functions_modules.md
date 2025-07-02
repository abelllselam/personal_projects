**Defining functions**

- What is a function? - It is a block of code that you can call (invoke) whenever you need it. It may take inputs (parameters), perform work and optionally return a result.
- Example of a python function:

```py
def function_name(param1, param2, …):
    """
    Optional docstring:
    Brief description of what the function does,
    its parameters, and its return value.
    """
    # 1. Compute something using parameters
    result = param1 + param2
    # 2. Return the result to the caller
    return result

```

- def: keyword to start a function definition.
- function_name: follows variable naming rules (letters, digits, underscores; can’t start with a digit).
- Parameters: names inside the parentheses—placeholders for inputs.
- Colon and indentation: mark the beginning of the function body.
- return: sends a value back. If omitted, the function returns None.

# Modules & Packages:

- A module is any Python file(.py) that contains definitions, functions, classes and variables or runnable code.
- In the other hand a package is a folder that contains one or more modules, plus a special (**init**.py) to signal Python that this directory should be treated as a package.
- Using packages and modules helps you organize code and reuse functionality and avoid naming collisions.

## Creating and importing a module:

- define a module
  1. Make a file called math_util.py
  2. Inside math_utils.py write some functions:

```py
# math_utils.py

def square(n):
    """Return n multiplied by itself."""
    return n * n

def cube(n):
    """Return n to the third power."""
    return n * n * n

PI = 3.14159  # you can also store constants or variables here

```

- In another file, say main.py, you can bring in that module:

```py
# main.py

import math_utils                # import the module namespace

print(math_utils.square(4))      # → 16
print(math_utils.cube(2))        # → 8
print(math_utils.PI)             # → 3.14159

```

- import math_util loads the entire module under the name math_util
- To call a function or access a variable, prefix it with math_util.

## Selective Imports:

- Instead of importing the whole module, you can import only what you need:

```py
# main_partial.py

from math_utils import square, PI  # import only these names directly

print(square(5))  # → 25
print(PI)         # → 3.14159

# Note: `cube` is NOT imported, so `cube(2)` would cause NameError here.
```

## Aliasing

- You can also rename on import for convenience or clarity:

```py
import math_utils as m

print(m.square(3))  # → 9

from math_utils import cube as third_power

print(third_power(4))  # → 64

```

- import math_utils as m means you refer to the module as m.
- from math_utils import cube as third_power lets you call third_power(…) instead of cube(…).

# Packages: Grouping Multiple Modules

- When you project grows, you will have several related modules. You can group then into a package (a directory).
- Example of Package Structure:

```py
project/
├── analytics/         ← this is a package directory
│   ├── __init__.py    ← makes Python treat this directory as a package
│   ├── stats.py       ← module 1
│   └── plots.py       ← module 2
└── main.py

```

- analytics/ is the package name.
- **init**.py: can be empty or contain package-level initialization (like **all** or helper imports). Its presence tells Python this folder is a package.
- stats.py and plots.py are separate modules inside the package.

## Writing a module inside a Package:

- analytics/stats.py:

```py
# analytics/stats.py

def mean(numbers):
    """Return the arithmetic mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Return the median of a list of numbers."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

```

- analytics/plots.py:

```py
# analytics/plots.py

def bar_chart(data):
    """
    Dummy function to simulate drawing a bar chart.
    In a real project, you might use matplotlib here.
    """
    print("Drawing bar chart for:", data)

def line_plot(data):
    """Simulate drawing a line plot."""
    print("Drawing line plot for:", data)

```

- analytics/**init**.py: You can leave it empty, or use it to expose certain names when someone does from analytics import \*:

```py
# analytics/__init__.py

__all__ = ["stats", "plots"]
# __all__ defines what import * will import. Without __all__, import * brings in all modules but not their contents.
```

## Importing from a package:

- inside main.py

```py
# main.py

# Import the stats module from the analytics package
from analytics import stats

data = [10, 20, 30, 40]

print(stats.mean(data))      # → 25.0
print(stats.median(data))    # → (20 + 30)/2 = 25.0

# Import specific functions directly
from analytics.plots import bar_chart

bar_chart(data)              # → Drawing bar chart for: [10, 20, 30, 40]

```

- from analytics import stats: stats now refers to the analytics/stats.py module.
- from analytics.plots import bar_chart: brings bar_chart into the local namespace.
- You can also import the entire package:

```py
import analytics

# Access modules via the package namespace
print(analytics.stats.mean(data))
analytics.plots.line_plot(data)

```

- import analytics: does not automatically import stats or plots into the top-level namespace—you must refer to analytics.stats or analytics.plots.

### Relative imports within a Package:

- Inside a module in the same package, you can import another module using a relative path:

```py
# analytics/plots.py

from .stats import mean   # the single dot (.) means “same directory/package”

def describe_data(numbers):
    avg = mean(numbers)
    print(f"The average is {avg}")

```

- . refers to the current package directory (analytics/).
- .. refers to the parent package (if nested deeper).
- This is useful if you move the entire package—imports remain consistent.

# Key Points & Best Practices

1. Avoid Circular Imports

   - If module_a imports from module_b and module_b also imports from module_a, Python will raise errors.
   - To fix, refactor so that shared functionality lives in a third module both import, or use local (in-function) imports to break the cycle.

2. Use **all** Sparingly

   - Defining **all** in a module controls what from module import \* brings in.
   - It’s generally better to import explicitly rather than rely on import \*.

3. Keep Modules Focused

   - Aim for each module to handle a single responsibility or related set of functions/classes.
   - This makes maintenance and testing easier.

4. Name Files Carefully

   - Avoid using names that clash with standard library modules (e.g., don’t name your file json.py if you plan to use Python’s json library).

5. Directory Structure Matters
   - Organize packages by feature or layer (e.g., models/, views/, controllers/ in a web app).
   - Keep an **init**.py (even if empty) in every package directory you want Python to recognize.
