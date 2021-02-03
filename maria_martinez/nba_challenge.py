import math

print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
fredVanVleet = 43
# TODO: Create variable here for number of 3 pt shots made by James Harden
jamesHarden = 37
print('\n')

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fredVanVleet} 3 point shots")
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {jamesHarden} 3 point shots")
print('\n')

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
jamalMurray2020 = 93
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
fredVanVleet2020 = 110
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
jamesHarden2020= 109
print('\n')

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamalMurray2020} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet  made {fredVanVleet2020} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {jamesHarden2020} 3 point shots")
print('\n')

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
murrayAverage=math.ceil((jamal_murray_3pts_made/jamalMurray2020)*100)
# TODO: Calculate and print the 3 point percentage for Jamal Murray
VanVleetAverage=math.ceil((fredVanVleet/fredVanVleet2020)*100)
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
hardenAverage=math.ceil((jamesHarden/jamesHarden2020)*100)
# TODO: Calculate and print the 3 point percentage for James Harden
print(f"Murray's average {murrayAverage}%")
print(f"VanVleet's average {VanVleetAverage}%")
print(f"Harden's average {hardenAverage}%")
print('\n')

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print('The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. Those three have made good developments with the Pelicans, especially Brandon Ingram. But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. The Lakers ended the season atop the Western Conference with a record of 49-14. They were narrowly behind the Bucks for the best record in the league. Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.')
print('\n')

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case
message ="The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
print(message)
print('\n')

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
lakers_are_best = True
# TODO: print out the variable in an f-string to convey your opinion on the lakers
print(f"It is {lakers_are_best} that The Los Angeles Laker are best!")

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
print(int(lakers_are_best))
# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(float(lakers_are_best))
print('\n')

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
print(f"Murray's percentage in string form {str(murrayAverage)}")
print(f"VanVleet's percentage in string form {str(VanVleetAverage)}")
print(f"Harden's percentage in string form {str(hardenAverage)}")
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(f"Murray's percentage in int conversion form {int(murrayAverage)}")
print(f"VanVleet's percentage in int conversion form {int(VanVleetAverage)}")
print(f"Harden's percentage in int conversion form {int(hardenAverage)}")