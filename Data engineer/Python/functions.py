#Exercise 1: Basic Print Statement
#Question: Write a simple Python program that prints the phrase “Hello, Python!” to the console.

1
print("Hello, Python!")
#Output:
Hello, Python!
#In this Python program, we have a single line of code that utilizes the print statement to display the text “Hello, Python!” on the console. I used double (” “) quotes to enclose the string “Hello, Python!”, but you can also use a single (‘ ‘) quote.


#Exercise 2: Printing Variables
#Question: Create a Python program that defines variables for a person’s name and age. Then print these details to the console. The program should display output in the format: “Name: [Name] Age: [Age]”. This exercise aims to familiarize Python learners with variable assignment and printing multiple values in a single statement.

1
2
3
name = "John"
age = 25
print("Name:", name, "Age:", age)
#Output:

Name: John Age: 25
T#he first two lines of the above Python script are to assign name and age variables. Then finally we used print statement to display output on the console. Here, it prints the concatenated text and variable values. The comma (,) in the print statement separates the different items to be printed.


#Exercise 3: Concatenating Strings
#Question: Develop a Python code that utilizes two variables, greeting and subject. Concatenate these variables and print the combined message in this format: “Greeting: [Greeting], and Subject: [Subject]”.

1
2
3
greeting = "This is first variable"
subject = "This is second variable"
print(greeting + ", and " + subject + "!")
#Output:
#This is first variable, and This is second variable!
#In the first two lines, we are initializing those two variables (greeting and subject). Then the print() statement combines the values of greeting, “, and “, subject, and “!” using the + operator.

#Exercise 4: Formatting Strings
#Question: In this exercises, write a Python program that defines variables for a person’s name and age, and then prints these details using the format function. The code should display output in the format: “Name: [Name], Age: [Age]”. This exercise aims to introduce learners to the format method for string formatting.

1
2
3
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))
Output:
Name: Alice, Age: 30
#Here the print statement uses the format method to insert the values of name and age into the specified positions within the string. The curly braces {} act as placeholders. The values inside the format method (in order) replace these placeholders.

#Exercise 5: f-Strings (Formatted String Literals)
#Question: Write a Python script that defines variables for a person’s name and age, and then prints these details using f-strings. The program should display output in the format: “Name: [Name], Age: [Age]”.

1
2
3
name = "Bob"
age = 22
print(f"Name: {name}, Age: {age}")
#Output:
Name: Bob, Age: 22
#Here the print statement uses an f-string, indicated by the ‘f’ prefix before the string. Inside the f-string, expressions enclosed in curly braces {} are evaluated and replaced with the corresponding values of the variables.

#Exercise 6: Print Multiple Lines
#Question: In this exercises, develop a Python program to print multiple lines of text to the console using just print function. The program should output the following lines:

Line 1
Line 2
Line 3
1
2
# Print multiple lines in Python
print("Line 1\nLine 2\nLine 3")
#Output:
Line 1
Line 2
Line 3
#The print statement outputs three lines of text using the escape sequence \n to create line breaks. This sequence (\n) is read as a newline character, which means the following text will be printed on a new line.


#Exercise 7: Printing in Reverse
#Question: Create a Python program that takes a string variable (text) and prints its reversed version. The program should output the reversed text with the label “Reversed: [Reversed Text]”.

1
2
3
# Print in reverse
text = "I Love Python"
print("Reversed:", text[::-1])
#Output:
Reversed: nohtyP evoL I
#Here the print statement outputs the reversed version of the text variable using string slicing with the [::-1] notation. This slice notation reverses the string.

#Exercise 8: Printing Emojis
#Question: Write a Python script to print three emojis in the console. Utilize Unicode escape sequences for the following emojis: 😍 (Heart Eyes), 🚀 (Rocket), and 👍 (Thumbs Up). The program should output these emojis with appropriate labels.

1
2
# Print emojis in Python
print("\U0001F60D", "\U0001F680", "\U0001F44D")
#Output:
😍 🚀 👍
#Here Unicode escape sequences \U0001F60D, \U0001F680, and \U0001F44D correspond to the emojis 😍 (Heart Eyes), 🚀 (Rocket), and 👍 (Thumbs Up) respectively.


#Exercise 9: Printing Chess Board
#Question: Write a Python program to generate a simple chessboard pattern. The program should use a nested loop to print an 8×8 chessboard, where black squares are represented by “■” (black square) and white squares are represented by “□” (white square). The program should output the chessboard pattern to the console.

1
2
3
4
5
6
7
# Printing Chess Board in Python
size = 8
 
