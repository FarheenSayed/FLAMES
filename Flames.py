'''Flames is popular game named after the acronym Friends, Lovers, Affectionate, Marriage, Enemies and Siblings. 
This game doesnot accurately predict whether or not an individual is right for you.
There are few steps in the game
* Take 2 names
* Remove the common characters
* Get the count of characters that are left
* Take Flames letter F,L,A,M,E,S
* Start removing the letters using the count we got
* The letter which lasts the process is the result

INPUT FORMAT: The input should be of 2 lines Player1name, Player2name
OUTPUT FORMAT: status is (result)
take input from user'''


def flames_game(player1name, player2name):
    # Convert names to lowercase and remove spaces
    player1name = player1name.lower().replace(" ", "")
    player2name = player2name.lower().replace(" ", "")

    # Remove common characters
    common_chars = set(player1name) & set(player2name)
    for char in common_chars:
        player1name = player1name.replace(char, "")
        player2name = player2name.replace(char, "")

    # Get the count of characters left
    count = len(player1name) + len(player2name)

    # Initialize Flames letters
    flames = ["F", "L", "A", "M", "E", "S"]

    # Start removing letters using the count
    index = 0
    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)

    # The last letter is the result
    result = flames[0]

    # Map the result to the corresponding status
    status_map = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affectionate",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }

    return status_map[result]

# Take input from user
player1name = input("Enter Player 1 name: ")
player2name = input("Enter Player 2 name: ")

# Play the game and print the result
result = flames_game(player1name, player2name)
print("Status is:", result)