# removes punctuation
def remove_punctuation(s):
    cleaned = ""
    for x in s:
        if x.isalnum():
            cleaned += x

    return cleaned


print(remove_punctuation("Hello, abel"))
