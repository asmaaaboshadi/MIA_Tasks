# **Two-Player Chess Game**

## Overview

This project is a two-player chess game implemented in Python using the Pygame library. The game features a graphical user interface (GUI) that allows two players to play chess on a standard 8x8 chessboard. The game includes functionalities such as piece movement, turn-based play, piece capture, and check detection.

## **Features**

* **Graphical User Interface (GUI)**: Rendered using Pygame, with a visually appealing chessboard and piece images.
* **Piece Movement**: Supports all standard chess moves for each piece (pawn, knight, bishop, rook, queen, king).
* **Turn Management**: Alternates turns between the two players.
* **Piece Capture**: Captured pieces are tracked and displayed.
* **Check Detection**: Highlights the king in check with a flashing border.
* **Game Over**: Displays a game-over message when a king is captured.


## Install Dependencies:

Ensure you have Python 3 installed. Install the required Python libraries using pip:

pip install pygame


## Prepare Assets:

Download chess piece images and place them in the ./images directory. The images should be named as follows:

* black_Queen.png
* black_King.png
* black_Rook.png
* black_Bishop.png
* black_Knight.png
* black_Pawn.png
* white_Queen.png
* white_King.png
* white_Rook.png
* white_Bishop.png
* white_Knight.png
* white_Pawn.png


## Usage

**Run the Game:**
Execute the main script to start the game:
* chess_game.py

**Playing the Game:**

* Selecting a Piece: Click on a piece to select it. White pieces can be selected during White's turn, and Black pieces can be selected during Black's turn.
* Moving a Piece: After selecting a piece, click on a valid move location to move the piece.
* Forfeit: Click on the designated area to forfeit the game.
* Check Detection: If a king is in check, it will be highlighted with a flashing border.

**Restarting the Game:**
Press ENTER to restart the game after a checkmate.

## Code Explanation
* Initialization: Sets up the Pygame environment, loads assets, and initializes game variables.
* Game Loop: Handles the game logic, including piece movement, turn management, and drawing updates to the screen.
* Drawing Functions: Render the chessboard, pieces, valid moves, captured pieces, and game status.
* Move Validation: Implements the rules for each piece's movement and checks for valid moves.
* Check Detection: Highlights the king in check if applicable.