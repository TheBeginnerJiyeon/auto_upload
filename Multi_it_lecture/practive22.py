# Original string with leading and trailing whitespace
original_string = "   Hello, world!    "

# Remove leading whitespace
cleaned_string_start = original_string.lstrip()

# Remove trailing whitespace
cleaned_string_end = original_string.rstrip()

print("Original string:", original_string)
print("Cleaned string (leading whitespace removed):", cleaned_string_start)
print("Cleaned string (trailing whitespace removed):", cleaned_string_end)
