import Game, Player, Token, Heuristic, math, random

if __name__ == "__main__":
    startState = False
    Players = []
    chosenToken, placementPosition, movementPosition, nbMoves = [], [], [], 0
    rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    CenterPosition = [[4,5],[4,6],[5,5],[5,6]]         #FOR NOW, START AI AT ONE OF THE 4 CENTER POSITIONS
    previousMove = []                                   #GETS THE PREVIOUS MOVE OF THE AI, TO START NEXT HEURISTIC SEARCH AT THE PREVIOUS MOVE
    possibleMoves = []                                  #LIST OF ALL THE POSSIBLE MOVES THE AI COULD DO THIS TURN

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
                    turnType, Position1, Position2, placementPosition, chosenToken, movementPosition = "", "", "", [], [], []

                    if len(Players[0].get_playerTokens()) == 0 and len(
                            Players[1].get_playerTokens()) == 0 and nbMoves >= 30:
                        newGame.setgameFinished(True)
                        print("The game ended as a tie.")
                        exit(1)

                    while turnType not in ["1", "2"]:
                        if len(i.get_playerTokens()) == 15:
                            turnType = "1"
                            print(i.get_playerName() + ", it is your turn to play.")
                            break
                        elif len(i.get_playerTokens()) == 0:
                            turnType = "2"
                            print(i.get_playerName() + ", it is your turn to play.")
                            break
                        turnType = input("\n\n" + (
                                    i.get_playerName() + ", it is your turn to play. Would you like to make a placement or a movement of a token? (1-Placement, 2-Movement): "))

                    if turnType == "1":
                        while len(placementPosition) == 0 or newGame.getGameGrid()[placementPosition[0]][
                            placementPosition[1]] is not None:
                            placementPosition, Position1, Position2 = [], "", ""
                            while Position1 not in rows:
                                Position1 = input(
                                    "\nPlease pick which row you would like to place your token in (Select from 1 to 10): ")
                            placementPosition.append(10 - int(Position1))
                            while Position2 not in columns:
                                Position2 = input(
                                    "\nPlease pick which column you would like to place your token in (Select from A to L): ").lower()
                            Position2 = ord(Position2.lower()) - 97
                            placementPosition.append(Position2)
                            if newGame.getGameGrid()[placementPosition[0]][placementPosition[1]] is not None:
                                print(
                                    "\nYour token could not be placed at the specified coordinate. Please re-enter the coordinate of the position you would like to move your token.")
                        i.placeToken(newGame, i.get_playerTokens(), placementPosition)
                        i.set_nbTokens(len(i.get_playerTokens()))

                    elif turnType == "2":
                        nbMoves += 1
                        print("\nYou will now input the coordinates of the Token you would like to have moved.")
                        while len(chosenToken) == 0 or newGame.getGameGrid()[chosenToken[0]][chosenToken[1]] is None or \
                                newGame.getGameGrid()[chosenToken[0]][
                                    chosenToken[1]].get_tokenColour() != i.get_playerColour():
                            Position1, Position2, chosenToken, movementPosition = "", "", [], []
                            while Position1 not in rows:
                                Position1 = input(
                                    "\nPlease pick which token you would like to move by specifying the row it is in (Select from 1 to 10): ")
                            chosenToken.append(10 - int(Position1))
                            while Position2 not in columns:
                                Position2 = input(
                                    "\nPlease pick which token you would like to move by specifying the column it is in (Select from A to L): ").lower()
                            Position2 = ord(Position2.lower()) - 97
                            chosenToken.append(Position2)
                            if newGame.getGameGrid()[chosenToken[0]][chosenToken[1]] is None or \
                                    newGame.getGameGrid()[chosenToken[0]][
                                        chosenToken[1]].get_tokenColour() != i.get_playerColour():
                                print(
                                    "\nYour token could not be found at the specified coordinate. Please re-enter the coordinate of the token you would like to move.")

                        print(
                            "\nYou will now input the coordinates of the position you would like to move your specified token to. You can only move 1 square from your current position.")
                        while len(movementPosition) == 0 or newGame.getGameGrid()[movementPosition[0]][
                            movementPosition[1]] is not None or \
                                (not (0 <= movementPosition[0] <= 9) and not (0 <= movementPosition[1] <= 11)) or \
                                math.sqrt(pow((movementPosition[0] - chosenToken[0]), 2) + pow(
                                    (movementPosition[1] - chosenToken[1]), 2)) != 1:

                            Position1, Position2, movementPosition = "", "", []
                            while Position1 not in rows:
                                Position1 = input(
                                    "\nPlease pick which row you would like to move your token in (Select from 1 to 10): ")
                            movementPosition.append(10 - int(Position1))
                            while Position2 not in columns:
                                Position2 = input(
                                    "\nPlease pick which column you would like to move your token in (Select from A to L): ").lower()
                            Position2 = ord(Position2.lower()) - 97
                            movementPosition.append(Position2)

                        """find surrounding tokens to chosenToken's old position and check if by moving there is a winning configuration.
                            for any tokens that are within a 1 radius distance from chosenToken, call checkstate() on them
                        """

                        neighbourTokenPositions = []  # contains neighbour token positions
                        neighbourOppositeTokens = []  # contains neighbour tokens that are opposite to current player's colour

                        left = [chosenToken[0], chosenToken[1] - 1]
                        right = [chosenToken[0], chosenToken[1] + 1]
                        top = [chosenToken[0] - 1, chosenToken[1]]
                        bottom = [chosenToken[0] + 1, chosenToken[1]]
                        topLeft = [chosenToken[0] - 1, chosenToken[1] - 1]
                        topRight = [chosenToken[0] - 1, chosenToken[1] + 1]
                        bottomLeft = [chosenToken[0] + 1, chosenToken[1] - 1]
                        bottomRight = [chosenToken[0] + 1, chosenToken[1] + 1]

                        neighbourTokenPositions.extend(
                            [left, right, top, bottom, topLeft, topRight, bottomLeft, bottomRight])

                        for tokenPosition in neighbourTokenPositions:
                            if 0 < tokenPosition[0] < 9 and 0 < tokenPosition[1] < 11 and \
                                    newGame.getGameGrid()[tokenPosition[0]][tokenPosition[1]] != None:
                                if newGame.getGameGrid()[tokenPosition[0]][
                                    tokenPosition[1]].get_tokenColour() != i.get_playerColour():
                                    neighbourOppositeTokens.append(
                                        newGame.getGameGrid()[tokenPosition[0]][tokenPosition[1]])

                        tempToken = Token.Token(i.get_playerColour(), [chosenToken[0], chosenToken[
                            1]])  # make a copy of the token to be moved
                        newGame.getGameGrid()[chosenToken[0]][chosenToken[
                            1]] = None  # set token at old position to None, so that we can see if any neighbours get winning configuration

                        for token in neighbourOppositeTokens:
                            newGame.checkState(token)
                            if newGame.getgameFinished():

                                if i == Players[0]:
                                    i = Players[1]
                                    print("Player " + i.get_playerName() + " won.")
                                else:
                                    i = Players[0]
                                    print("Player " + i.get_playerName() + " won.")

                                print("\nThe game has ended.")
                                break

                        newGame.getGameGrid()[chosenToken[0]][chosenToken[
                            1]] = tempToken  # bring back moved token to old position so that it may be moved later

                        i.moveToken(newGame, chosenToken, movementPosition)

                    if newGame.getgameFinished():
                        print("Player " + i.get_playerName() + " won.")
                        break

        elif gameMode == "2":
            startState = True

            print("\n\nWelcome Player 1, as an artificially intelligent agent, your name will be AI. ")
            Player1 = Player.Player("AI", "\u2588   ")
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
                    turnType, Position1, Position2, placementPosition, chosenToken, movementPosition = "", "", "", [], [], []

                    if len(Players[0].get_playerTokens()) == 0 and len(
                            Players[1].get_playerTokens()) == 0 and nbMoves >= 30:
                        newGame.setgameFinished(True)
                        print("The game ended as a tie.")
                        exit(1)

                    if i == newGame.getPlayers()[0]:
                        print("It is the artificial intelligent agent's turn to play now.")
                        if len(i.get_playerTokens()) != 0:
                            if len(i.get_playerTokens()) == 15:
                                previousMove = CenterPosition[random.randrange(0,4)]

                                print("AI is going to place at :", previousMove)

                                i.placeToken(newGame, i.get_playerTokens(), previousMove)
                                i.set_nbTokens(len(i.get_playerTokens()))

                            else:
                                possibleMoves = Heuristic.Heuristic.searchList(newGame, previousMove, 1)
                                toRemove = []

                                print("Ai found these moves : ", possibleMoves)

                                for move in possibleMoves:
                                    print("State of position: ", move , " - " , newGame.getGameGrid()[move[0]][move[1]], " - ", newGame.getGameGrid()[move[0]][move[1]] is not None)

                                for move in possibleMoves:
                                    print("Check if it has to be removed ", move, " - ", newGame.getGameGrid()[move[0]][move[1]] is not None)
                                    if newGame.getGameGrid()[move[0]][move[1]] is not None:
                                        toRemove.append(move)
                                
                                for move in toRemove:
                                    possibleMoves.remove(move)

                                print("These moves are remaining: ", possibleMoves)

                                previousMove = possibleMoves[random.randrange(0,(len(possibleMoves)))]

                                print("AI is going to place at :", previousMove)


                                i.placeToken(newGame, i.get_playerTokens(), previousMove)
                                i.set_nbTokens(len(i.get_playerTokens()))
                        continue

                    while turnType not in ["1", "2"]:
                        if len(i.get_playerTokens()) == 15:
                            turnType = "1"
                            print(i.get_playerName() + ", it is your turn to play.")
                            break
                        elif len(i.get_playerTokens()) == 0:
                            turnType = "2"
                            print(i.get_playerName() + ", it is your turn to play.")
                            break
                        turnType = input("\n\n" + (
                                    i.get_playerName() + ", it is your turn to play. Would you like to make a placement or a movement of a token? (1-Placement, 2-Movement): "))

                    if turnType == "1":
                        while len(placementPosition) == 0 or newGame.getGameGrid()[placementPosition[0]][
                            placementPosition[1]] is not None:
                            placementPosition, Position1, Position2 = [], "", ""
                            while Position1 not in rows:
                                Position1 = input(
                                    "\nPlease pick which row you would like to place your token in (Select from 1 to 10): ")
                            placementPosition.append(10 - int(Position1))
                            while Position2 not in columns:
                                Position2 = input(
                                    "\nPlease pick which column you would like to place your token in (Select from A to L): ").lower()
                            Position2 = ord(Position2.lower()) - 97
                            placementPosition.append(Position2)
                            if newGame.getGameGrid()[placementPosition[0]][placementPosition[1]] is not None:
                                print(
                                    "\nYour token could not be placed at the specified coordinate. Please re-enter the coordinate of the position you would like to move your token.")
                        i.placeToken(newGame, i.get_playerTokens(), placementPosition)
                        i.set_nbTokens(len(i.get_playerTokens()))

                    elif turnType == "2":
                        nbMoves += 1
                        print("\nYou will now input the coordinates of the Token you would like to have moved.")
                        while len(chosenToken) == 0 or newGame.getGameGrid()[chosenToken[0]][chosenToken[1]] is None or \
                                newGame.getGameGrid()[chosenToken[0]][
                                    chosenToken[1]].get_tokenColour() != i.get_playerColour():
                            Position1, Position2, chosenToken, movementPosition = "", "", [], []
                            while Position1 not in rows:
                                Position1 = input(
                                    "\nPlease pick which token you would like to move by specifying the row it is in (Select from 1 to 10): ")
                            chosenToken.append(10 - int(Position1))
                            while Position2 not in columns:
                                Position2 = input(
                                    "\nPlease pick which token you would like to move by specifying the column it is in (Select from A to L): ").lower()
                            Position2 = ord(Position2.lower()) - 97
                            chosenToken.append(Position2)
                            if newGame.getGameGrid()[chosenToken[0]][chosenToken[1]] is None or \
                                    newGame.getGameGrid()[chosenToken[0]][
                                        chosenToken[1]].get_tokenColour() != i.get_playerColour():
                                print(
                                    "\nYour token could not be found at the specified coordinate. Please re-enter the coordinate of the token you would like to move.")

                        print(
                            "\nYou will now input the coordinates of the position you would like to move your specified token to. You can only move 1 square from your current position.")
                        while len(movementPosition) == 0 or newGame.getGameGrid()[movementPosition[0]][
                            movementPosition[1]] is not None or \
                                (not (0 <= movementPosition[0] <= 9) and not (0 <= movementPosition[1] <= 11)) or \
                                math.sqrt(pow((movementPosition[0] - chosenToken[0]), 2) + pow(
                                    (movementPosition[1] - chosenToken[1]), 2)) != 1:

                            Position1, Position2, movementPosition = "", "", []
                            while Position1 not in rows:
                                Position1 = input(
                                    "\nPlease pick which row you would like to move your token in (Select from 1 to 10): ")
                            movementPosition.append(10 - int(Position1))
                            while Position2 not in columns:
                                Position2 = input(
                                    "\nPlease pick which column you would like to move your token in (Select from A to L): ").lower()
                            Position2 = ord(Position2.lower()) - 97
                            movementPosition.append(Position2)

                        """find surrounding tokens to chosenToken's old position and check if by moving there is a winning configuration.
                            for any tokens that are within a 1 radius distance from chosenToken, call checkstate() on them
                        """

                        neighbourTokenPositions = []  # contains neighbour token positions
                        neighbourOppositeTokens = []  # contains neighbour tokens that are opposite to current player's colour

                        left = [chosenToken[0], chosenToken[1] - 1]
                        right = [chosenToken[0], chosenToken[1] + 1]
                        top = [chosenToken[0] - 1, chosenToken[1]]
                        bottom = [chosenToken[0] + 1, chosenToken[1]]
                        topLeft = [chosenToken[0] - 1, chosenToken[1] - 1]
                        topRight = [chosenToken[0] - 1, chosenToken[1] + 1]
                        bottomLeft = [chosenToken[0] + 1, chosenToken[1] - 1]
                        bottomRight = [chosenToken[0] + 1, chosenToken[1] + 1]

                        neighbourTokenPositions.extend(
                            [left, right, top, bottom, topLeft, topRight, bottomLeft, bottomRight])

                        for tokenPosition in neighbourTokenPositions:
                            if 0 < tokenPosition[0] < 9 and 0 < tokenPosition[1] < 11 and \
                                    newGame.getGameGrid()[tokenPosition[0]][tokenPosition[1]] != None:
                                if newGame.getGameGrid()[tokenPosition[0]][
                                    tokenPosition[1]].get_tokenColour() != i.get_playerColour():
                                    neighbourOppositeTokens.append(
                                        newGame.getGameGrid()[tokenPosition[0]][tokenPosition[1]])

                        tempToken = Token.Token(i.get_playerColour(), [chosenToken[0], chosenToken[
                            1]])  # make a copy of the token to be moved
                        newGame.getGameGrid()[chosenToken[0]][chosenToken[
                            1]] = None  # set token at old position to None, so that we can see if any neighbours get winning configuration

                        for token in neighbourOppositeTokens:
                            newGame.checkState(token)
                            if newGame.getgameFinished():

                                if i == Players[0]:
                                    i = Players[1]
                                    print("Player " + i.get_playerName() + " won.")
                                else:
                                    i = Players[0]
                                    print("Player " + i.get_playerName() + " won.")

                                print("\nThe game has ended.")
                                break

                        newGame.getGameGrid()[chosenToken[0]][chosenToken[
                            1]] = tempToken  # bring back moved token to old position so that it may be moved later

                        i.moveToken(newGame, chosenToken, movementPosition)

                    if newGame.getgameFinished():
                        print("Player " + i.get_playerName() + " won.")
                        break

        else:
            print("\nInvalid Option. Please try again.\n")