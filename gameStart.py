import Game, Player, Token

if __name__ == "__main__":
    startState = False
    Players = []

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
                print("\nWelcome", i.get_playerName(), ", you will be playing in the token colour", i.get_playerColour(), ", with the starting amount of", i.get_nbTokens(), "tokens.")

            print("\n\n\n-------------------------------------------------- Starting a new game session. --------------------------------------------------\n")
            newGame = Game.Game(Players)
            print("\n\n", newGame.printGameGrid())

            Player1.placeToken(newGame, i.get_playerTokens(), [1,1])























        elif gameMode == "2":
            startState = True
            print("\nNOT IMPLEMENTED YET. GOODBYE.")

        else:
            print("\nInvalid Option. Please try again.\n")