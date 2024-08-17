#String handling is a frequently done task in any programming language. 

#E1: String Concatenation
#Question: Write a Python script that concatenates three strings (str1, str2, and str3) to form a complete sentence. You need to print the output sentence to the console. In this exercise, the strings represent “Hello”, a space (” “), and “Python!” respectively.

1
2
3
4
5
6
# Exercise: Combine the following strings and print the result.
str1 = "Hello"
str2 = " "
str3 = "Python!"
result = str1 + str2 + str3
print(result)
#Output:
Hello Python!
#In this exercise, we are using the + operator to concatenate three strings – “Hello” a space (” “), and “Python!“. The print(result) statement will display the combined string.

#E2: String Length
#Question: Find and print the length of a string. After calculating, you need to print the length.

1
2
3
4
# Exercise: Find and print the length of the string.
my_string = "Python is amazing!"
length = len(my_string)
print("Length of the string:", length)
#Output:
Length of the string: 18
#The len() function calculates the length of a string. In this example exercises for beginners, we are using it to print the length of the given string “Python is amazing!”.

#E3: Accessing Characters
#Question: Write a Python program that prints the first and last characters of a given string. The program should display the results using a print statement.

1
2
3
4
5
6
# Exercise: Print the first and last characters of the string.
word = "Python"
first_char = word[0]
last_char = word[-1]
print("First Character:", first_char)
print("Last Character:", last_char)
Output:
First Character: P
Last Character: n
#The string is assigned to the variable word. The first character is accessed using word[0], and the last character is accessed using word[-1].

#E4: Slicing Strings
#Question: Write a Python program that extracts and prints the substring “is” from a given string: “Python is versatile.”.

1
2
3
4
# Exercise: Print the substring "is" from the given string.
sentence = "Python is versatile."
substring = sentence[7:9]
print("Substring:", substring)
Output:
Substring: is
#This Python code is an exercise that prints the substring “is” from the given string “Python is versatile.” The string is assigned to the variable sentence, and the substring is extracted using slicing with the indices 7 (inclusive) to 9 (exclusive).

#E5: Reversing a String
#Question: Create a Python program that reverses a given string (“Python is fun!”) and prints the result.

1
2
3
4
# Exercise: Reverse the given string and print the result.
original_string = "Python is fun!"
reversed_string = original_string[::-1]
print("Reversed String:", reversed_string)
#Output:
Reversed String: !nuf si nohtyP
#This exercise focuses on the use of string slicing with a negative step to reverse a string in Python. The string is assigned to the variable original_string, and the slicing notation [::-1] is used to reverse the entire string. I have mentioned a similar example in the Python print exercise.

#E6: Changing Case
#Question: Write a Python script that converts a given string (“Python Programming”) to lowercase and prints the result.

1
2
3
4
# Exercise: Convert the string to lowercase and print it.
text = "Python Programming"
lowercase_text = text.lower()
print("Lowercase:", lowercase_text)
#Output:
Lowercase: python programming
#This Python code is an exercise that converts the string “Python Programming” to lowercase and prints the result. The string is assigned to the variable text, and the lower() method is applied to convert all characters to lowercase. Similarly, you can use upper() function to convert string to upper case in Python.

#E7: Checking Case
#Question: Develop a Python code that checks whether a given string is in uppercase and prints the result in boolean (True or False).

1
2
3
4
# Exercise: Check if the given string is in uppercase and print the result.
uppercase_string = "HELLO PYTHON"
is_uppercase = uppercase_string.isupper()
print("Is Uppercase?", is_uppercase)
#Output:
Is Uppercase? True
#The string is assigned to the variable uppercase_string, and the isupper() method is used to determine whether all characters in the string are uppercase.


#E8: Swapping Case
#Question: Write a Python program that swaps the case (upper to lower and lower to upper) of a given string and prints the result.

