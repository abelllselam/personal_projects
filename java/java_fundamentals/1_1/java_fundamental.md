**Java_Fundamental**

# Primitive Types

- Java has 8 built in primitive types. These are the most basic building blocks for storing values. Here's a quick overview.

  - byte

    - 8- bit signed (it means starts from -2 billion to 2 billion) integer
    - Range: -128 to 127
    - Use when you need a small range of numbers to save memory (rare in modern apps)

  - short
    - 16-bit signed integer
    - range -32768 to 32,767
  - int
    - 32-bit signed integer
    - Range: roughly -2 billion to 2 billion
    - The default choice for whole numbers in most code.
  - long
    - 64-bit signed integer
    - Range: roughly -9 quantillion to 9 quantillion
    - When you know values might exceed the int range(e.g, large counters)
  - float
    - 32 bit floating point (decimal) number
    - use for decimal values when you need less precision ot to save memory
    - Note: suffix literal with f (e.g, 3.14f)
  - double
    - 64-bit floating point(decimal) number
    - default choice for decimal values (more precision than float)
  - char
    - 16-bit unicode character
    - can store a single character like 'A', '7' or '?'
    - wrapped in single quotes(e.g char letter = 'A');
  - boolean
    - Represents truth values: true or false
    - Often used for conditions and flags

```java
public class PrimitivesExample {
    public static void main(String[] args) {
        byte      smallNumber    = 100;        // fits in –128 to 127
        short     mediumNumber   = 10_000;     // underscores help readability: 10000
        int       age            = 25;         // typical whole number
        long      bigNumber      = 9_000_000_000L; // note the 'L' suffix: tells Java this is a long
        float     price          = 19.99f;     // 'f' suffix indicates float literal
        double    preciseValue   = 3.1415926535;
        char      initial        = 'A';        // single character in single quotes
        boolean   isStudent      = true;       // true or false

        // Print them out
        System.out.println("byte: "      + smallNumber);
        System.out.println("short: "     + mediumNumber);
        System.out.println("int: "       + age);
        System.out.println("long: "      + bigNumber);
        System.out.println("float: "     + price);
        System.out.println("double: "    + preciseValue);
        System.out.println("char: "      + initial);
        System.out.println("boolean: "   + isStudent);
    }
}

```

- Numeric literals without suffix default to int (for whole numbers) or double (for decimals).
- Use L to mark a literal as long, and f to mark a literal as float.
- Underscores in numeric literals (e.g., 1_000_000) improve readability but don’t affect the value.

## Rules & Conventions

- Naming:

  - Must start with a letter, underscore \_, or dollar sign $ (though $ is rare in normal code).
  - Subsequent characters can be letters, digits, \_, or $.
  - Cannot use Java reserved words (e.g., int, class, void, etc.).
  - By convention, use camelCase for variable names: firstName, totalPrice, counter.

- Scope:

  - Variables declared inside a method (like main) are local to that method.
  - You’ll learn about other scopes (class-level fields, block scope) soon.

- E.g

```java
public class VariableExample {
    public static void main(String[] args) {
        // Declaration
        int    count;
        double temperature;

        // Initialization
        count       = 5;
        temperature = 36.6;

        // Combined
        int score = 100;

        // Re-assigning
        score = 120; // OK, as long as types match

        System.out.println("Count: "       + count);
        System.out.println("Temperature: "+ temperature);
        System.out.println("Score: "       + score);
    }
}

```

# Basic Operators

- Operators lets you perform computations, comparisons and combine or modify values we'll cover the most common ones:

## Arithmetic Operators

| Operator | Meaning                     | Example | Result                                                      |
| -------- | --------------------------- | ------- | ----------------------------------------------------------- |
| `+`      | Addition                    | `5 + 3` | `8`                                                         |
| `-`      | Subtraction                 | `5 - 3` | `2`                                                         |
| `*`      | Multiplication              | `5 * 3` | `15`                                                        |
| `/`      | Division (integer or float) | `5 / 2` | `2` (int division) <br> `5.0 / 2` = `2.5` (double division) |
| `%`      | Remainder (modulus)         | `5 % 2` | `1`                                                         |

- Integer division discards the fractional part: 5 / 2 yields 2, not 2.5.
- To force decimal division, make at least one operand a float or double: 5.0 / 2, or (double)5 / 2.

### Increment and decrement

- ++ adds 1
- -- subtracts 1

```java
int x = 5;
x++;           // x is now 6
++x;           // x is now 7

int y = 5;
y--;           // y is now 4
--y;           // y is now 3

```

- Difference between post-increment (x++) and pre-increment (++x):
  - int a = x++; → a gets the old value of x, then x increments.
  - int b = ++x; → x increments first, then b gets the new value.

## Relational (Comparison) Operators

- Compare two values and yield a boolean (true or false)

| Operator | Meaning          | Example            | Result |
| -------- | ---------------- | ------------------ | ------ |
| `==`     | Equals           | `5 == 3` → `false` |        |
| `!=`     | Not equals       | `5 != 3` → `true`  |        |
| `>`      | Greater than     | `5 > 3` → `true`   |        |
| `<`      | Less than        | `5 < 3` → `false`  |        |
| `>=`     | Greater or equal | `5 >= 5` → `true`  |        |
| `<=`     | Less or equal    | `3 <= 5` → `true`  |        |

- Code Example:

```java
int a = 10;
int b = 20;

boolean isEqual    = (a == b);  // false
boolean isNotEqual = (a != b);  // true
boolean greater    = (b > a);   // true
boolean less       = (a < b);   // true

```

## Logical Operators

- Combine boolean expressions:
  | Operator | Meaning | Example | Result |
  | -------- | ----------- | ---------------------- | ------------------------------ |
  | `&&` | Logical AND | `(a < b) && (b < c)` | true if both sides true |
  | `\|\|` | Logical OR | `(a < b) \|\| (b > c)` | true if at least one side true |
  | `!` | Logical NOT | `!(a == b)` | true if `a != b` |

- Code example:

```java
boolean cond1 = (5 > 3); // true
boolean cond2 = (2 > 4); // false

boolean andResult = cond1 && cond2; // false
boolean orResult = cond1 || cond2; // true
boolean notResult = !cond1; // false
```

## Assignment & Compound Assignment

- simple assignment: =

```java
int x =10;
```

- compound assignments: combine an operator with assignment:

  - += (add and assign)
  - -= (subtract and assign)
  - \*= (multiply and assign)
  - /= (divide and assign)
  - %= (modulus and assign)

  - Code example:

  ```java
  int x = 5;
  x += 3;   // equivalent to x = x + 3;  → x is now 8
  x *= 2;   // equivalent to x = x * 2;  → x is now 16
  x -= 4;   // x = x - 4;                → x is now 12
  x /= 3;   // x = x / 3;                → x is now 4

  ```