for i in range(size):
    for j in range(size):
        print("■ " if (i + j) % 2 == 0 else "□ ", end="")
    print()
Output:
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■ 
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■ 
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■ 
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■
#This Python code prints an 8×8 chessboard pattern using “■” (black square) and “□” (white square). It uses nested loops to iterate over each row and column. The choice of square (black or white) is determined by the condition (i + j) % 2 == 0. The end="" in the print statement ensures that the squares are printed side by side in each row.

#Exercise 10: ASCII Art
#Question: Write a Python script to print a stylized ASCII art representation of word “Thank you”. This exercise is designed to show you the creative side of Python programming and inspire you to use ASCII art for enjoyment and visual charm.

1
2
3
4
5
6
7
8
9
10
print("""
  _______ _                 _                
 |__   __| |               | |               
    | |  | |__   __ _ _ __ | | __   _   _  ___   _   _ 
    | |  | '_ \ / _` | '_ \| |/ /  | | | |/ _ \ | | | |
    | |  | | | | (_| | | | |   <   | |_| | (_) || |_| |
    |_|  |_| |_|\__,_|_| |_|_|\_\   \__, |\___/ \___,_|
                                     __/ |        
                                    |___/      
""")
Output:
print-ascii-art-in-python
#We can use triple-quoted (“”” “””) strings to enclose the ASCII art, allowing for multiline string representation. I tried to display the word “Thank you”. You can try other words also.

#Exercise 11: Printing a Countdown
#Question: In this exercises, write a Python code to display (using print function) a countdown from 5 to 1, followed by the message “Blast off!” after the countdown completes. Utilize the time module to introduce a one-second delay between countdown steps.

1
2
3
4
5
6
7
8
# Print Countdown in Python
import time
 
for i in range(5, 0, -1):
    print(f"Countdown: {i}")
    time.sleep(1)
 
print("Blast off!")
#Output:
Print-Countdown-in-Python
#This Python code prints a countdown from 5 to 1 with a one-second delay between each count using the time.sleep(1) function. After the countdown, it prints “Blast off!” to signify the end of the countdown.

#Exercise 12: Dynamic Line Printing
#Question: Write a Python program to simulate a loading process with a progress indicator. The program should display “Loading… [current step]/5” in the same line, updating the progress in real-time. After completing the loading simulation, print “Loading complete!” on a new line.

1
2
3
4
5
6
7
8
9
10
# Print in the same line in python
import sys
import time
 
for i in range(1, 6):
    sys.stdout.write(f"\rLoading... {i}/5")
    sys.stdout.flush()
    time.sleep(1)
 
print("\nLoading complete!")
#We can use sys.stdout.write to overwrite the previous line by using the carriage return character (\r). The progress is displayed as “Loading… [current count]/5“. The sys.stdout.flush() ensures that the output is immediately visible, and time.sleep(1) introduces a one-second delay between updates. After the loop, it prints “Loading complete!” on a new line.


Output:
dynamic-printing-in-the-same-line-in-python
#Exercise 13: Print a Loading Spinner
#Question: Write a Python script to create a loading spinner animation. The spinner should cycle through the characters ‘|’, ‘/’, ‘-‘, and ‘\’ to create the appearance of spinning. The program should run indefinitely until manually interrupted.

1
2
3
4
5
6
7
8
9
10
11
12
13
# Print Loading Spinner exercises in Python
import sys
import itertools
import time
 
def loading_spinner():
    for char in itertools.cycle('|/-\\'):
        sys.stdout.write('\rLoading ' + char)
        sys.stdout.flush()
        time.sleep(0.1)
 
# Example Usage
loading_spinner()
#Output:
print-Loading-Spinner-exercises-with-solutions-examples-in-python
#We defined a function loading_spinner to print a loading spinner animation in the console. It uses the itertools.cycle function to iterate indefinitely through the characters ‘|’, ‘/’, ‘-‘, and ‘\’. The animation is displayed using \r to overwrite the previous line. And time.sleep(0.1) introduces a slight delay between each character for a smoother effect.