1
2
3
4
# Exercise: Swap the case of the given string and print the result.
mixed_case_string = "PyThOn PrOgRaMmInG"
swapped_case_string = mixed_case_string.swapcase()
print("Swapped Case:", swapped_case_string)
#Output:
Swapped Case: pYtHoN pRoGrAmMiNg
#Here we are using swapcase() method to reverse the case of each character. Then printing the resulting string with the swapped case in the console.

#E9: Title Case
#Question: Write a Python script that converts a given string to title case (the first character of every word to be capitalized and the rest of the characters should be in lowercase) and prints the result.

1
2
3
4
# Exercise: Convert the given string to title case and print the result.
sentence_to_title = "python programming is amazing"
title_case_sentence = sentence_to_title.title()
print("Title Case Sentence:", title_case_sentence)
#Output:
Title Case Sentence: Python Programming Is Amazing
#To achieve this, we assign the original string to the variable sentence_to_title, and apply a function .title() to make the entire string in the title case. Finally, print the title case string to the console.

#E10: Finding Substrings
#Question: Create a Python code that checks if a specific word, “easy” is present in a given string (“Programming in Python is easy.”) and prints the result.

1
2
3
4
# Exercise: Check if the word "easy" is present in the string.
quote = "Programming in Python is easy."
is_present = "easy" in quote
print("Is 'easy' present?", is_present)
#Output:
Is 'easy' present? True
#In this Python exercise, the objective is to determine if the word “easy” is present in the given string “Programming in Python is easy.” We assign the string to the variable quote, then check using the in keyword to see if the substring “easy” exists within it or not. Storing the result of this check in the variable is_present.

#E11: Replacing Characters
#Question: Develop a Python program that replaces the word ‘good’ with ‘awesome’ in a given string (“The tutorial is good.”) and prints the result.

1
2
3
4
# Exercise: Replace 'good' with 'awesome' in the string and print the result.
feedback = "The tutorial is good."
updated_feedback = feedback.replace("good", "awesome")
print("Updated Feedback:", updated_feedback)
#Output:
Updated Feedback: The tutorial is awesome.
#The original string, assigned to the variable feedback, undergoes the replacement operation using the replace() method. The updated feedback, stored in the variable updated_feedback, is then printed to the console.

#E12: String Formatting
#Question: Write a Python script that uses string formatting to insert the values of ‘name‘ and ‘age‘ into a given sentence and print the result. The values for ‘name’ and ‘age’ are: name = “Alice” and age = 25.

1
2
3
4
5
# Exercise: Use string formatting to insert the values of 'name' and 'age' into the sentence and print the result.
name = "Alice"
age = 25
sentence = "Hello, my name is {} and I am {} years old.".format(name, age)
print(sentence)
#Output:
Hello, my name is Alice and I am 25 years old.
#The variables ‘name’ (set to “Alice”) and ‘age’ (set to 25) are integrated into the sentence template “Hello, my name is {} and I am {} years old.” using the .format() method. We are storing this formatted sentence in the variable sentence, and then printing the result to the console.


#E13: Counting Occurrences
#Question: Develop a Python program that counts the number of times the character ‘o’ appears in a given string (“Python Programming”) and prints the result.

1
2
3
4
# Exercise: Count the number of times 'o' appears in the string and print the result.
word = "Python Programming"
count_o = word.count('o')
print("Number of 'o's:", count_o)
#Output:
Number of 'o's: 2
#In this Python exercises for beginners, the objective is to count the number of occurrences of the character ‘o’ in the given string “Python Programming.” We assign the string to the variable word. Passing this variable through the counting operation using the count() method, where the argument ‘o’ represents the character to be counted. We store the count result in the variable count_o, and the code then prints the outcome.

#E14: Joining Strings
#Question: Write a Python script that joins the elements of a given list ([‘Coding’, ‘is’, ‘fun’]) into a single string and prints the result.

1
2
3
4
# Exercise: Join the elements of the list into a single string and print the result.
words = ['Coding', 'is', 'fun']
joined_string = ' '.join(words)
print("Joined String:", joined_string)
#Output:
Joined String: Coding is fun
#In this Python exercise, the task is to join the elements of the list ['Coding', 'is', 'fun'] into a single string. We can do this easily using the .join(). Concatenating elements of this list using a space (‘ ‘) to make it a cohesive string.

