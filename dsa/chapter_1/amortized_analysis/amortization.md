**Amortized Analysis**

- Amortization in algorithms is like sharing the cost of a big job across many small jobs so you see how expensive each job is on average.

- Simple Picture
  - Big Job:
    - Every so often you do something slow (e.g., resize a growing array, or replace your full piggy bank).
  - Small Jobs:
    - Most of the time you do quick, tiny steps (e.g., add one item, drop one coin).
  - Amortized Cost:
    - You take the total work of all the big jobs plus the tiny jobs, then divide by the number of tiny jobs to find the average work per tiny job.
- Key Idea:
  Even though some steps are slow, when you spread out their cost over all steps, each step is still cheap on average.

- Amortized Cost in a Dynamic Array:
  - Imagine a toy box that holds toys in a row.
    - Start Small: It can hold 1 toy at first.
    - Add a Toy:
      - If there’s room, you just drop it in—1 quick step.
      - If it’s full, you must:
        a. Make a new box twice as big.
        b. Move all toys over (one by one).
        c. Then add the new toy.
- Counting the Steps - Assume you add n toys, and each time you double:
  | Append # | Capacity Before | Action | Cost (steps) |
  | -------- | --------------- | ---------------------- | ---------------------- |
  | 1 | 1 | add in place | 1 |
  | 2 | 1 (full) | resize (1 move) + add | 1 (move) + 1 (add) = 2 |
  | 3 | 2 | add in place | 1 |
  | 4 | 2 (full) | resize (2 moves) + add | 2 + 1 = 3 |
  | 5–8 | 4 | adds in place | each 1 |
  | 9 | 4 (full) | resize (4 moves)+ add | 4 + 1 = 5 |
  | … | … | … | … |
  | Up to n | … | … | … |

  - Resize costs happen at sizes 1, 2, 4, 8, …, up to ≤ n.
  - Total resize cost ≈ 1 + 2 + 4 + … + (≤n) ≈ 2n steps.
  - Plus the simple adds (n steps).
  - Total ≈ 3n steps over n appends.

- Average (“Amortized”) Cost
  Total work ≈ 3n steps.
  Number of appends = n.
  Average per append = (3n) / n = 3 steps → O(1) time amortized.
- Key Idea:
  Even though some appends take many steps (when resizing), most take just one, and on average each append is still a constant-time operation.
