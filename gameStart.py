import Game,Player,Token

if __name__ == "__main__":
    startState = False
    Players = []

    print("--------------------------------------------------")
    print("Welcome to the 2-player game called X-Rudder.\n")

    while startState == False:
        gameMode = input("Which mode would you like to play? (1-Player vs Player, 2-Player vs AI): ")

        if gameMode == "1":
            startState = True

            Player1Name = input("Welcome Player 1, please enter your name: ")
            Player1 = Player(Player1Name, "u\u2588")

            Player2Name = input("Welcome Player 2, please enter your name: ")
            Player2 = Player(Player2Name, "u\u2591")

            print("Starting a new game session.")
            newGame = Game()
            players.append(player1,player2)

        elif gameMode == "2":
            startState = True
            print("\nNOT IMPLEMENTED YET. GOODBYE.")

        else:
            print("\nInvalid Option. Please try again.\n")