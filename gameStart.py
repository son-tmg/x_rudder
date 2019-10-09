import Game, Player, Token
from Player import Player
if __name__ == "__main__":
    startState = False
    Players = []

    print("----------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------")
    print("Welcome to the 2-player game called X-Rudder.\n")

    while startState == False:
        gameMode = input("Which mode would you like to play? (1-Player vs Player, 2-Player vs AI): ")

        if gameMode == "1":
            startState = True

            Player1Name = input("\nWelcome Player 1, please enter your name: ")
            Player1 = Player(Player1Name, "\u2588")
            Players.append(Player1)

            Player2Name = input("\nWelcome Player 2, please enter your name: ")
            Player2 = Player(Player2Name, "\u2591")
            Players.append(Player2)

            for i in Players:
                i.InitializeTokenList()
                print("\n", i.get_playerName(), i.get_playerColour(), i.get_playerTokens(), i.get_nbTokens())

            print("\nStarting a new game session.")
            #newGame = Game()

        elif gameMode == "2":
            startState = True
            print("\nNOT IMPLEMENTED YET. GOODBYE.")

        else:
            print("\nInvalid Option. Please try again.\n")