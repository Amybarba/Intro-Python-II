from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player(input("Welcome, enter your hero name: "), room['outside'])
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
print(f"{newPlayer.name} begins the journey in the {newPlayer.current_room}")
while True:
    current_room = newPlayer.current_room
    print(current_room.name)
    print(current_room.description)
    command = input("Please begin your journey,\n enter n, s, e, w, to navigate or q to quit game")

# If the user enters "q", quit the game.
    if command == "q":
        break
    # * Waits for user input and decides what to do.
    # If the user enters a cardinal direction, attempt to move to the room there.

    elif command == "n":
        newPlayer.current_room = newPlayer.current_room.n_to
    elif command == "s":
        newPlayer.current_room = newPlayer.current_room.s_to
    elif command == "e":
        newPlayer.current_room = newPlayer.current_room.e_to
    elif command == "w":
        newPlayer.current_room = newPlayer.current_room.w_to

# Print an error message if the movement isn't allowed.
    else:
        print("Unauthorized command")
