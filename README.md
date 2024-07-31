# Python-Projects

## Project - 1: Random Number Guessing Game

**Description**: This is a number guessing game where the player has to guess a randomly selected number between 1 and 100 within a limited number of attempts based on the chosen difficulty level.

**Algorithm**:
1. Generate a random number between 1 and 100.
2. Ask the player to choose a difficulty level ('EASY' or 'HARD').
   - EASY: Player gets 10 attempts.
   - HARD: Player gets 5 attempts.
3. Loop until the player runs out of attempts:
   - Prompt the player to guess the number.
   - Decrement the number of remaining attempts.
   - Check the player's guess:
     - If the guess is correct, print a success message and end the game.
     - If the guess is too high, prompt the player to guess lower.
     - If the guess is too low, prompt the player to guess higher.
4. If the player uses all attempts without guessing correctly, print a failure message.

## Project - 2: Black Jack Game

**Description**: This is a simplified version of the Black Jack card game where the player competes against the computer to get the highest hand total without exceeding 21.

**Algorithm**:
1. Initialize the deck of cards and the hands for the user and the computer.
2. Define helper functions:
   - `Eleven_To_One(temp_list)`: Converts an Ace (11) to 1 if the hand total exceeds 21.
   - `Random_Card_Selector()`: Selects a random card from the deck.
   - `Proper_Sum_Checker(temp_list)`: Checks if the hand total exceeds 21.
3. Start the game loop:
   - Ask the player if they want to play ('y' or 'n').
   - If 'n', exit the game.
   - If 'y', deal two cards to the player and one card to the computer.
4. Player's turn:
   - Display the player's cards and the computer's first card.
   - Loop until the player chooses to pass:
     - Ask the player if they want to draw a card ('y' or 'n').
     - If 'y', draw a card and add it to the player's hand.
       - If the hand total exceeds 21, check if there is an Ace (11) to convert to 1.
       - If the hand total still exceeds 21, end the player's turn.
     - If 'n', end the player's turn.
5. Display the player's final hand.
6. Computer's turn:
   - If the player has not busted, draw cards for the computer until it wins or busts:
     - Draw a card and add it to the computer's hand.
     - If the hand total exceeds 21, check if there is an Ace (11) to convert to 1.
     - If the hand total still exceeds 21, the player wins.
     - If the computer's hand total exceeds the player's hand total without busting, the computer wins.
7. Display the computer's final hand and declare the winner.
8. Thank the player for playing.

**More projects will be uploaded soon!**
