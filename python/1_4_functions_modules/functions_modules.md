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