#Exercise 14: Printing a Custom Progress Bar
#Question: Write a Python program to display a custom progress bar for a given iteration and the total number of iterations. The progress bar should include a percentage indicator. Additionally, introduce a slight delay between iterations using the time.sleep method to simulate a real-time progress update.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
# Print custom progress bar in python
def print_custom_progress_bar(iteration, total, length=30):
    percent = int((iteration / total) * 100)
    progress = int(length * iteration // total)
    bar = "#" * progress + "-" * (length - progress)
    print(f"\rProgress: [{bar}] {percent}%", end="")
 
# Example Usage
total_iterations = 50
for i in range(1, total_iterations + 1):
    print_custom_progress_bar(i, total_iterations)
    time.sleep(0.1)
 
print("\nTask complete!")
#Output:
print-progress-bar-in-python-for-loop
#The progress bar consists of “#” representing completed progress and “-“ representing remaining progress. The function takes three parameters: iteration (current iteration), total (total number of iterations), and an optional parameter length (length of the progress bar, default is 30).

#In this print assignment example, we used a loop that iterates from 1 to total_iterations, calling the print_custom_progress_bar function at each iteration to display the progress. A slight delay (time.sleep(0.1)) is introduced for visualization. After the loop, it prints “Task complete!” on a new line (using \n).

#Exercise 15: Print Execution Time
#Question: Write a Python program to calculate the duration of a specific task’s execution time. Use datetime module to record the start and end times, and calculate the duration.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
from datetime import datetime
import time
 
# Record the start time
start_time = datetime.now()
 
# do your work here
# For example, a simple loop
for i in range(100):
    time.sleep(1)
    pass
 
# Record the end time
end_time = datetime.now()
 
# Print the execution time
print('Duration: {}'.format(end_time - start_time))
#Output:
Duration: 0:01:40.704905
#This Python code measures the execution time of a specific task using the datetime module. It records the start time, performs a simulated task (a loop with a one-second delay per iteration), records the end time, and calculates the duration.

#Note: Just for the example, I used the work in the loop with a time.sleep(1) statement, which simulates a task taking one second to complete. You can change this to your actual code.

#You can also calculate code execution using time library in Python. But I personally like the format datatime library produces by default. It is accurate and you can easily find how many hours, minutes, seconds and milliseconds takes to execute your Python code.

#Exercise 16: Print Colored Text
#Question: Write a Python script that prints colored text in the console. You can use colorama library of Python. The program should print “Success!” in green and “Error!” in red.

1
2
3
4
5
6
7
# Print Colored Text in Python
from colorama import Fore, Back, Style, init
 
init(autoreset=True)
 
print(Fore.GREEN + "Success!" + Style.RESET_ALL)
print(Fore.RED + "Error!" + Style.RESET_ALL)
#Output:
print-colored-text-exercise-solution-example-in-python
#This Python code uses a library called colorama to print text in different colors in the console. It starts by setting up the library and then prints “Success!“ in green (using Fore.GREEN) and “Error!“ in red (using Fore.RED). The code ensures that the color settings reset (using autoreset=True) after each print so that the rest of the text appears in the default color.


#Note: This code will only work in the Python command prompt console. It will not work in Jupyter Notebook. In Jupyter Notebook you will not see the color changes.

#Exercise 17: Printing in Columns
#Question: Create a Python program that prints tabular data in a neat and organized format. The table should have two columns: one for the fruit name and one for the quantity.

1
2
3
4
# Print like a tabular data in Python
data = [("Apple", 3), ("Banana", 6), ("Cherry", 4)]
for item in data:
    print(f"{item[0]:<10} | {item[1]:>2}")
$#Output:
print-like-a-tabular-data-in-python
#The data variable contains tuples representing items and their quantities. The for loop iterates through each tuple and uses formatted strings to print the data in a tabular layout.

#The first element of each tuple (item) is left-aligned with a width of 10 characters, and the second element (quantity) is right-aligned with a width of 2 characters. This results in a clear and organized presentation of the tabular data.

#Exercise 18: Printing GitHub-Style Markdown Table
#Question: This Python print function exercises is an extension of the previous one. In the print function assignment write a Python script using tabulate library to create a GitHub-style table from a list of tuples. First, install this library using the below pip command.

!pip install tabulate
#Leverage the Tabulate library to print a GitHub-style markdown table. This example displays information about individuals in a neat and structured format.

1
2
3
4
5
6
7
from tabulate import tabulate
 
data = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
headers = ["Name", "Age"]
 
table = tabulate(data, headers, tablefmt="github")
print(table)
#Output:
python-print-function-exercises-with-solutions-display-github-style-markdown-table
#The headers list provides column titles and data contans list of tuples . The tablefmt="github" parameter specifies the GitHub-flavored markdown format for the table.

#You can also produce the same output using prettytable library in Python. Below is the code to do this.

!pip install prettytable
1
2
3
4
5
6
7
from prettytable import PrettyTable
 
table = PrettyTable(["Fruit", "Quantity"])
table.add_row(["Apple", 3])
table.add_row(["Banana", 6])
table.add_row(["Cherry", 4])
print(table)
Output:
print-data-in-table-format-in-python