#E15: Stripping Whitespace
#Question: Develop a Python program that removes whitespaces from a given string and prints the result.

1
2
3
4
5
# Exercise: Remove whitespaces from the string and print the result.
sentence = "   Python is fun   to work"
stripped_sentence = " ".join(sentence.split())
print("Before Sentence:", sentence)
print("Stripped Sentence:", stripped_sentence)

#Output:
Before Sentence:    Python is fun   to work
Stripped Sentence: Python is fun to work
#We assign the original string to the variable sentence. Then pass this variable through removal operation using a combination of split() and join() methods. The split() method divides the string into individual words. Then the join() method brings these words back together using a single space as a separator.

#E16: Splitting Strings
#Question: Create a Python program that splits a given string (“Coding is an art”) into a list of words ([‘Coding’, ‘is’, ‘an’, ‘art’]) and prints the result.

1
2
3
4
# Exercise: Split the string into a list of words and print the result
quote = "Coding is an art"
word_list = quote.split()
print("Word List:", word_list)
#Output:
Word List: ['Coding', 'is', 'an', 'art']
#After applying split() method, the string separates it into individual words based on whitespace. Note: you can mention the way of splitting. For example, if you want to split by comma the function should look like: split(',').

#E17: Formatting Numbers in Strings
#Question: Write a Python script that formats a given number (1500.50) as a currency ($1,500.50) and prints the result.

1
2
3
4
# Exercise: Format the given number as a currency and print the result.
amount = 1500.50
formatted_amount = "${:,.2f}".format(amount)
print("Formatted Amount:", formatted_amount)
#Output:
Formatted Amount: $1,500.50
#We can achieve this by using the format() method with the format specifier "{:,.2f}" to represent the number in currency format with two decimal places and comma separators for thousands. If you want a simpler and hardcoded way then you can try this code: "$" + str(1500.50)

#E18: String Repetition
#Question: Create a Python program that repeats a given word (‘Python’) three times and prints the result (PythonPythonPython).

1
2
3
4
# Exercise: Repeat the word 'Python' three times and print the result.
word_to_repeat = 'Python'
repeated_word = word_to_repeat * 3
print("Repeated Word:", repeated_word)
#Output:
Repeated Word: PythonPythonPython
#You can use the * operator to repeat a string a certain number of times. Here, we repeat the word ‘Python’ three times.

#E19: Finding Index of a Substring
#Question: Develop a Python script that finds the index of the first occurrence of the word ‘world’ in a given string (“Hello, world! Python world!”) and prints the result.

1
2
3
4
# Exercise: Find the index of the first occurrence of 'world' in the string and print the result.
text = "Hello, world! Python world!"
index_of_world = text.find('world')
print("Index of 'world':", index_of_world)
#Output:
Index of 'world': 7
#You can do this using find() method. Here we are assigning the string to the variable text. Then apply the find() method to locate the starting index of the specified substring ‘world’.


#E20: Padding a String
#Question: Write a Python code that pads a given string (“Python”) with dashes on both sides (——-Python——-) to make it 20 characters long and prints the result.

1
2
3
4
# Exercise: Pad the given string with dashes on both sides to make it 20 characters long and print the result.
text_to_pad = "Python"
padded_text = text_to_pad.center(20, '-')
print("Padded Text:", padded_text)
#Output:

#You can use the center() method to center the string within a 20-character width, filling the remaining spaces on both sides with dashes (‘-‘). Storing the padded text in the variable padded_text for further printing. This exercises for beginners demonstrates an effective way to manipulate the alignment and length of string in Python.

#E21: Finding the Most Common Character
#Question: Write a Python program that finds and prints the most common (frequent) character in a given string (“python programming”).

1
2
3
4
# Exercise: Find and print the most common character in the given string.
input_string = "python programming"
most_common_char = max(set(input_string), key=input_string.count)
print("Most Common Character:", most_common_char)
#Output:
Most Common Character: p
