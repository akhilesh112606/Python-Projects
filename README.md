# Python-Projects (TOTAL - 26)

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

## Project 13: Flipcard Learning
## Algorithm

### 1. Initialize the Application
- Load libraries: `tkinter`, `pandas`, `random`.
- Attempt to read `data/words_to_learn.csv`. If not found, load `data/french_words.csv`.

### 2. Prepare Data
- Convert CSV data into a list of dictionaries.

### 3. Define Button Functions
- **`next_slide()`**
  - Select a random word pair.
  - Display French word.
  - Schedule `flip_card()` in 3 seconds.
- **`flip_card()`**
  - Show English translation.
- **`is_known()`**
  - Remove current word pair from list.
  - Update `data/words_to_learn.csv`.
  - Call `next_slide()`.

### 4. Setup the User Interface
- Create a `tkinter` window with a canvas for flashcards.
- Load and set card images and buttons.
- Show the initial French word.

### 5. Start the Application
- Call `next_slide()` to display the first word.
- Start the `tkinter` main loop.

<img width="673" alt="one" src="https://github.com/user-attachments/assets/e77f10c3-baaa-43e1-bbac-3c22a40aaa6e">
<img width="672" alt="two" src="https://github.com/user-attachments/assets/85867fc9-e10b-474f-9976-4c9aca8c96a7">
This Python application tracks the position of the International Space Station (ISS) and checks if it is visible from your current location. The program also considers sunrise and sunset times to determine if the ISS is visible in the sky based on the time of day.

## Project 14 : Satelitte Coordinates Detector

## Alogrithm

### 1. **Fetch ISS Position**
   - The application retrieves the current position of the ISS using the Open Notify API (`http://api.open-notify.org/iss-now.json`).
   - The API provides the latitude and longitude of the ISS, which are stored for comparison with your location.

### 2. **Get Sunrise and Sunset Data**
   - The application fetches sunrise and sunset times using the `Sunrise-Sunset` API (`https://api.sunrise-sunset.org/json`).
   - Based on your latitude and longitude, the API returns the time of sunrise and sunset in UTC.
   - These times are extracted and converted into hour values for comparison with the current time.

### 3. **Check ISS Visibility**
   - The application determines whether the ISS is within a visible range of your location. This is done by checking if the ISS’s current latitude and longitude are within ±5 degrees of your location's latitude and longitude.
   - The visibility also depends on whether the current time is between sunset and sunrise (i.e., during the night).
   - If both conditions are met (proximity and nighttime), the ISS is considered visible.

### 4. **Visual Feedback with Tkinter**
   - The application creates a graphical user interface (GUI) using Tkinter.
   - If the ISS is visible, the background of the window turns green, and the text displays "CAN SEE ISS."
   - If the ISS is not visible, the background turns red, and the text displays "CANNOT SEE ISS."
   - The position of the ISS is checked every second using the `window.after()` method in Tkinter, ensuring real-time updates.

## APIs Used
- **Open Notify API**: Provides real-time data on the current position of the ISS.
- **Sunrise-Sunset API**: Provides the sunrise and sunset times for a given location.

<img width="148" alt="one" src="https://github.com/user-attachments/assets/d3990b5b-105b-4174-a732-c3ee501bc0c7">
<img width="153" alt="two" src="https://github.com/user-attachments/assets/8c3435e7-b11f-4f1a-bd3e-e70ddd1c5938">


## Project 15 - Quizzler Game

## Algorithm

1. **Question and Answer Data**
   - Fetches a list of True/False questions from the Open Trivia Database API using a GET request.
   - The `Question` class is used to store each question's text and correct answer.
   
2. **Setup Question Bank**
   - The `question_data` is iterated to create a `question_bank`, which stores all questions as instances of the `Question` class.

3. **QuizBrain Class**
   - Manages the quiz logic, including keeping track of the question number and score.
   - Provides the `next_question()` method to serve the next question in the quiz.
   - The `check_answer(user_answer)` method validates if the user's answer is correct.

4. **QuizDesign Class (UI Layer)**
   - The user interface is created using the Tkinter library.
   - Contains buttons for answering True or False to the displayed questions.
   - Displays feedback to the user by changing the background color of the question canvas (green for correct, red for incorrect).
   - The `change_question()` method updates the UI with a new question after each answer.
   
5. **Game Flow**
   - When the app starts, the first question is shown.
   - User answers by clicking either the "True" or "False" button.
   - The quiz continues until there are no more questions, after which the game ends and disables the answer buttons.

