# creating lists (arrays)
fruits = ["apple", "orange", "banana", "pear"]
nums = [1, 2, 3, 4, 5]
empty = []

# Indexing and slicing
# index 0
print("Index 0--------------")
print(fruits[0])
print("Index -1--------------")
print(fruits[-1])
print("range-----------------")
print(nums[1:4])


# mutating
print("print index 1-----------------")
print(fruits[1])
print("add at the end----------------------")
print(nums.append(6))
print("insert on after index 3 which is value 4--------")
print(nums.insert(3, 4.5))
print("removing the value 4.5 --------------")
print(nums.remove(4.5))
print("removing the last value which is 6--------")
last_value = nums.pop()
print(last_value)


# inspecting
print("length of the nums-------------")
print(len(nums))
print("check if the value 3 exists in the list----------")
print(3 in nums)
print("count the number of 5's-------")
print(nums.count(5))
print("find out the index of 3--------------")
print(nums.index(3))

# Ordering
print("sort in place------")
print(fruits.sort())
print("return a new sorted list-------")
print(sorted(fruits))
print("reverse in place-----------")
print(nums.reverse())
