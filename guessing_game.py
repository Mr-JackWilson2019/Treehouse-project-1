"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
#random is slower than numpy.random

import random


def start_game(high_score):
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    print("""Hello, welcome to the number guessing game. This program will
    randomly select a number between 1 and 10, including 1 and 10. To play,
    guess a number between 1 and 10. If the program tells you the number is 
    higher, guess another number that is higher than the last number you 
    guessed. If the program tells you that the number is lower, guess a number
    lower than the one you guessed. Try to beat the high score if one exists.
    
    Enjoy!""")
    
    if high_score is not None:
      #I learned about f strings a while ago. I'm not new to python
      print(f"The current high score is {high_score}")
    
    number_to_guess = random.randrange(1, 10)
    
    number_of_guesses = 0
    try:
      guess = int(input("Guess the number. It's between 1 and 10: "))
    except ValueError:
      print("Looks like you didn't enter an integer. Pleae try again")
      exit()
    
    while True:
      try:
        number_of_guesses += 1
        if guess == number_to_guess:
          print("congratulations! You won!")
          print(f"It took {number_of_guesses} tries.")
          play_again = input("Do you want to play again? Y/N ")
          
          if play_again.upper() == "Y":
            #check to see if current score is lower than high score
      
            #keeping my character count in check
            #shouldn't be an error since the entire or statement evaluates
            #the true as soon as part of the condition is true.
            if (high_score is None) or\
              (number_of_guesses < high_score):
              start_game(high_score = number_of_guesses)
            else:
              start_game(high_score = high_score)
          elif play_again.upper() == "N":
            exit()
          else:
            raise ValueError()
           
        elif guess < number_to_guess:
          guess = int(input("It's higher! "))
          continue
        elif guess > number_to_guess:
          guess = int(input("It's lower! "))
          continue
    
      except ValueError as e:
        print("Please enter integers for guessing. Enter either a Y or an N"
              "when prompted with Y/N")
        #This is just to make sure that your number of guesses doesn't
        #increase if you mess up
        number_of_guesses -= 1
        continue

    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game(None)
