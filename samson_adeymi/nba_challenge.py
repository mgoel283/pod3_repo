print("Challenge 2.1:")
jamal_murray_3pts_made = 46
Fred_VanVleet_3pts_made = 43
james_harden_3pts_made = 37
print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"in the 2020 NBA playoffs, Fred_VanVleet made {Fred_VanVleet_3pts_made} 3 point shots")
print(f"in the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 points shots")


print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_attempts = 93
Fred_VanVleet_3pts_attempts = 110
james_harden_3pts_attempts =109
print()

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {jamal_murray_3pts_attempts} attempts")
print(f"in the 2020 NBA playoffs, Fred VanVleet made {Fred_VanVleet_3pts_made} 3 point shots and {Fred_VanVleet_3pts_attempts} attempts")
print(f"in the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 points shots and {james_harden_3pts_attempts} attempts")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
print(f"Jamal Murray three point percentages {jamal_murray_3pts_made/jamal_murray_3pts_attempts}")
print(f"Fred VanVleet three point percentages {Fred_VanVleet_3pts_made/Fred_VanVleet_3pts_attempts}")
print(f"James Harden three point percentages {james_harden_3pts_made/james_harden_3pts_attempts}")
print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
sentance = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \n Those three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case
print(sentance)
print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers
lakers_are_best = ("true")
print(f"the lakers are the best team. {lakers_are_best}")
print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
lakers_are_best = 6
print(lakers_are_best)
# TODO: Convert your `lakers_are best` variable to a float, and print it out
lakers_are_best = 6.1
print(lakers_are_best)
print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
print("Jamal Murray three point percentages is fortynine percent")
print("Fred VanVleet three point percentages is thirtynine percent")
print("James Harden three point percentages is thirtythree percent")
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print("Jamal Murray three point percentages is 49")
print("Fred VanVleet three point percentages is 39")
print("James Harden three point percentages is 33")