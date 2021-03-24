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

sorted_friends = sorted(my_friends) #I found the sorted function from the link below. I applied that function to my list "my_friends" & I created a new list "sorted_friends"

print(sorted_friends)
print()

# 1B. Comment your code in 1A to convince yourself you understand how it works

# https://stackoverflow.com/questions/14032521/python-data-structure-sort-list-alphabetically

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

for key, value in my_account.items(): 
	print(key, ' : ', value)
#I found this code from 2nd link below - & compared w/ first link. I liked 2nd option better. The dict.items() function will print each key value pairs on separate lines & the middle part determines what separates the two.

# 2B. Comment your code in 2A to convince yourself you understand how it works

# https://www.kite.com/python/answers/how-to-print-all-key-value-pairs-of-a-dictionary-in-python#
# https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/

print()

# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'

def return_count(string, word): # I found the count() function @ link below. It's counting var2 "word" in the var1 "string"
	return string.count(word)

wood_count = return_count(my_string, 'wood')

print(f"The word 'wood' shows up {wood_count} times!")

# 3B. Comment your code in 3A to convince yourself you understand how it works

# https://www.pythonpool.com/python-count-words-in-string/

print()

# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']

def fruit_count(string, word):
	return string.count(word) #same thought process as above

banana_count = fruit_count(my_list, 'banana')
print(f"The number of times the word 'banana' appears in the list is {banana_count} times!")


# 4B. Comment your code in 4A to convince yourself you understand how it works

# https://www.pythonpool.com/python-count-words-in-string/ - I used the same link & code from above

print()
# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')

for item in my_list: 
	print(item)

# used a for-loop to specifically print out each item from the list

# 5B. Comment your code in 5A to convince yourself you understand how it works

# https://www.kite.com/python/answers/how-to-print-items-in-a-list-on-separate-lines-in-python#

print()

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')

from numpy import random

my_random_number = random.rand(1)

print(my_random_number)

print()

print("using randint function:")


# 6B. Comment your code in 6A to convince yourself you understand how it works


'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
