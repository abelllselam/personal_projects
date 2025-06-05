# Returns the reverse of strings
def reverseString(val):
    lowercase_val = val.lower()
    # print(lowercase_val)
    reversed_val = "".join(reversed(lowercase_val))
    # print(reversed_val)
    if lowercase_val == reversed_val:
        return True

    return False


# print(reverseString("raceCar"))
