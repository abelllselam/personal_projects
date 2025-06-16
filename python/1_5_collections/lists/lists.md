**What is a List**

- It is an ordered mutable sequence of elements
- Elements can be any type (even mixed in the same list).
- Defined with square brackets:[...].

# Core Operations:

- Creation

```py
empty = []
nums = [1,2,3]
fruits = ["apple","banana","cherry"]

//Indexing & Slicing

fruits[0] #apple
fruits[-1] #cherry
nums[1:3] #[2,3]

//mutating
fruits[1] #banana
nums.append(4) #[1,2,3,4]
nums.insert(2,2.5) #[1,2,2.5,3,4]
nums.remove(2.5) #[1,2,3,4]
last = nums.pop() #removes & returns 4

//Inspecting
len(fruits) #3
2 in nums #true
nums.count(2) #how many 2's
nums.index(3) #index of first 3

//ordering
nums.sort() #sorts in place
sorted(fruits) #returns a new sorted list
nums.reverse() #reverse in place
```
