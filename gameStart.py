import Game,Player,Token

if __name__ == "__main__":
    print("Welcome to X-rudder.")

    gameMode = input("Which mode would you like to play? : 1- Manual 2-CPU 3-A")

    if gameMode == "1":
        players = []

        player1 = Player("Black")
        player1Name = input("Player1 enter your name: ")

        player2 = Player("Red")
        player2Name = input("Player2 enter your name: ")

        print("Starting a new game session.")
        newGame = Game()
        players.append(player1,player2)
