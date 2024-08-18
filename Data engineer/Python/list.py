#What is a List?
#A list in Python is an ordered collection of elements enclosed in square brackets [ ]. Each element in a list can be of any data type, including numbers, strings, or even other lists. Lists are mutable, which means you can change their contents (add, remove, or modify elements) after they are created.


#Exercise 1: Creating a List
#Create a list named fruits containing the following fruits: “apple,” “banana,” “cherry,” and “date.”

1
fruits = ["apple", "banana", "cherry", "date"]

#Exercise 2: Accessing List Elements
#Access the second element (banana) from the fruits list. You know that Python starts the counting from 0. So second element in Python can be accessed through index 1.

1
2
3
4
5
# python lists exercises: Accessing List Elements
fruits = ["apple", "banana", "cherry", "date"]
 
second_fruit = fruits[1]
print(second_fruit)
banana

#Exercise 3: Modifying List Elements
#Replace “cherry” with “grape” in the fruits list.

1
2
3
4
# python exercises lists: Modifying List Elements
fruits = ["apple", "banana", "cherry", "date"]
fruits[2] = "grape"
print(fruits)
['apple', 'banana', 'grape', 'date']

#Exercise 4: Adding Elements to a List
Add “fig” to the end of the fruits list.

1
2
3
4
# lists in python exercises: Adding Elements to a List
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("fig")
print(fruits)
['apple', 'banana', 'cherry', 'date', 'fig']
Exercise 5: Removing Elements from a List
Remove “apple” from the fruits list.

1
2
3
4
# python lists and strings exercises: Removing Elements from a List
fruits = ["apple", "banana", "cherry", "date"]
fruits.remove("apple")
print(fruits)
['banana', 'cherry', 'date']

#Exercise 6: Checking if an Element Exists
#Check if “date” is in the fruits list.

1
2
3
4
5
6
7
# python lists and strings exercises: Checking if an Element Exists
fruits = ["apple", "banana", "cherry", "date"]
 
if "date" in fruits:
    print("Date is in the list.")
else:
    print("Date is not in the list.")

#Date is in the list.

#Exercise 7: Slicing a List
#Create a new list selected_fruits containing the first two elements of the fruits list.

1
2
3
4
5
# python lists and strings exercises: Slicing a List
fruits = ["apple", "banana", "cherry", "date"]
 
selected_fruits = fruits[:2]
print(selected_fruits)
['apple', 'banana']

#Exercise 8: Reversing a List
#Reverse the order of elements in the fruits list.

1
2
3
4
5
6
7
8
9
# lists in python exercises: Reversing a List
fruits = ["apple", "banana", "cherry", "date"]
 
# Method:1
fruits.reverse()
print(fruits)
 
# Method: 2
print(fruits[:])
['date', 'cherry', 'banana', 'apple']
['date', 'cherry', 'banana', 'apple']

#Exercise 9: Sorting a List
#Sort the fruits list in alphabetical order.

1
2
3
4
5
# sorted lists function python exercises
fruits = ["apple", "cherry", "banana", "date", "cherry"]
 
fruits.sort()
print(fruits)

#Output of sorted lists Python exercises:

['apple', 'banana', 'cherry', 'cherry', 'date']

#Exercise 10: Combining Lists
#Create a new list more_fruits containing “grape,” “kiwi,” and “melon,” then combine it with the fruits list. This is also called List Concatenation.

1
2
3
4
5
6
# python lists and strings exercises: Combining Lists
fruits = ["apple", "banana", "cherry", "date"]
 
more_fruits = ["grape", "kiwi", "melon"]
combined_fruits = fruits + more_fruits
print(combined_fruits)
['apple', 'banana', 'cherry', 'date', 'grape', 'kiwi', 'melon']

#Exercise 11: List Comprehensions
#Create a new list even_numbers containing the even numbers from 1 to 10.

1
2
3
# python exercises with for range lists: List Comprehensions
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)
[2, 4, 6, 8, 10]

#Exercise 12: Nested Lists Exercises
#Create a nested list called matrix that represents a 2×2 matrix.

1
2
3
# Create Nested List in Python exercises
matrix = [[1, 2], [3, 4]]
print(matrix)
[[1, 2], [3, 4]]

#Exercise 13: Lists Exercises with For Loop
#List Modification exercise in Python: Given a list numbers, double the value of each element in the list, this can be done using for loop.

1
2
3
4
# python exercises with for range lists
numbers = [2, 4, 6, 8]
doubled_numbers = [x * 2 for x in numbers]
print(doubled_numbers)
[4, 8, 12, 16]

#Exercise 14: List Filtering
#Given a list of numbers, numbers, create a new list even_numbers that contains only the even numbers from the original list.

1
2
3
4
# List filtering python exercise
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
[2, 4, 6, 8, 10]

#Exercise 15: List Filtering with Index
#Given a list numbers, create a new list odd_index_numbers that contains only the elements at odd indices (1st, 3rd, 5th, etc.) of the original list.

1
2
3
4
# List filtering python exercise
numbers = [10, 20, 30, 40, 50, 60]
odd_index_numbers = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]
print(odd_index_numbers)
[20, 40, 60]

#Exercise 16: List Splitting
#Split a given list my_list into two lists, first_half containing the first half of the elements and second_half containing the second half.

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
# List spliting python exercise
my_list = [1, 2, 3, 4, 5, 6]
 
mid_point = len(my_list) // 2
 
first_half = my_list[:mid_point]
second_half = my_list[mid_point:]
 
print(first_half)
print(second_half)
[1, 2, 3]
[4, 5, 6]

#Exercise 17: List Intersection
#Given two lists, list1 and list2, create a new list common_elements containing the elements that appear in both lists.

1
2
3
4
5
6
# Python Practice test: List intersection or common element in two list
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = [x for x in list1 if x in list2]
 
print(common_elements)
[3, 4, 5]

#Exercise 18: Flattening a List of Lists
#In this Python exercise, given a list of lists nested_list, flatten it into a single list flat_list.

1
2
3
4
# python list of lists exercises
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)
[1, 2, 3, 4, 5, 6, 7, 8]

#Exercise 19: List of Tuples
#Create a list of tuples, where each tuple represents a person’s name and age.

1
2
3
# lists and tuples python exercises
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(people)
[('Alice', 30), ('Bob', 25), ('Charlie', 35)]
