print("Challenge 2.1:")

jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

jamal_murray_3pts_att = 93
fred_vanvleet_3pts_att = 110
james_harden_3pts_att = 109

print("Challenge 2.2:")

print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")

print()

print(f"In the 2020 NBA playoffs, Jamal Murray attempted {jamal_murray_3pts_att} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred Vanvleet attempted {fred_vanvleet_3pts_att} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden attempted {james_harden_3pts_att} 3 point shots")

print()

print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and attempted {jamal_murray_3pts_att} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred Vanvleet made {fred_vanvleet_3pts_made} 3 point shots and attempted {fred_vanvleet_3pts_att} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots and attempted {james_harden_3pts_att} 3 point shots")

print()

jamal_murray_3pts_per = jamal_murray_3pts_made/jamal_murray_3pts_att
fred_vanvleet_3pts_per = fred_vanvleet_3pts_made/fred_vanvleet_3pts_att
james_harden_3pts_per = james_harden_3pts_made/james_harden_3pts_att

print(f"Jamal Murray's 3 point percentage was {jamal_murray_3pts_per}")
print(f"Fred Vanvleet's 3 point percentage was {fred_vanvleet_3pts_per}")
print(f"James Harden's 3 point percentage was {james_harden_3pts_per}")

print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line

print('The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\n They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\n Those three have made good developments with the Pelicans, especially Brandon Ingram.\n But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\n Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\n The Lakers ended the season atop the Western Conference with a record of 49-14.\n They were narrowly behind the Bucks for the best record in the league.\n Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\n Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.')

print()

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case

message ='The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\n They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\n Those three have made good developments with the Pelicans, especially Brandon Ingram.\n But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\n Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\n The Lakers ended the season atop the Western Conference with a record of 49-14.\n They were narrowly behind the Bucks for the best record in the league.\n Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\n Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.'

print(message.upper())

print()

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this

lakers_are_best = False

# TODO: print out the variable in an f-string to convey your opinion on the lakers
print(f'Lakers suck! And the idea that they are the best is {lakers_are_best}.')

print()

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 

print(int(lakers_are_best))

print()

# TODO: Convert your `lakers_are best` variable to a float, and print it out

print(float(lakers_are_best))

print()

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.

print(str(jamal_murray_3pts_per))
print(str(fred_vanvleet_3pts_per))
print(str(james_harden_3pts_per))

print()

# comparing this vs. above - what is difference when adding "str" vs just "printing it". It's the same

print(f"{jamal_murray_3pts_per}")
print(f"{fred_vanvleet_3pts_per}")
print(f"{james_harden_3pts_per}")

print()

jm3 = jamal_murray_3pts_per
fv3 = fred_vanvleet_3pts_per
jh3 = james_harden_3pts_per

# comparing this vs. above - using f string

print(f"This is Jamal Murray's three point percentage {jm3}.")
print(f"This is Fred VanVleet's three point percentage {fv3}.")
print(f"This is James Harden's three point percentage {jh3}.")

print()

# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.

print(int(jamal_murray_3pts_per))
print(int(fred_vanvleet_3pts_per))
print(int(james_harden_3pts_per))
