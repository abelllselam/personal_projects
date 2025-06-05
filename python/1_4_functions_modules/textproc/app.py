from string_util import reverseString
from textprocdir import clean
from textprocdir import transform

sample = "A man, a plan, a canal, Panama!"

# 2. Clean the sample
cleaned = clean.remove_punctuation(sample)
print("Cleaned:", cleaned)

# 3. Transform to uppercase
uppercased = transform.to_uppercase(cleaned)
print("Uppercase:", uppercased)

# 4. Check palindrome ignoring case
lowered = transform.to_lowercase(cleaned)
print("Is palindrome?", reverseString(lowered))

# 5. Print reversed
print("Reversed:", reverseString(cleaned))
