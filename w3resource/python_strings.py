Question:
--------
Python: Get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself

Code:
----
str="restart"
# print(str)
str1=""
count=0
for i in str:
  # print(i)
  if i not in str1:
    # print("yes")
    str1+=i

  else:
    print(i)
    # str1[i]='$'
    # print(str1)
    str=str.replace(i,"$")
    # count+=1
    # if count>1:
    #   break
print(str)
# print(str1)


str1='restart'   
char = str1[0]
str1 = str1.replace(char, '$')
str1 = char + str1[1:]
print(str1)


Question:
--------
Python: Get a string made of the first 2 and the last 2 chars from a given a string
Code:
-----
str="w3resource"
#print(str)
length=len(str)
#print(length)
count1=2
str1=""
if length<2:
  print("empty string")
else:
  #print("continue")
  for i in str:
    str1+=i
    count1=count1-1
    if count1==0:
      break
  #print(str1)
# rev=reversed(str)
# print(type(rev))

str2=str[-2:]
print(str1+str2)
# res=str1+str2
# print(res)
  # for i in str:
  #   str1+=i
  #   count1=count1-1
  #   if count1==0:
  #     break
  # print(str1)

Question:
--------
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
Code:
-----
str="google"
li=""
count=0
# for i in str:
#   if i in li:
#     # li+='a'
#     # print(li)
#     print("if",li)
#   else:
#     li+=i
#     print("else",li)
  
  
# for i in str:
#   if 'g' in str:
#     count+=1
# print('g count',count)
# print(str)

for i in str:
  continue
print(i,'count',str.count(i))
