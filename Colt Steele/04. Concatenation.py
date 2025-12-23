username = "kfmd"
username += " 19" #nambahin value username tanpa edit
combat_class = "Warrior"

level = "97"

print(f"Welcome to the game, {username} \n Your current status is {combat_class} Level {level} \n")

online_players = 1000
online_players -= 100
print(f"Currently, there are {online_players} players playing the game")
print(f"Currently, there are {online_players + 300} players playing the game")


#Using .format()
first = "Venus"
last = "Williams"
formatted = "First Name: {}, Last Name: {}".format(first, last)

#Using f-strings, I think it's a much nicer syntax:
first = "Venus"
last = "Williams"
formatted = f"First Name: {first}, Last Name: {last}"