<img width="251" alt="four" src="https://github.com/user-attachments/assets/2d5d000a-dc2e-4644-b1fb-2e5b6d1b0ee4">
<img width="257" alt="one" src="https://github.com/user-attachments/assets/9973cba9-be39-49fb-8f36-14e90771c962">
<img width="253" alt="three" src="https://github.com/user-attachments/assets/b7f613bc-5475-458c-b7be-117f614fef0d">
<img width="257" alt="twp" src="https://github.com/user-attachments/assets/1be128b2-04fb-4519-87f8-38d1ade8b26a">

## Project 16 - Rain Alert SMS

## Algorithm

1. **Get Weather Data:**
   - The script retrieves weather data using the OpenWeatherMap API based on latitude and longitude coordinates.
   
2. **Parse Weather Data:**
   - It extracts the weather forecast for the next 12 hours from the API response.
   
3. **Check for Rain:**
   - The script loops through the 12-hour forecast and checks the weather condition codes to determine if rain is expected (codes less than 700).
   
4. **Send SMS Alert:**
   - If rain is detected, an SMS message is sent using the Twilio API to notify the user.
![two](https://github.com/user-attachments/assets/285cd829-39f8-4482-95ba-387de1778238)
<img width="877" alt="one" src="https://github.com/user-attachments/assets/e47b6e38-1eee-4329-b2a7-50e5887fa381">

## Project 17 - Stock Market Price Alert SMS

## Algorithm

**Step 1: Get Stock Prices**
1. Use Alpha Vantage API to get daily stock data for Tesla (TSLA).
2. Extract the closing prices for:
   - `yesterday_price` (most recent day).
   - `day_before_yesterday_price` (day before the most recent day).

**Step 2: Calculate Price Difference**
1. Find the difference between the two prices:
   - `difference = abs(yesterday_price - day_before_yesterday_price)`
2. Calculate the percentage change between the two prices:
   - `percentage_difference = (difference / average of both prices) * 100`

**Step 3: Get News**
1. If the percentage change is above a threshold (e.g., 5%), use NewsAPI to get the latest news about Tesla.
2. Extract the top 3 news headlines.

**Step 4: Send SMS Alerts**
1. Use Twilio API to send SMS with the news headlines if the condition is met.
   
**Step 5: End Program**
1. Output confirmation of actions taken.

![WhatsApp Image 2024-09-16 at 21 51 22_e4c31b7b](https://github.com/user-attachments/assets/b1c8ed10-f678-437b-b14e-647e7002f720)
![asdfaf](https://github.com/user-attachments/assets/2e24b0f9-0dbb-4852-bf7f-7e5f58f46449)

## Project 18 - Graphical Habit Tracker

## Algorithm

**1. Initialize Required Libraries and Variables**

- Import the necessary libraries:
  - `requests`: For making HTTP requests to the Pixela API.
  - `datetime`: To get the current date.

- Define the following constants:
  - `USERNAME`: Your Pixela username.
  - `TOKEN`: A secure token for authenticating API requests.
  - `GRAPH_ID`: The unique ID for the graph you're creating.
  - `DATE`: Current date in the format `YYYYMMDD` for creating and updating progress pixels.
  
**2. Define API Endpoints**

- Define the base Pixela API endpoint:
  ```python
  pixela_endpoint = "https://pixe.la/v1/users"

<img width="947" alt="file" src="https://github.com/user-attachments/assets/ff8d1f70-5e62-44db-85cd-65e811962b18">

## Project 19 - Workout Tracker using GOOGLE SHEETS

## Algorithm


**1. Setup**
- **Import necessary libraries**: The program uses the `requests` and `datetime` libraries for API requests and date-time management.
- **Define constants**:
  - `APP_ID` and `API_KEY`: These are credentials for the Nutritionix API.
  - `DOMAIN_ENDPOINT`: Base URL for the Nutritionix API.
  - `EXERCISE_ENDPOINT`: Specific path for natural exercise processing in the Nutritionix API.
  - `ADD_ROW_ENDPOINT`: The URL for the Sheety API to append workout data to a Google Sheet.
  - Get the current date (`TODAY`) and current time (`TIME`).

**2. Input and NLP Processing**
- **Prompt the user** to enter the details of the exercise they performed, in natural language format (e.g., "ran for 30 minutes").
- **Send a `POST` request** to the Nutritionix API:
  - The request uses the exercise input as part of the `data` parameter.
  - The API response returns details such as:
    - Exercise name (e.g., "running")
    - Duration (in minutes)
    - Calories burned (based on the type of exercise and duration).
    
**3. Extract Exercise Data**
- **Parse the response** from the Nutritionix API:
  - `EXERCISE`: The specific exercise the user performed.
  - `DURATION`: The duration of the exercise (in minutes).
  - `CALORIES`: The number of calories burned during the exercise.

**4. Prepare Data for Logging**
- **Create a new row** of data to be sent to the Google Sheet, structured as:
  - `date`: The current date of the exercise.
  - `time`: The current time when the exercise was logged.
  - `exercise`: The exercise performed (from Nutritionix API).
  - `duration`: Duration of the exercise in minutes.
  - `calories`: Calories burned during the exercise.

**5. Send Data to Google Sheets**
- **Send a `POST` request** to the Sheety API:
  - The new row data is passed as `JSON`.
  - If the API returns a success status (HTTP 200), print a success message confirming the row was added.

**6. Completion**
- The program ends once the workout data is successfully logged.

![two](https://github.com/user-attachments/assets/e2a15b5e-09d7-4182-8157-937f0767cf2b)
![one](https://github.com/user-attachments/assets/c9a4428e-7861-4af4-9fd1-3e65155c6c61)


## Project 20 - Cheap Flight Price SMS & EMAIL Alert

## Algorithm
**1. Initialization**:
   - Import the required modules:
     - `datetime`, `requests`, `smtplib`, `twilio.rest.Client`
   - Instantiate the following objects:
     - `DataManager` to manage sheet data.
     - `FlightSearch` to search for flight data and IATA codes.
     - `FlightData` to manage flight data retrieval.
     - `NotificationManager` to send email and SMS notifications.

**2. Set Date Range**:
   - Define a `DATE_SPAN` variable by adding 180 days to the current date.
   - Format the date into a string to use in API requests and notifications.

**3. Fetch Google Sheet Data**:
   - Retrieve data from Google Sheets using the `DataManager.get_sheet_data()` method.
   - Initialize an empty list `iata_missing_list` to store city names where IATA codes are missing.

**4. Check for Missing IATA Codes**:
   - Loop through the sheet data and identify entries where `iataCode` is empty.
   - Append cities with missing IATA codes to `iata_missing_list`.

**5. Update IATA Codes**:
   - Pass the list of missing cities to `FlightSearch.update_iata_codes()` to fetch and update IATA codes.
   - Update the Google Sheet with the newly fetched IATA codes using `DataManager.update_sheet_data()`.

**6. Extract Email Addresses**:
   - Retrieve email addresses from Google Sheets using `DataManager.get_EMAIL_data()` and store them in the `email_IDs` list.

**7. Check for Flight Deals**:
   - Loop through each city in the sheet data:
     - Use `FlightData.flight_cheapest_flight()` to fetch the lowest price for a given city.
     - Compare the current flight price to the previously recorded lowest price (`price_in_doc`).
     - If the new price is lower, send SMS and email notifications to the user using `NotificationManager.send_sms()` and `NotificationManager.send_mail()`.

**8. Send Notifications**:
   - **SMS**:
     - Use the Twilio API to send an SMS notification about the lower price.
     - Message content includes details about the flight, such as the price, departure city, destination city, and available date range.
   - **Email**:
     - Use the SMTP module to send an email to all recipients retrieved from Google Sheets.
     - The email contains details about the flight and its new lower price.

![one](https://github.com/user-attachments/assets/b248832b-bc41-4df8-a679-038e5de8c6ab)
![four](https://github.com/user-attachments/assets/bf0cdc46-70df-4771-85d3-259622a0f05a)
![three](https://github.com/user-attachments/assets/59476843-045c-45f8-bc19-3de3d2d110eb)
![two](https://github.com/user-attachments/assets/a773a2b0-4e7e-457d-8aa3-c9a8415a8769)
![five](https://github.com/user-attachments/assets/78bab9df-aaf8-4530-8531-57c9e4fa5aa0)

## Project 21 - Spotify Playlist Maker - TOP 100 BillBoard
## ALgorithm
1. **User Input**:
    - Prompt the user to input a date in the format `YYYY-MM-DD`.

2. **Validate Date**:
    - Use the `datetime.strptime()` method to validate the date format.
    - If the date is invalid, print an error message and exit.

3. **Fetch Billboard Chart**:
    - Make a GET request to the Billboard website to retrieve the HTML data for the chart corresponding to the input date.
    - Parse the HTML using `BeautifulSoup` to extract the song titles from the page.
    - Store the song titles in a list.

4. **Spotify Authentication**:
    - Use `SpotifyOAuth` from the Spotipy library to authenticate with Spotify using `Client_ID`, `Client_Secret`, and `Spotify_Username`.
    - Obtain an authentication token to modify the user's Spotify playlist.

5. **Find Song URIs on Spotify**:
    - For each song title in the list:
        - Search Spotify's track database using the song title.
        - Retrieve the song's URI (if available) and add it to a list.
        - Print a message if the song is not found.

6. **Create a New Playlist**:
    - Use Spotify's API to create a private playlist on the user's account with the name corresponding to the input date and Billboard Hot 100.

7. **Add Songs to Playlist**:
    - Add all the song URIs from the list to the newly created playlist on Spotify.

<img width="318" alt="pic1" src="https://github.com/user-attachments/assets/89d11aa6-5fd3-4e6d-9c9c-fd3f3516ec3c">
<img width="245" alt="pic2" src="https://github.com/user-attachments/assets/cc80a97c-94bd-4b7f-9e63-ca8287a94873">
<img width="437" alt="pic3" src="https://github.com/user-attachments/assets/c264ccd1-395d-4b35-998e-d7391ed347a4">

## Project 22 - Automated Amazon Price Tracker
## ALgorithm
1. **Input Product URL**:
    - Prompt the user to enter the Amazon product link.

2. **Set Target Price**:
    - Define a target price for the product (can be modified by the user).

3. **Fetch Product Page**:
    - Attempt to connect to the specified product URL.
        - If successful, print "Website Connected!"
        - If unsuccessful, print "Website Connection Failed!" and exit the program.

4. **Parse HTML**:
    - Use BeautifulSoup to parse the HTML content of the product page.

5. **Extract Product Title**:
    - Locate the product title using the appropriate HTML tags and classes.
    - Clean up the title string by removing extra spaces.

6. **Extract Product Price**:
    - Locate the product price using the appropriate HTML tags and classes.
    - Remove any commas and dots from the price string.
    - Convert the cleaned price string to an integer.

7. **Display Product Information**:
    - Print the product title and the current price.

8. **Email Setup**:
    - Define email sender and receiver details (email addresses and SMTP credentials).
    - Compose the email body with the product title and price.

9. **Check Price Against Target**:
    - If the current product price is less than the target price:
        - Create an email message with the subject "Price Drop Alert!" and the email body.
        - Attempt to connect to the SMTP server and send the email.
            - If successful, print "EMAIL SENT SUCCESSFULLY!"
            - If unsuccessful, print "EMAIL FAILED! ERROR OCCURED"
         
![pic2](https://github.com/user-attachments/assets/6b1ca25b-3509-4089-8530-081cfe9a3923)
<img width="856" alt="pic1" src="https://github.com/user-attachments/assets/ba47dac5-0f3e-4c9d-878e-97bb3e5ebb56">

## Project 23 - Automated LinkedIN Job Applier
## Algorithm

1. **Set up WebDriver Options**:
   - Configure the WebDriver options to keep the Chrome browser open after execution.
   
2. **Initialize WebDriver**:
   - Launch a new Chrome WebDriver instance with the configured options.
   
3. **Navigate to LinkedIn Login Page**:
   - Open the LinkedIn login page by specifying the URL (`https://www.linkedin.com/login`).

4. **Log in to LinkedIn**:
   - Locate the email and password input fields and the "Sign in" button.
   - Input the email and password, then click the "Sign in" button to log in.
   
5. **Access LinkedIn Jobs Section**:
   - Navigate to the "Jobs" tab by locating and clicking the corresponding element.

6. **Search for Job Title**:
   - Locate the job search input box, input the desired job title (e.g., "Python Developer"), and press Enter to perform the search.
   
7. **Select Easy Apply Option**:
   - Locate the "Easy Apply" button for a job listing and click it to open the application form.

8. **Fill in Application Details**:
   - Input personal details such as the mobile number in the appropriate fields.
   - Click the "Next" button to proceed to additional steps, if required.

9. **Answer Additional Questions**:
   - If a dialogue box with questions appears, locate and select appropriate answers.

10. **Review and Submit Application**:
    - Click the "Review" button to review the application details.
    - Finally, locate and click the "Submit" button to complete the application process.

https://github.com/user-attachments/assets/2cbb0181-e8d0-407b-8f09-a12a6f529901

## Project 24 - Automated Tinder Swiper
## Algorithm
1. **Set Up Chrome Browser to Stay Open After Code Completion**
   - Use `webdriver.ChromeOptions()` to configure Chrome to remain open when the code execution finishes.
   - Add the `detach` option to `ChromeOptions`.

2. **Initialize Web Driver and Open Tinder Recovery Link**
   - Use `webdriver.Chrome()` with the Chrome options configured.
   - Open Tinder's account recovery URL.

3. **Pause Execution for Page to Load** 
   - Wait 10 seconds to allow all elements to load.

4. **Accept Cookies**
   - Locate and click the cookie acceptance button using its XPath.

5. **Enter Mobile Number**
   - Locate the mobile number input box by ID.
   - Input your mobile number or login credentials.

6. **Submit Login Form**
   - Locate and click the submit button to proceed.

7. **Allow Location Access**  
   - After a 15-second pause, locate and click the location access button to allow location access.

8. **Dismiss Notifications Popup**  
   - Wait 2 seconds.
   - Locate and click the button to dismiss notification requests.

9. **Automate 'Like' Button Clicks**
   - Locate the 'like' button on the page.
   - Set up a loop to repeat the 'like' button click for a specified number of times (e.g., 100).
   
10. **Handle Exceptions for Intercepted Clicks and Matches**
    - For each iteration, wait 1 second and attempt to click the 'like' button.
    - **If Element Not Found**: Pause for 2 seconds before trying again.
    - **If Element Click Intercepted**: Check if there's a match popup.
      - If found, locate and click the "It's a Match" button to dismiss.
      - If not, pause for 2 seconds before retrying.

11. **Close Browser**
    - End the session by calling `driver.quit()` after the loop completes.

## Project 25 - Automated XTwitter Complpaint Bot
## Algorithm

1. **Initialize Browser Options:**
   - Set up `chrome_options` for ChromeDriver with an option to keep the browser open.

2. **Launch WebDriver Instances:**
   - Open two browser windows:
     - `ookla` for internet speed testing.
     - `driver` for Twitter login and interaction.

3. **Navigate to Websites:**
   - Load `https://www.speedtest.net/` in the `ookla` browser.
   - Load Twitter's signup/login page in the `driver` browser.

4. **Start Internet Speed Test:**
   - Locate and click the "Start Test" button on the Speedtest website.
   - Wait for the test to complete and extract the download and upload speeds.

5. **Extract Speed Test Results:**
   - Use `find_element` with appropriate selectors to get the download and upload speed data.
   - Store the text values in `download_text` and `upload_text`.

6. **Twitter Login Process:**
   - Locate the login button on Twitter and click it.
   - Enter the username/email and click "Next".
   - Input the phone number (if required) and proceed.
   - Enter the password and log in.

7. **Compose and Send Tweet:**
   - Navigate to the tweet input field.
   - Write a tweet containing the speed test results.
   - Optionally, submit the tweet.

8. **Custom Message:
   - Print or log the custom message with download and upload speeds.
  

https://github.com/user-attachments/assets/7d5ed24b-68dc-494e-b9b3-bbc6eb0ba946

## Project 26 - Automated Instagram 
## Algorithm
   1. **Setup**
- Import necessary libraries:
  - Use `selenium` for browser automation.
  - Use `time` for delays to ensure elements load properly.
- Initialize the `InstaFollower` class:
  - Create the `__init__` method to:
    - Configure Chrome browser options to keep the browser open after the script runs.
    - Create an instance of the Chrome WebDriver to interact with the Instagram web interface.
    - Navigate to the Instagram login page (`https://www.instagram.com/`).

2. **Login Method**
- Locate elements and input credentials:
  - Locate the username input field using an XPath selector and send the username.
  - Locate the password input field using an XPath selector and send the password.
  - Locate and click the login button using an XPath selector.
- Handle the "Not Now" prompt:
  - Wait for the page to load using `time.sleep()`.
  - Locate and click the "Not Now" button for notifications using a CSS selector.

3. **Find Followers Method**
- Navigate to the followers section:
  - Locate and click the search button using a CSS selector.
  - Wait for the page to load and locate the followers button using a CSS selector.
  - Click the followers button to open the followers list.

4. **Completion**
- The program completes the automation sequence once the followers section is accessed successfully.
- The browser remains open for further inspection due to the Chrome option configuration.



https://github.com/user-attachments/assets/796c231c-500d-49c6-a80f-0edafad4b82a



**More projects will be uploaded soon!**





