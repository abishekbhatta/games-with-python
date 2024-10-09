# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.


#user-turn
def user_turn(name):
  user_hand = draw_starting_hand(name.upper())
  should_hit = 'y'
  while user_hand < 21:
    should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
    if should_hit == 'n':
      break
    elif should_hit != 'y':
      print("Sorry I didn't get that.")
    else:
      user_hand = user_hand + draw_card()
  print_end_turn_status(user_hand)
  return user_hand

#dealer-turn   
def dealer_turn():
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)
  return dealer_hand

number_of_players = int(input("Welcome to Blackjack! How many players? "))
users = []  # Stores a 2D list of each player's [Name, Hand Value, Score]


# Loop to gather player names and initialize hand value (0) and score (3)
for index in range(1, number_of_players + 1):
  player_name = input(f"What is player {index}'s name? ")
  users.append([player_name, 0, 3])  # Each player starts with a score of 3

again = 'y'  # Used to control the continuation of rounds
number_of_eliminated = 0  # Tracks the number of players eliminated from the game

# Main game loop; runs as long as the user wants to continue ('again' is 'y')
while again == 'y':

  # Loop over each player to handle their turn
  for rows in users:

      # Check if player is still in the game (score is not 0)
      if rows[2] != 0:
          # Call user_turn function to handle the player's hand, and update their hand value
          user_hand_value = user_turn(rows[0])
          rows[1] = user_hand_value

  # Dealer plays their turn after all players have played
  dealer_hand_value = dealer_turn()

  # Display the result header for this round
  print_header("GAME RESULT")

  # Loop through each player's result after the dealer's turn
  for rows in users:
      if rows[2] != 0:  # Only process players who are not eliminated
          # Call function to determine the result of the game (win, lose, or push)
          result = print_end_game_status(rows[0], rows[1], dealer_hand_value)
          
          # Update the player's score based on the game result
          if result == "W":  # Player wins
              rows[2] += 1
              print(f"{rows[0]} wins! Score: {rows[2]}")
          elif result == "L":  # Player loses
              rows[2] -= 1
              print(f"{rows[0]} loses! Score: {rows[2]}")
          else:  # It's a push (tie)
              print(f"{rows[0]} pushes. Score: {rows[2]}")
          
          # Eliminate the player if their score reaches 0
          if not rows[2]:
              print(f"{rows[0]} eliminated!")
              number_of_eliminated += 1

  # If all players are eliminated, the game ends
  if number_of_eliminated == number_of_players:
      print("All players eliminated!")
      break

  # Ask if players want to play another round
  again = input("Do you want to play another hand (y/n)? ")