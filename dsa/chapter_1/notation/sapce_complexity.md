# Space Complexity:

- What It Measures

  - Space complexity tracks how much extra memory an algorithm uses as n grows.
  - We ignore the space for the input itself and count only additional allocations (arrays, objects, recursion stack, etc.).

- common classes:
  | Notation | Description | Example |
  | -------- | ----------------- | ------------------------------------------------ |
  | O(1) | Constant space | A few variables or pointers (like `i`, `count`). |
  | O(n) | Linear space | Creating a new array or list of size n. |
  | O(log n) | Logarithmic space | Recursion on half the input (depth ≈ log n). |
- Illustrative Example

```js
function countSevens(arr) {
  let count = 0; // O(1) space
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 7) {
      count++;
    }
  }
  return count; // No extra arrays or structures
}
```

- Space Complexity: O(1)(only count and i)
- Why It Matters
  - Some fast algorithms use lots of memory (e.g., creating big helper arrays).
  - Devices with limited RAM (like phones) may favor in-place (O(1) space) solutions even if they’re a bit slower.
