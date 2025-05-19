## Time complexity:

- What It Measures
  - Time complexity tells us how the number of steps an algorithm takes grows as the input size n increases.
  - A “step” is a basic operation like a comparison (if), an assignment, or an arithmetic operation.

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
  - Analogy: For each door, you walk the entire hallway again - so you do "walk n doors" n times.
  - Steps: about n\*n checks.
  - Example in Code:

```js
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    // two nested loops → n² steps
  }
}
```

- O(log n): Logarithmic Time
  - Analogy: You stand in the middle of the hallway, decide if the person you want is on the left or right, then move to the middle of the half - and repeat.
  - Steps: Each move cuts the hallway in half, so you only need about log2(n) moves.
  - Example in code (Binary Search):

```js
let low = 0,
  high = n - 1;
while (low <= high) {
  let mid = Math.floor((low + high) / 2);
  if (arr[mid] === target) return mid;
  else if (arr[mid] < target) low = mid + 1;
  else high = mid - 1;
}
```

#### Why use Big-O?

- Quick comparison: "This one is O(n), that one is O(n^2)."
- Scalability warning: O(n) might be OK when n=100, but O(n^2) may be too slow when n=1000

# Log explained:

- Logarithm (log) answers the question:
  - To get down to 1 by repeatedly dividing by a certain number, how many divisions do i need?
  - Usually in algorithm, we use log base 2, because we're cutting things in half each step (like binary search).

#### Simple Example

- Think of Dividing Candies in Half:
  You have 8 candies.

  - Give away half → 4 left
  - Give away half → 2 left
  - Give away half → 1 left
  - You did 3 steps ⇒ log₂(8) = 3

- General Rule:
  If you start with n, dividing by 2 each time, you need about log₂(n) steps to get down to 1.

#### Mini-Chunk: What “O” Really Means

- O(f(n)) is just a way to say:
- “The number of steps (time) my algorithm takes grows on the order of f(n) for large n.”
- It doesn’t literally stand for “time,” but we use it almost always to describe time complexity (how steps grow) or sometimes space complexity (how extra memory grows).

##### Key takeaway:

      - When you see O(n), read it as “steps grow linearly with n.”
      - O(log n) means “steps grow logarithmically with n,” and so on.

# Big-Ω (Omega) (Lower Bound)

- Big-Ω, written Ω(f(n)), gives a best-case guarantee: the algorithm takes at least c·f(n) steps for sufficiently large n.
- Think of it as the minimum work you must do.
  - Analogy
    If you always have to check at least half the doors in a hallway before you find someone, that’s Ω(n) work—even if sometimes you get lucky and finish earlier.
  - Formal Definition
    An algorithm is Ω(f(n)) if there exist constants c > 0 and n₀ such that for all n ≥ n₀:
    ```scss
      steps(n) ≥ c · f(n)
    ```
    - Simple Examples:
      - Linear scan (for i in 0…n):
        - Always looks at every element → Ω(n).
      - Binary search:
        - Best case you find the target in the first comparison → Ω(1).
      - Bubble sort:
        - Best case (already sorted) still does one full pass of n–1 comparisons → Ω(n).
  - Why It’s Useful
    - Tells you the least amount of work required, so you know if an algorithm can ever be faster than that bound.

# Big-Θ (Theta) (Tight Bound)

- What It Measures
  - Big-Θ, written Θ(f(n)), means the algorithm’s running time grows both no faster than c₂·f(n) and no slower than c₁·f(n) for large n.
  - It gives a tight bound—an exact growth rate up to constant factors.
- Formal Definition
  - An algorithm is Θ(f(n)) if there exist constants c₁, c₂ > 0 and n₀ such that for all n ≥ n₀:
  ```scss
     c₁·f(n) ≤ steps(n) ≤ c₂·f(n)
  ```
  - Example: The simple loop that scans an array:
  ```js
  for (let i = 0; i < n; i++) {
    // constant work each time
  }
  ```
  - Worst case: ≈ n steps → O(n)
  - Best case: ≈ n steps → Ω(n)
  - Tight: Θ(n), since it’s both O(n) and Ω(n).
  - Why It’s Useful
    When you know Θ(f(n)), you know the algorithm’s running time will be “on the order of f(n)” in typical scenarios—not just worst or best case.
