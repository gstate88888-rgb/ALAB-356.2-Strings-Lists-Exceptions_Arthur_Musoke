# string_manipulation.py

# Prompt the user for a sentence
sentence = input("Enter a sentence: ")

# Convert to uppercase
uppercase_sentence = sentence.upper()

# Reverse the sentence
reversed_sentence = sentence[::-1]

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1

# Replace spaces with hyphens
hyphen_sentence = sentence.replace(" ", "-")

# Display results
print("\nResults:")
print("Uppercase:", uppercase_sentence)
print("Reversed:", reversed_sentence)
print("Vowel Count:", vowel_count)
print("Hyphenated:", hyphen_sentence)
