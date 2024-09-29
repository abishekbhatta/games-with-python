from blackjack_helper import *

def validation(answer):
    while answer != 'y' and answer != 'n':
      print("Sorry I didn't get that.")
      answer = input(f"You have {user_hand_value}. Hit (y/n)? ")
    return answer

#code for user-end    

user_hand_value = draw_starting_hand("YOUR")

answer = 'y'
while answer == 'y' and user_hand_value < 21:
  answer = input(f"You have {user_hand_value}. Hit (y/n)? ")
  if validation(answer) == 'y':
    user_hand_value += draw_card()

print_end_turn_status(user_hand_value)


#code for dealer-end

dealer_hand_value = draw_starting_hand("DEALER")

while dealer_hand_value < 17:
    print(f"Dealer has {dealer_hand_value}.")
    dealer_hand_value += draw_card()

print_end_turn_status(dealer_hand_value)
    
print_end_game_status(user_hand_value,dealer_hand_value)
