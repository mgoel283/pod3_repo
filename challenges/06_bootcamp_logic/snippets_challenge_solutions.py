print("Challenge 3.1: Debug code snippets")

print()

print("Code Snippet 1:")

u = 5
v = 2

# '=' is the assignment operator; '==' is the comparison operator
if u * v == 10:
    print(f"The product of u ({u}) and v ({v}) is 10")
else:
    print(f"The product of u ({u}) and v ({v}) is not 10")

print()

print("Code Snippet 2:")
x = 15
y = 25

z = 30

if z < x:
    print(f"z ({z}) is less than x ({x})")

# Missing the semicolon after the elif condition
elif z > x and z < y:
    print(f"z ({z}) is between x ({x}) and y ({y})")

# Missing the semicolon after else
else:
    print(f"z ({z}) is greater than y ({y})")


print()

print("Code Snippet 3:")

a = 1
b = 1
c = (a >= b)

# 1 is not greater than 1 hence modifying the comparison operator and print statement 
print(f"The value of c ({c}) is True since a ({a}) is greater than or equal to b ({b}).")
assert(c == True) #Do not change this line

print()

print("Code Snippet 4:")

d = (5 < 7) and not (8 < 20) 

# Change second 'or' to 'and' to make d evaluate to false
print("The value of d is False when we add an and operator between a False and True expression")
assert(d == False) #Do not change this line

print()


print("Code Snippet 5:")

m = "GOAT"
n = "goat"

o = (m != n)

# Python is case-sensitive so m and n are not equal
print (f"The value of o ({o}) is True since Python is case-sensitive.")
assert(o == True) #Do not change this line

print()
print("CHALLENGE COMPLETE!")