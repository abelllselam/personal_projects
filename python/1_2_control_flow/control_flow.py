# # control flow

# # if Statement
# score = 85

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("Below B")

# # for loop:
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

# # using range()
# # for range (start, stop, step)
# for i in range(3):
#     print(i)  # prints 0, then 1, then 2

# # ---------------------------------------------------
# print("Exercise")
# print("------------------------------------")

# print("Using continue, break in for..in loop")
# numbers = [1, -2, 3, 4, -5, 6]

# for num in numbers:
#     if num < 0:
#         continue
#     elif num == 4:
#         break
#     else:
#         print("Processing number: ", num)
# print("------------------------------------")

# # Using range
# print("Using in range()")
# for num in range(5, 0, -1):
#     print("Countdown: ", num)


# print("------------------------------------")
# print("Using enumerate (start at 1):")
# colors = ["red", "green", "blue"]

# for idx, color in enumerate(colors, start=1):
#     print(idx, " -> ", color)

# print("------------------------------------")
# print("Iterate over a dictionary")
# person = {"name": "Alice", "age": 30, "city": "NY"}

# # Printing keys only
# print('Printing keys only person = {"name": "Alice", "age": 30, "city": "NY"}')
# for per in person:
#     print(per)

# print("------------------------------------")
# print('Printing values only person = {"name": "Alice", "age": 30, "city": "NY"}')
# for per in person.values():
#     print(per)

# print("------------------------------------")
# print(
#     'Printing both key and values only person = {"name": "Alice", "age": 30, "city": "NY"}'
# )
# for key, value in person.items():
#     print("The key: ", key, " and the Value: ", value)

print("--------------------------------------------------")
print("Exercise")
print("--------------------------------------------------")
x = 10

while x >= 1:
    print("T-minus: ", x)
    x -= 1
else:
    print("Liftoff!")
