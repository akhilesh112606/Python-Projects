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
   
   ![work1](https://github.com/user-attachments/assets/eca7bdfa-d3ab-42e9-88a3-e09449b48cad)
   ![work2](https://github.com/user-attachments/assets/84061651-f60c-4041-9191-a2d1aff8a9f6)


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
   
   
   ![image](https://github.com/user-attachments/assets/7edd7b9c-e487-430e-af7a-b5179aa6bcdc)

## Project - 3: Higher & Lower Game

**Description**: The "Higher & Lower Game" challenges players to guess which of two randomly selected entities has more followers. The game continues until the player guesses incorrectly, and their score reflects the number of consecutive correct guesses.

**Algorithm**:
1. Initialize the game by setting the player's score to 0 and selecting a random choice for "A" from a predefined list of data.
2. Loop until the player makes an incorrect guess:
   - Display the current score and details of the choice "A" (name, description, and country).
   - Randomly select a new choice for "B" from the data list.
   - Display the details of choice "B" along with a graphic separator.
   - Compare the follower counts of choice "A" and choice "B".
   - Determine which choice has more followers:
     - If choice "A" has more or equal followers, set the correct answer to "A".
     - Otherwise, set the correct answer to "B".
   - Prompt the player to guess which choice has more followers by typing "A" or "B".
   - If the player's guess is correct:
     - Increment the player's score.
     - Replace choice "A" with choice "B" for the next round.
     - Clear the screen to prepare for the next round.
   - If the player's guess is incorrect, end the game and display the final score.

![pic1](https://github.com/user-attachments/assets/5ff94c85-5062-4228-b594-5f3a8c777548)
![pic2](https://github.com/user-attachments/assets/3e366d71-4a14-4713-be1d-e8b7c486e091)
![pic3](https://github.com/user-attachments/assets/74aad3d8-d08b-4cae-b76c-aa867e372898)
![pic4](https://github.com/user-attachments/assets/8b9f4a63-8c99-47ca-850d-35ff4906cb8c)


## Project - 4: COFFEE MACHINE LOGIC

**Description**: The "Coffee Machine Logic" project simulates a basic coffee vending machine. Users can choose from different coffee options, pay using coins, and receive their selected beverage if sufficient resources and money are available.

**Algorithm**:
1. **Define the Menu and Resources**:
   - The `MENU` dictionary contains the recipes for each coffee type (`espresso`, `latte`, `cappuccino`) with their respective ingredients and costs.
   - The `resources` dictionary keeps track of the current available ingredients and money in the machine.

2. **Start the Machine Loop**:
   - Prompt the user to select a beverage (`espresso`, `latte`, `cappuccino`) or type 'report' to see the current resources.
   - If the user types 'no', exit the loop and end the program.
   - If the user selects a valid coffee option:
     - Check if the machine has enough resources to make the selected coffee.
     - If not, inform the user and restart the loop.
   
3. **Handle Coin Insertion**:
   - Prompt the user to insert coins: quarters, dimes, nickels, and pennies.
   - Calculate the total amount of money inserted by the user.

4. **Check Payment**:
   - If the inserted amount is less than the coffee cost, notify the user of insufficient funds and return the money.
   - If the inserted amount is sufficient:
     - Calculate and return any change to the user.
     - Deduct the ingredients used to make the coffee from the machine's resources.
     - Add the payment to the machine's money resources.
     - Serve the coffee to the user.

5. **Invalid Option Handling**:
   - If the user selects an invalid option, notify them and prompt them to choose again.

6. **Exit the Program**:
   - Thank the user for using the coffee machine when they choose to exit.
  
![result1](https://github.com/user-attachments/assets/cb258be4-a7a3-4155-8eaa-0a69e8dfb2a3)

## Project - 5: True or False Game using OOP

**Description**: This project is a "True or False" quiz game implemented using Object-Oriented Programming (OOP). It allows players to answer a series of true or false questions and provides feedback on their performance.

**Algorithm**:
1. **Question Data**: 
   - Questions and their correct answers are stored in a data source (e.g., a list of dictionaries).

2. **Question Model**:
   - Define a `Question` class to represent each question with its text and answer.

3. **Quiz Brain**:
   - Define a `QuizBrain` class to manage the quiz flow:
     - Initialize with a list of `Question` objects (`question_bank`).
     - Track the current question index and the player's score.

4. **Setup**:
   - Create a list called `question_bank`.
   - Loop through the `question_data` to create `Question` objects for each question and add them to `question_bank`.

5. **Quiz Flow**:
   - Create a `QuizBrain` instance with the `question_bank`.
   - Loop through the questions using the `still_has_questions()` method:
     - Display the next question and prompt the player for an answer.
     - Check if the player's answer is correct.
     - Update the score accordingly.

6. **Completion**:
   - After all questions have been answered, display the player's final score.
  

![pic1](https://github.com/user-attachments/assets/c2a4e55a-5fd5-4671-bfb7-6e811f542359)

![pic2](https://github.com/user-attachments/assets/641df79b-d548-482d-acf5-32ae60fca2dd)

## PROJECT - 6: TURTLE RACING GAME

**Description**
This is a simple turtle race game built using Python's `turtle` module. The game allows users to place bets on a turtle's color and then watch a race to see if their chosen turtle wins!

**How to Play**
1. When the game starts, you will be prompted to place your bet by selecting a turtle's color from the available options.
2. After placing your bet, the race will begin following a brief countdown.
3. Watch the turtles race to the finish line!
4. If your chosen turtle wins, you will be notified with a "YOU WON!" message. If not, you'll see a "YOU LOST!" message.

**Algorithm**

1. **Initialize Variables:**
   - Create a list `color_list` containing the colors for the turtles.
   - Initialize an empty list `turtle_list` to store the turtle objects.
   - Create variables `winner_turtle` and `is_race_on` to track the race status.

2. **Setup Screen:**
   - Set up the turtle screen with a size of 500x400 pixels.
   - Prompt the user to place a bet on a turtle color from the `color_list`.

3. **Create Turtles:**
   - Loop through the `color_list` and create six turtles with the respective colors.
   - Append each turtle to the `turtle_list`.

4. **Position Turtles:**
   - Set the initial vertical position of the turtles.
   - Loop through the `turtle_list` and position each turtle at the starting line with appropriate spacing.

5. **Countdown Before Race:**
   - Create a countdown sequence (3, 2, 1, GO!) with a delay between each number.
   - Clear the turtle used for displaying the countdown.

6. **Start the Race:**
   - If the user's chosen color is in the `color_list`, start the race.
   - While the race is on:
     - For each turtle, randomly generate a forward distance.
     - Move the turtle forward by the generated distance.
     - Check if any turtle has crossed the finish line (x-coordinate > 230).
     - If a turtle wins, stop the race and store the winning turtle's color.

7. **Announce the Result:**
   - Create a temporary turtle to display the race result.
   - If the user's chosen turtle wins, display a "YOU WON!" message in green.
   - If the user's chosen turtle loses, display a "YOU LOST!" message in red.

8. **Handle Invalid Input:**
   - If the user inputs a color not in `color_list`, display an error message and exit the program.

9. **Exit Program:**
   - Keep the screen open until the user clicks on it to exit.

![pic1](https://github.com/user-attachments/assets/1df75185-6ba0-4281-9c2f-21a61b0654a7)
![pic2](https://github.com/user-attachments/assets/4ff8e0ea-63ce-459a-99af-c9ce45e44669)
![pic3](https://github.com/user-attachments/assets/fff7c05b-1b60-4061-91a3-386f8f500752)

## Project - 6: Snake Game

**Description**: This project is a classic "Snake Game" where the player controls a snake to eat food, grow in size, and avoid colliding with the walls or itself.

**Algorithm**:
1. **Initialize the Game**:
   - Set up the screen with a black background and a title.
   - Create a `Snake` class to initialize a snake with a list of turtle segments.
   - Create a `Food` class to manage the food item on the screen.
   - Create a `Score` class to track and display the player's score.

2. **Game Controls**:
   - Use the arrow keys to change the snake's direction (`up`, `down`, `left`, `right`).

3. **Game Loop**:
   - Continuously update the screen and move the snake.
   - Check for collision with food:
     - If the snake's head is close to the food, reposition the food, increase the score, and grow the snake.
   - Check for collision with walls:
     - If the snake's head collides with the wall, end the game and display "Game Over".
   - Check for collision with itself:
     - If the snake's head collides with any part of its body, end the game.

4. **End Game**:
   - Display "Game Over" and the final score when the game ends.
   - Close the game window on click.
  


https://github.com/user-attachments/assets/e6192aee-8eea-49c9-8067-cb44c954e18a

## PROJECT 7 - Snake Game Part 2

This repository contains a simple implementation of the classic Snake Game using Python's Turtle graphics module. The game features an evolving snake that moves around the screen, consuming food, and growing in size. The game ends when the snake collides with itself.



## Algorithm

### Snake Initialization
1. *Snake Body Creation*: 
    - The snake starts with three segments, initialized as square-shaped turtle objects.
    - The head of the snake is represented with a turtle shape for distinction.

### Game Loop
1. *Movement*:
    - Each segment of the snake follows the segment in front of it, with the head moving in the direction indicated by the player.
    - The speed of the snake increases as the score reaches specific thresholds, making the game progressively challenging.

2. *Food Detection*:
    - The snake checks if its head is within a certain distance of the food. If so:
        - The food is repositioned randomly on the screen.
        - The score is incremented.
        - A new segment is added to the snake's body.

3. *Screen Wrapping*:
    - If the snake's head moves beyond the screen boundary, it reappears on the opposite side, maintaining the game's continuity.

4. *Collision Detection*:
    - *Wall Collision*: Instead of stopping the game, the snake reappears on the opposite side of the screen when it hits the wall.
    - *Self-Collision*: The game checks if the snake's head collides with any other part of its body. If a collision is detected, the game ends.

### Game End
- When the game detects a collision with the snake's body, it triggers the game-over sequence, displaying a "GAME OVER" message and ending the loop.

## Code Analysis

### Snake Class
- *Attributes*: 
    - turtles_list: A list that stores all segments of the snake.
- *Methods*:
    - __init__: Initializes the snake with three segments.
    - move: Controls the movement of the snake, adjusting speed based on the score.
    - up, down, left, right: Handle directional movement based on key presses.
    - increase_snake_body: Adds a new segment to the snake's body.

### Food Class
- *Attributes*:
    - dot_turtle: A turtle object representing the food.
- *Methods*:
    - __init__: Initializes the food and places it randomly on the screen.
    - new_position_food: Randomly places the food in a new position.

### Score Class
- *Attributes*:
    - score_turtle: A turtle object used for displaying the score.
    - score: Tracks the player's score.
- *Methods*:
    - __init__: Initializes the score display.
    - increase_score: Updates the score and refreshes the display.
    - game_over: Displays a "GAME OVER" message when the game ends.

## Project 8: Pong Game

## Algorithm Overview

1. **Initialize the Game**:
   - Setup the screen with the correct size and background.
   - Initialize two paddles (`left_paddle`, `right_paddle`), a ball, and a scoreboard.

2. **Paddle Movement**:
   - Use the arrow keys to move the right paddle up and down.
   - Use 'W' and 'S' keys to move the left paddle up and down.

3. **Ball Movement**:
   - The ball moves continuously, bouncing off the top and bottom edges of the screen.
   - If the ball hits a paddle, it bounces back in the opposite direction (horizontal reflection).

4. **Ball-Paddle Collision**:
   - When the ball comes within a certain distance of a paddle and aligns with its position, it bounces back.

5. **Scoring System**:
   - If the ball goes past the right edge of the screen, Player 1 scores, and the ball is reset to the center.
   - If the ball goes past the left edge, Player 2 scores, and the ball is reset.

6. **Winning Condition**:
   - The game checks if either player has reached the winning score.
   - The game ends when Player 1 scores 2 points or Player 2 scores 5 points. A winning message is displayed on the screen.




https://github.com/user-attachments/assets/afeae3a6-61e2-4875-b431-1d4f935602b1

## Project 9: Turtle Cross Game

## Algorithm Overview

1. **Initialize the Game**:
   - Set up the screen size and tracer for performance optimization.
   - Initialize the player (`main_turtle`), car manager (`car_manager_turtle`), and scoreboard (`score_turtle`).

2. **Player Movement**:
   - Bind the **Up** and **Down** arrow keys to move the player turtle forward and backward.

3. **Car Creation and Movement**:
   - Cars are randomly generated from the right side of the screen.
   - The cars move from right to left, and the speed increases with each level.

4. **Collision Detection**:
   - If the player's turtle is within a certain distance of any car, the game ends.

5. **Level Progression**:
   - Once the turtle reaches the finish line, the level increases, the turtle moves back to the start, and the cars move faster.

6. **Game Over**:
   - Display a "GAME OVER!" message if a collision occurs.



https://github.com/user-attachments/assets/775193b3-cd40-40e1-b68c-a5e1ebe01873


## Project 10: U.S. States Game

## Algorithm

1. **Initialize Game**: Set up the screen with a blank map image and initialize variables for tracking the score and guessed states.
2. **Load Data**: Read the CSV file containing state names and their corresponding coordinates.
3. **Main Game Loop**:
   - Prompt the user to input a state name.
   - Check if the input state is in the list of all states.
   - If the user types "Exit", create a list of missed states and save it to a CSV file.
   - If the state is valid and not already guessed, update the guessed states list and score.
   - Use the `turtle` library to place the state name on the map at the corresponding coordinates.
4. **End Game**: Close the game window when the user exits.

<img width="477" alt="image" src="https://github.com/user-attachments/assets/dcd36024-9e7c-452c-9117-8fb572828507">
<img width="177" alt="image" src="https://github.com/user-attachments/assets/f6ce05de-2518-47ad-93cc-67465f623375">

## Project 11: Pomodoro Timer

## Alogrithm

**1. Initialize**
- Set up a Tkinter window.
- Define constants for colors, fonts, and timer durations.
- Initialize global variables for repetitions, ticks, and reset handle.

**2. Reset Timer**
- Reset `REPS` and `TICK`.
- Update UI to show "TIMER" and reset countdown display.
- Cancel any active timer using `window.after_cancel()`.

**3. Start Timer**
- Increment `REPS`.
- Determine the timer phase (work, short break, or long break) based on `REPS`.
- Update UI with the current phase and start the countdown.

**4. Countdown**
- Update countdown display every second.
- On countdown completion, start the next timer phase.
- Update tick marks if the session is completed.

**5. UI Setup**
- Configure window appearance and layout.
- Create and place UI elements such as labels, buttons, and canvas.

**6. Run Application**
- Start the Tkinter event loop with `window.mainloop()`.
  
<img width="416" alt="tomato screenshot" src="https://github.com/user-attachments/assets/017f3720-555d-4e75-9f6a-31877497090e">

## Project 12: Password Manager

## Algorithm

1. **Password Generation**:
    - A random password is generated using letters, numbers, and symbols.
    - The length of the password is random, with 8-10 letters, 2-4 symbols, and 2-4 numbers.
    - The password is shuffled to ensure randomness and copied to the clipboard for ease of use.

2. **Password Storage**:
    - User inputs the website name, email/username, and password into the UI.
    - On clicking the "Add" button:
        - The program checks if all fields are filled.
        - If filled, a confirmation message is displayed.
        - Once confirmed, the details are written to the `data.txt` file.
        - The input fields are then cleared, and the email/username field is reset to a default value.

<img width="346" alt="1" src="https://github.com/user-attachments/assets/e30be7d2-c637-49bb-9123-b26c4c1f3250">
<img width="512" alt="2" src="https://github.com/user-attachments/assets/b00928b3-5956-4a3a-806c-ff7f4f1ccb35">
<img width="477" alt="3" src="https://github.com/user-attachments/assets/2df99f0b-d7b5-456f-9532-f0696d417e48">


**More projects will be uploaded soon!**





