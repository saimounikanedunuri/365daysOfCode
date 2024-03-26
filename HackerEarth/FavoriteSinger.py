Problem
-------
Bob has a playlist of 
 songs, each song has a singer associated with it (denoted by an integer)

Favourite singer of Bob is the one whose songs are the most on the playlist

Count the number of Favourite Singers of Bob

Input Format 

The first line contains an integer 
, denoting the number of songs in Bob's playlist.

The following input contains 
 integers, 
 integer denoting the singer of the 
 song.

Output Format

Output a single integer, the number of favourite singers of Bob

Note: Use 64 bit data type


Solution:
---------
my_list = [1, 3, 5, 5, 5, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    counts = {}
    max_count = 0
    recurring_number = None

    for num in my_list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        
        if counts[num] > max_count:
            max_count = counts[num]
            recurring_number = num
        elif counts[num] == max_count and num > recurring_number:
            recurring_number = num
    
    print(recurring_number)
