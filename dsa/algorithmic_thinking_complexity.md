**Algorithm thinking & Complexity**

# What is Complexity:

- Complexity measures how an algorithm work grows as the input size (n) grows.
- Two main resources: Time (how many steps) and space (how much extra memory).
- You can think of time, like how many moves it will take you to finish a puzzle; space as how many extra pieces or bins you need while you work.
- The time complexity tells us how the number of steps an algorithm takes grows as the input size n increases. A step is a basic operation like a comparison (if) an assignment or an arithmetic operation.
- The reason we count steps is that even though computers are fast, if your steps grow too quickly even billions of operations per-second wont save you when n is large.
- counting steps give a machine-independent way to compare how efficient different algorithms are.

## Time complexity:

- What It Measures
  - Time complexity tells us how the number of steps an algorithm takes grows as the input size n increases.
  - A “step” is a basic operation like a comparison (if), an assignment, or an arithmetic operation.

## Space complexity:

# What is Big-O

- Think you have a hallway of numbered doors 1...n, and you need to check each door to see if someone's inside, time complexity asks - if the hallway doubles in length, how many more doors do i check?
- Big-O gives a quick way to say "at most this many checks" when n gets large.

- Some common classes (notations)

| Notation       | Growth Rate  | What It Means                                                  | Example                                  |
| -------------- | ------------ | -------------------------------------------------------------- | ---------------------------------------- |
| **O(1)**       | Constant     | Time does **not** grow with n; same cost always.               | Look up an element by index in an array. |
| **O(log n)**   | Logarithmic  | Grows **very slowly**; doubling n adds only one extra step.    | Binary search in a sorted list.          |
| **O(n)**       | Linear       | Grows **proportionally** to n.                                 | Scanning every element in an array.      |
| **O(n log n)** | Linearithmic | Slightly more than linear; common in fast sorting.             | Merge sort or heapsort.                  |
| **O(n²)**      | Quadratic    | Grows with the **square** of n.                                | Two nested loops over the same array.    |
| **O(2ⁿ)**      | Exponential  | Doubles work for each additional element—**very** fast growth. | Checking all subsets of a set.           |

#### The table explained:

- O(1) - Constant Time
  - Analogy:You have one special door (say door#1) and you always check only that door - no matter how many doors there are.
  - Steps:Always one check.
  - Example in Code:

```js
return arr[0]; // Always look at the very first element
```

- O(n)- Linear Time
  - Analogy: You walk down the hallway and knock on every door until the end.
  - steps: n check for n doors.
  - Example in code:

```js
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]); // one check per element
}
```

- O(n^2) - Quadratic Time:
  - Analogy:
  - Steps:
  - Example in Code:
