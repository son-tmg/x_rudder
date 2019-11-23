X-Rudder

To run the game, open a terminal and run the 'gameStart.py' file as such : 

"python3 gameStart.py"

Upon running the gameStart file, a prmopt will be asked to select one of the following 2 game modes : 1. Player vs. Player or 2. Player vs. AI . 
To select a mode, simply input 1 or 2 for the desired mode. 


1. Player vs Player : 

A prompt will ask for player 1 and player 2 name. Simply write the name of the player and press enter when done :

"Welcome Player 1, please enter your name:"

"Welcome Player 2, please enter your name:"

By default, player 1 will be the white token and player 2 will be the black token. 
The first turn will run and the gameGrid will be displayed, where 'None' means that a position in the gameGrid is unoccupied and a token may be placed by a player.
To place a token, the player will be prompted to enter a row number (between 1 and 10). If you enter an invalid input, you will be prompted again.
Then, the player will be prompted to enter the column letter between (between A and L). If you enter an invalid input, you will be prompted again.

"Please pick which row you would like to place your token in (Select from 1 to 10):" 

"Please pick which column you would like to place your token in (Select from A to L):" 

If an row and column position is entered for a position that is already occupied, you will be repromtpted to enter the row and column.

"Your token could not be placed at the specified coordinate. Please re-enter the coordinate of the position you would like to move your token."

When a player has successfully entered the row and column, the gamegrid will be displayed to show the new state of the game.

After the first round, it will now be possible for a player to place or move tokens via the following prompt:

"Player_name it is your turn to play. Would you like to make a placement or a movement of a token? (1-Placement, 2-Movement): "

To make a placement, input "1" and you will be prompted to enter the row and column coordinates.
To make a movement, input "2" and you will be prompted to select the desired token and input the new coordinates as follows : 


"player_name, it is your turn to play. Would you like to make a placement or a movement of a token? (1-Placement, 2-Movement): 2
You will now input the coordinates of the position you would like to move your specified token to. You can only move 1 square from your current position. Please pick which token you would like to move by specifying the row it is in (Select from 1 to 10): 1 
Please pick which token you would like to move by specifying the column it is in (Select from A to L):  A
Please pick which row you would like to move your token in (Select from 1 to 10): 1
Please pick which column you would like to move your token in (Select from A to L): b
"

If you do not select your own token or if you enter an invalid new position to move your token, you will be prompted again.
If a player has finished placing all their tokens, they will only be allowed to move tokens.



2. Player vs. AI:
