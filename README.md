# Text-Analyzer-Python


Text Analyzer Script (README.md)
This script demonstrates several functionalities for analyzing text data in Python. Users can interact with the program to perform various analyses on a provided text string.

Here's a breakdown of the functionalities:

# User Input and Letter Counting:
The script prompts the user to enter a text string and three characters.
It converts all input (text and characters) to lowercase for case-insensitive analysis.
It then creates a list containing the three specified letters.
Finally, it utilizes the count method to determine the frequency of each letter within the text.

# Character Analysis:
The script converts the user-provided text into a list of individual characters.
It then calculates the total number of characters in the text using the len function.

# First and Last Letter Detection:
By accessing the first and last element of the character list, the script retrieves the first and last letters of the text.
It includes a validation check to ensure the last character is actually a letter (a-z or ñ).

# Text Reversal:
The script utilizes the reverse method to reverse the order of characters in the list.
It then joins the reversed list back into a string using the join method.

# Word Search:
The script checks if the word "python" (case-insensitive) exists within the text using the in operator.
It employs a dictionary to translate the resulting boolean value (True/False) into a user-friendly string ("yes" or "no").

#Running the Script:
1. Save the code snippet as a Python file (e.g., text_analyzer.py).
2. Open a terminal or command prompt and navigate to the directory containing the saved file.
3. Execute the script using the python command followed by the filename: python text_analyzer.py
4. Follow the prompts to enter the desired text and characters for analysis.
Note: This script serves as a basic example and can be further enhanced with additional functionalities.
