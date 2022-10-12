import random

while True:
    choices = ["sten","sax","påse"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("sten, sax, eller påse?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Oavgjort.")
    elif player == "sten":
        if computer == "påse":
            print("computer: ", computer )
            print("player :", player)
            print("Du förlorade... :(")
        if computer == "sax":
            print("computer: ", computer)
            print("player: ", player)
            print("Du vann!")
    elif player == "sax":
        if computer == "påse":
            print("computer: ", computer )
            print("player :", player)
            print("Du vann!")
        if computer == "sten":
            print("computer: ", computer)
            print("player: ", player)
            print("Du förlorade... :(")
    elif player == "påse":
        if computer == "sten":
            print("computer: ", computer )
            print("player :", player)
            print("Du vann!")
        if computer == "sax":
            print("computer: ", computer)
            print("player: ", player)
            print("Du förlorade... :(")

    play_again = input("Spela en gång till? (ja/nej): ").lower()

    if play_again != "ja":
         break

print("Hejdå!")