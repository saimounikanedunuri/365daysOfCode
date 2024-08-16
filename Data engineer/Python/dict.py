#Dictionary concepts:
# reference: https://thinkinfi.com/12-python-dictionaries-practice-exercises-for-beginners/
#What is a Dictionary?
#A dictionary is an unordered collection of key-value pairs. Each key is unique and maps to a specific value. Think of it like a real-life dictionary where you look up a word (the key) to find its meaning (the value). Below example code is to create a dictionary in Python:

1
2
my_dict = {"apple": "a fruit", "dog": "a pet", "car": "a vehicle"}
print(my_dict)
{'apple': 'a fruit', 'dog': 'a pet', 'car': 'a vehicle'}
#Now, let’s begin with some practice exercises to gain confidence in Python dictionaries:

#Exercise 1: Creating a Dictionary
#Create a dictionary called student with the following key-value pairs:

“name” – “John”
“age” – 20
“grade” – “A”
1
student = {"name": "John", "age": 20, "grade": "A"}

#Exercise 2: Accessing Values
#Given the student dictionary from Exercise 1, write code to print the student’s name and age.

1
2
3
4
# dictionaries exercises python
student = {"name": "John", "age": 20, "grade": "A"}
print("Student Name:", student["name"])
print("Student Age:", student["age"])
Student Name: John
Student Age: 20

#Exercise 3: Modifying Values
#Change the grade of the student to “B”.

1
2
3
4
# dictionaries exercises python
student = {"name": "John", "age": 20, "grade": "A"}
student["grade"] = "B"
print(student)
{'name': 'John', 'age': 20, 'grade': 'B'}

#Exercise 4: Adding Key-Value Pairs
#Add a new key-value pair to the student dictionary for “city” with the value “Mumbai.”

1
2
3
4
# dictionaries exercises python
student = {"name": "John", "age": 20, "grade": "A"}
student["city"] = "Mumbai"
print(student)
{'name': 'John', 'age': 20, 'grade': 'A', 'city': 'Mumbai'}
#Exercise 5: Deleting Key-Value Pairs
#Remove the “grade” key and its corresponding value from the student dictionary.

1
2
3
4
# dictionaries exercises python
student = {'name': 'John', 'age': 20, 'grade': 'A', 'city': 'Mumbai'}
del student["grade"]
print(student)
{'name': 'John', 'age': 20, 'city': 'Mumbai'}

#Exercise 6: Checking if a Key Exists
#Write code to check if the “age” key exists in the student dictionary. Print “Age key exists” if it does; otherwise, print “Age key does not exist.”

1
2
3
4
5
6
7
# dictionaries exercises python
student = {'name': 'John', 'age': 20, 'grade': 'A', 'city': 'Mumbai'}
 
if "age" in student:
    print("Age key exists")
else:
    print("Age key does not exist")
Age key exists

#Exercise 7: Iterating Through a Dictionary
#In this Python exercises of dictionaries write code to iterate through the student dictionary and print all the key-value pairs.

1
2
3
4
5
# dictionaries exercises python
student = {'name': 'John', 'age': 20, 'grade': 'A', 'city': 'Mumbai'}
 
for key, value in student.items():
    print(key, ":", value)
name : John
age : 20
grade : A
city : Mumbai

#Exercise 8: Merging Dictionaries
#Create two dictionaries, dict1 and dict2, with some key-value pairs. Merge these dictionaries into a new dictionary called merged_dict.

1
2
3
4
5
6
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
 
merged_dict = {**dict1, **dict2}
 
print(merged_dict)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

#Exercise 9: Summing Values
#In this Python practice exercise create a dictionary expenses with different categories as keys (e.g., “food,” “rent,” “transport”) and their corresponding expenses as values. Write code to calculate and print the total expenses.

1
2
3
4
5
# python dictionaries exercises problem solution
expenses = {"food": 200, "rent": 1000, "transport": 150, "entertainment": 50}
 
total_expenses = sum(expenses.values())
print("Total expenses:", total_expenses)
Total expenses: 1400

#Exercise 10: Dictionary Comprehension
#Create a dictionary called squared_numbers that contains the squares of numbers from 1 to 10 using dictionary comprehension.

1
2
squared_numbers = {x: x**2 for x in range(1, 11)}
print(squared_numbers)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

#Exercise 11: Nested Dictionaries
#Create a nested dictionary called student_records with information about multiple students. Each student should have a unique student ID as the key and a dictionary of attributes (e.g., name, age, grade) as the value.

1
2
3
4
5
6
student_records = {
    101: {"name": "Alice", "age": 19, "grade": "A"},
    102: {"name": "Bob", "age": 20, "grade": "B"},
    103: {"name": "Charlie", "age": 18, "grade": "A"},
}
print(student_records)
{101: {'name': 'Alice', 'age': 19, 'grade': 'A'}, 102: {'name': 'Bob', 'age': 20, 'grade': 'B'}, 103: {'name': 'Charlie', 'age': 18, 'grade': 'A'}}

#Exercise 12: Converting Lists to a Dictionary
#Create two lists, keys and values, and write code to create a dictionary where elements from the keys list become keys and elements from the values list become values.

1
2
3
4
5
keys = ["name", "age", "city"]
values = ["John", 25, "New York"]
 
new_dict = dict(zip(keys, values))
print(new_dict)
{'name': 'John', 'age': 25, 'city': 'New York'}
