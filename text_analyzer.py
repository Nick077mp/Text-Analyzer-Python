# Text analyzer program.
text = input("Enter a text: ").lower()  # Get input text from the user and convert it to lowercase
letter_1 = input("Enter the first letter: ")  # Get the first letter from the user
letter_2 = input("Enter the second letter: ")  # Get the second letter from the user
letter_3 = input("Enter the third letter: ")  # Get the third letter from the user

# Create a list of the specified letters in lowercase
letters_list = [letter_1.lower(), letter_2.lower(), letter_3.lower()]

# Count occurrences of each letter in the text
count_1 = text.count(letters_list[0])  # Count the first letter
count_2 = text.count(letters_list[1])  # Count the second letter
count_3 = text.count(letters_list[2])  # Count the third letter

# Print the count of each specified letter
print(f"Count found for each of the specified letters:\nThe letter {letter_1} appears {count_1} times.\nThe letter {letter_2} appears {count_2} times.\nThe letter {letter_3} appears {count_3} times.")
print("////////////////////////////////////////////////////////////\n\n")

# Convert the text to a list of characters
text_list = list(text)
print(text_list)  # Print the list of characters
count_text_list = len(text_list)  # Count the total number of characters in the text
print(f"Total number of characters found in the text: {count_text_list}")
print("////////////////////////////////////////////////////////////\n\n")

# Get the first and last letters of the text
first_letter = text_list[0]
last_letter = text_list[-1]

# Check if the last letter is a valid letter
if last_letter in "abcdefghijklmnñopqrstuvwxyz":
    print(f"The first letter of the text is: {first_letter}\nThe last letter of the text is: {last_letter}")
    print("////////////////////////////////////////////////////////////\n\n")
else:
    print(f"The first letter of the text is: {first_letter}. It seems your last character is not a letter.")

# Print the reversed text
print("This is your text reversed, HAHA!")
text_list.reverse()  # Reverse the list of characters
reversed_text_join = " ".join(text_list)  # Join the reversed list into a string
print(f"Your text reversed: '{reversed_text_join}'")
print("////////////////////////////////////////////////////////////\n\n")

# Check if the word 'python' is in the text
search_python = 'python' in text  # The variable search_python stores a boolean
dic_python = {True: "yes", False: "no"}  # Dictionary for translating boolean to string
print(f"The word 'Python' {dic_python[search_python]} is found in the text.")
