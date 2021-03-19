'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
my_friends.sort()
print(my_friends)
#https://www.geeksforgeeks.org/python-how-to-sort-a-list-of-strings/


# 1B. Comment your code in 1A to convince yourself you understand how it works

#my_friends.sort()function alphabetized the list by sorting it
#print_(my_friend printed the newly sorted list)

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}
print(my_account.keys())

#https://www.geeksforgeeks.org/python-dictionary-keys-method/


# 2B. Comment your code in 2A to convince yourself you understand how it works

#adding.keys()function to the print statement specified to only print the key )


# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'
substring = 'wood'
#created a substring from the main string that contains only 'wood'
count = my_string.count(substring)
#counted that substring, meaning, counted how many times "wood" appeared
print('The count is:', count)
#print the results

#https://www.programiz.com/python-programming/methods/string/count



# 3B. Comment your code in 3A to convince yourself you understand how it works


# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
occurences = my_list.count('banana')
# counts how many times 'banana" is located in the list my_list
print(occurences)

# https://www.kite.com/python/answers/how-to-count-the-number-of-occurrences-of-an-element-in-a-list-in-python#:~:text=of%20%22b%22%20.-,Use%20list.,number%20of%20occurrences%20of%20value%20.


# 4B. Comment your code in 4A to convince yourself you understand how it works


# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
unique_strings = list(set(my_list))
# unique_list creates a set of strings that are only used once in the list
print(unique_strings)

# https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/


# 5B. Comment your code in 5A to convince yourself you understand how it works


# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')
import numpy
#imports numpy
import random
#imports random function

print(random.randint(0,1))
#use print function to grab a random interger between the set parameters

# https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9/40993111





'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
