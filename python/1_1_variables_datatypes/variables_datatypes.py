# How we figure out type of variables
a = 7
user_name = "AW"
is_ready = False
user_name = 7  # this will output #<class 'int'> because it was reassigned again
num = 19.2
print(type(a))  # <class 'int'>
print(type(user_name))  # <class 'str'>
print(type(is_ready))  # <class 'bool'>
print(type(num))  # <class 'float'>
