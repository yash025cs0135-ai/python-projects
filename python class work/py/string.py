# ============================================================
# String Practice Set 3.3
# Q1 to Q12 - Combined Program
# ============================================================


# Q1. Input a string and display original string,
#     length and data type
print("\n========== Q1 ==========")

text = input("Enter a string: ")

print("Original String:", text)
print("Length:", len(text))
print("Data Type:", type(text))


# Q2. Display different parts of the string
print("\n========== Q2 ==========")

print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])
print("Characters from index 3 to 10:", text[3:11])
print("Every second character:", text[::2])
print("Reverse of the string:", text[::-1])


# Q3. Count uppercase, lowercase, digits,
#     spaces and special characters
print("\n========== Q3 ==========")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isupper():
        uppercase += 1

    elif ch.islower():
        lowercase += 1

    elif ch.isdigit():
        digits += 1

    elif ch.isspace():
        spaces += 1

    else:
        special += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


# Q4. Check whether string is palindrome or not
print("\n========== Q4 ==========")

clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# Q5. Replace every space with a hyphen
print("\n========== Q5 ==========")

hyphen_text = text.replace(" ", "-")

print("Original String:", text)
print("After replacing spaces:", hyphen_text)


# Q6. Check whether two strings are anagrams
print("\n========== Q6 ==========")

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

s1 = string1.replace(" ", "").lower()
s2 = string2.replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("The strings are Anagrams")
else:
    print("The strings are not Anagrams")


# Q7. Find frequency of each character
print("\n========== Q7 ==========")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:")

for ch, count in frequency.items():
    print(ch, ":", count)


# Q8. Display every word on a new line
print("\n========== Q8 ==========")

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Words:")

for word in words:
    print(word)


# Q9. Reverse the order of words in a sentence
print("\n========== Q9 ==========")

words = sentence.split()

reversed_words = words[::-1]

print("Original Sentence:", sentence)
print("Reversed Word Order:", " ".join(reversed_words))


# Q10. Remove duplicate characters from a string
print("\n========== Q10 ==========")

duplicate_string = input("Enter a string: ")

result = ""

for ch in duplicate_string:
    if ch not in result:
        result += ch

print("Original String:", duplicate_string)
print("After removing duplicates:", result)


# Q11. Find the longest word in a sentence
print("\n========== Q11 ==========")

words = sentence.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest Word:", longest_word)
print("Length:", len(longest_word))


# Q12. Perform different string operations
print("\n========== Q12 ==========")

operation_string = input("Enter a string: ")

# Convert to uppercase
print("Uppercase:", operation_string.upper())

# Convert to lowercase
print("Lowercase:", operation_string.lower())

# Swap case
print("Swap Case:", operation_string.swapcase())

# Remove leading/trailing spaces
print("Without leading/trailing spaces:",
      operation_string.strip())

# Replace one word with another
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

replaced_string = operation_string.replace(old_word, new_word)

print("After replacement:", replaced_string)

# Split into words
word_list = operation_string.split()

print("Split into words:", word_list)

# Join words using hyphen
joined_string = "-".join(word_list)

print("Joined using hyphen:", joined_string)


print("\n========== PROGRAM COMPLETED ==========")