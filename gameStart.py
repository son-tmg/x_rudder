import Game, Player, Token

if __name__ == "__main__":
    startState = False
    Players = []
    rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

    print("----------------------------------------------------------------------------------------------------")
    print("Welcome to the 2-player game called X-Rudder.\n")

    while startState == False:
        gameMode = input("Which mode would you like to play? (1-Player vs Player, 2-Player vs AI): ")

        if gameMode == "1":
            startState = True

            Player1Name = input("\n\nWelcome Player 1, please enter your name: ")
            Player1 = Player.Player(Player1Name, "\u2588   ")
            Players.append(Player1)

            Player2Name = input("\nWelcome Player 2, please enter your name: ")
            Player2 = Player.Player(Player2Name, "\u2591   ")
            Players.append(Player2)

            print("\n")

            for i in Players:
                i.InitializeTokenList()
                print("\nWelcome", i.get_playerName(), ", you will be playing in the token colour", i.get_playerColour().strip(), ", with the starting amount of", i.get_nbTokens(), "tokens.")

            print("\n\n\n-------------------------------------------------- Starting a new game session. --------------------------------------------------\n")
            newGame = Game.Game(Players)
            print("\n\n", newGame.printGameGrid())

            while not newGame.getgameFinished():
                for i in Players:
                    turnType, Position1, Position2 = "", "", ""
                    while turnType != ("1" or "2"):
                        turnType = input("\n\n" + (i.get_playerName() + ", it is your turn to play. Would you like to make a placement or a movement of a token? (1-Placement, 2-Movement): "))

                    if turnType == "1":
                        placementPosition = []
                        while Position1 not in rows:
                            Position1 = input("\nPlease pick which row you would like to place your token in (Select from 1 to 10): ")
                        placementPosition.append(10 - int(Position1))
                        while Position2 not in columns:
                            Position2 = input("\nPlease pick which column you would like to place your token in (Select from A to L): ").lower()
                        Position2 = ord(Position2.lower()) - 97
                        placementPosition.append(Position2)
                        i.placeToken(newGame, i.get_playerTokens(), placementPosition)

                    elif turnType == "2":
                        movementPosition = []




        elif gameMode == "2":
            startState = True
            print("\nNOT IMPLEMENTED YET. GOODBYE.")

        else:
            print("\nInvalid Option. Please try again.\n")