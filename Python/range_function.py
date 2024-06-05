1. Basic Usage:
Code:
for i inrange(5): 
 print(i)

Output:
0 
1
2 
3 
4

2. Custom Start and Stop:
Code:
list(range(5, 10))

Output:
[5, 6, 7, 8, 9]

3. Custom Step:
list(range(0, 10, 3))

Output:
[0, 3, 6, 9]

4. Negative Step:
Code:
list(range(-10, -100, -30))

Output:
[-10, -40, -70]

5. Iterating Over Indices:
Code:
a = ['Mary', 'had', 'a', 'little', 'lamb'] 
for i inrange(len(a)): 
 print(i, a[i])

Output:
0 Mary 
1 had 
2 a
3 little 
4 lamb

