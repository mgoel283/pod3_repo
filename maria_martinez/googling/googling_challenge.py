'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
#https://www.geeksforgeeks.org/python-how-to-sort-a-list-of-strings/
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
my_friends.sort()
print(my_friends)

# 1B. Comment your code in 1A to convince yourself you understand how it works
# https://www.programiz.com/python-programming/methods/list/sort
#sort() Parameters
# By default, sort() doesn't require any extra parameters. However, it has two optional parameters:

# reverse - If True, the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison
# Return value from sort()
# The sort() method doesn't return any value. Rather, it changes the original list.

# If you want a function to return the sorted list rather than change the original list, use sorted().

# Example 1: Sort a given list
# # vowels list
# vowels = ['e', 'a', 'u', 'o', 'i']

# # sort the vowels
# vowels.sort()

# # print vowels
# print('Sorted list:', vowels)
# Output

# Sorted list: ['a', 'e', 'i', 'o', 'u']
# Sort in Descending order
# The sort() method accepts a reverse parameter as an optional argument.

# Setting reverse = True sorts the list in the descending order.

# list.sort(reverse=True)
# Alternately for sorted(), you can use the following code.

# sorted(list, reverse=True) 

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')
#https://www.programiz.com/python-programming/methods/dictionary/keys
my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

print (my_account.keys())

# 2B. Comment your code in 2A to convince yourself you understand how it works
#works the same way as Object.key() in javascript
#it just takes the keys inside the dictonary and create an array of them


# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'
#https://stackoverflow.com/questions/17268958/finding-occurrences-of-a-word-in-a-string-in-python-3
result = my_string.count('wood')
print(result)
# 3B. Comment your code in 3A to convince yourself you understand how it works
#https://www.programiz.com/python-programming/methods/string/count
#count() method returns the number of occurrences of the substring in the given string.



# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
result = my_list.count('banana')
print(result)

# 4B. Comment your code in 4A to convince yourself you understand how it works
#https://www.programiz.com/python-programming/methods/list/count
#count() Parameters
# The count() method takes a single argument:
# element - the element to be counted
# Return value from count()
# The count() method returns the number of times element appears in the list.

# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')
#https://www.geeksforgeeks.org/python-get-unique-values-list/
result = list(set(my_list))
print(result)
# 5B. Comment your code in 5A to convince yourself you understand how it works
#Using set() property of Python, we can easily check for the unique values. Insert the values of the list in a set. Set only stores a value once even if it is inserted more then once. After inserting all the values in the set by list_set=set(list1), convert this set to a list to print it. 

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')
#https://www.w3schools.com/python/numpy_random.asp
from numpy import random
number = random.randint(0,1)
print(number)

# 6B. Comment your code in 6A to convince yourself you understand how it works
#I am not sure if the parameters are right because everytime i run the code it only produces 0
# but from what i read in the geeks for geeks article it should also draw a 1

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
