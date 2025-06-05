Try It Yourself
Create a standalone module

File: string_utils.py

Functions to include:

reverse(s): returns the reverse of string s.

is_palindrome(s): returns True if s reads the same backwards (ignore case and punctuation for extra credit).

Create a package

textproc/
├── **init**.py
├── clean.py
└── transform.py
clean.py:

remove_punctuation(s): returns s with punctuation removed. You can use str.isalnum() to filter characters.

transform.py:

to_upper(s): returns s.upper().

to_lower(s): returns s.lower().

Write a script app.py in the parent directory (project_root/):

python
Copy
Edit

# app.py

# 1. Import your functions

from string_utils import reverse, is_palindrome
from textproc.clean import remove_punctuation
from textproc.transform import to_upper, to_lower

sample = "A man, a plan, a canal, Panama!"

# 2. Clean the sample

cleaned = remove_punctuation(sample)
print("Cleaned:", cleaned)

# 3. Transform to uppercase

uppercased = to_upper(cleaned)
print("Uppercase:", uppercased)

# 4. Check palindrome ignoring case

lowered = to_lower(cleaned)
print("Is palindrome?", is_palindrome(lowered))

# 5. Print reversed

print("Reversed:", reverse(cleaned))
Run app.py and observe:

Does it remove punctuation properly?

Does it convert case?

Does it correctly detect the palindrome?

Does it reverse the cleaned string?
