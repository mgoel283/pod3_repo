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
x = sorted(my_friends)
print(x)
print(f' this is my source, https://www.w3schools.com/python/ref_func_sorted.asp')
# 1B. Comment your code in 1A to convince yourself you understand how it works
# i basically used a function in python called sorted. which sorted the order of my list

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

print(my_account.keys())
print(f'i used this https://www.codegrepper.com/code-examples/python/extract+keys+from+dictionary+python my source')
# 2B. Comment your code in 2A to convince yourself you understand how it works

# well the function keys exsisted in python already. it took no parameter so all i had to do was add the comand to my dictionary and print it.

# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'

n = my_string.count('wood')
print(n)

# 3B. Comment your code in 3A to convince yourself you understand how it works
# well i had to assign a veriable that included the count function and the word i was looking for in my paramaters, and then print that the new veriable 


# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']

z = my_list.count('banana')
print(z)
# 4B. Comment your code in 4A to convince yourself you understand how it works

# i essentially did the same thing i did in question 4a

# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')
list_set = set(my_list)

print(list_set)

# 5B. Comment your code in 5A to convince yourself you understand how it works
#  assign a veriable that included the set function and printed that veriable
print(f'i used this https://www.geeksforgeeks.org/python-get-unique-values-list/#:~:text=Using%20set()%20property%20of,a%20list%20to%20print%20it my source')

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')
import numpy as np

rand_num = np.random.normal(0,1)

print(rand_num)

(f'i used this https://www.w3resource.com/python-exercises/numpy/basic/numpy-basic-exercise-17.php my source')

# 6B. Comment your code in 6A to convince yourself you understand how it works
# so by importing numpy i was able to use the np.random function and also use normal which i found out uses the normal distrubition of numbers. i set the limitations of my random number in my paramiters and them printed rand_num which i assigned to my equation.

(f'i used this https://www.w3resource.com/python-exercises/numpy/basic/numpy-basic-exercise-17.php my source')

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
