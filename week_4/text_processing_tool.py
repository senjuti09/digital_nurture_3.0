```python
# text_processing_tool/__init__.py
from .count_words import count_words
from .find_unique_words import find_unique_words
from .convert_to_uppercase import convert_to_uppercase

# text_processing_tool/count_words.py
def count_words(text):
    return len(text.split())

# text_processing_tool/find_unique_words.py
def find_unique_words(text):
    return set(text.split())

# text_processing_tool/convert_to_uppercase.py
def convert_to_uppercase(text):
    return text.upper()

# main.py
from text_processing_tool import count_words, find_unique_words, convert_to_uppercase

text = input("Enter a text string: ")
print("Choose an action: 1. Count Words 2. Find Unique Words 3. Convert to Uppercase")
choice = int(input("Enter the number corresponding to your choice: "))

if choice == 1:
    result = count_words(text)
elif choice == 2:
    result = find_unique_words(text)
elif choice == 3:
    result = convert_to_uppercase(text)
    
print("Result:", result)
```
