# %%
import os

# %%
#user-defined functions

def insert(symbol, location, map, list):
  i, j = map[location - 1][0], map[location - 1][1] #inserts the symbol at the location specified
  list[i][j] = symbol

def print_box(list):
  print("")
  for rows in list:
    for elements in rows:
      print(elements, end = "          ")  #displays the box after each player makes their move
    print("\n")

def clear_screen():      #clears the screen for each new move
  if os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")

def check_rows(symbol, list):
  for rows in list:
    count_row = 0
    for element in rows:
      if element == symbol:         #check each rows to see whether a player has won
        count_row +=1
    if count_row == 3:
      return True

  return False

def check_columns(symbol, list):
  for i in range(3):
    count_col = 0
    for j in range(3):
      if list[j][i] == symbol:    #check each columns to see whether a player has won
        count_col += 1
    if count_col == 3:
      return True

  return False

def check_diagonally_left(symbol, list):
  count_diagonally_left = 0
  for i in range(3):
    if list[i][i] == symbol:        #check left diagonal to see whether a player has won
      count_diagonally_left += 1
  
  return True if count_diagonally_left == 3 else False


def check_diagonally_right(symbol, list):
  count_diagonally_right = 0
  j = 2
  for i in range(3):                #check right diagonal to see whether a player has won
    if list[i][j] == symbol:
      count_diagonally_right += 1
    j -= 1
  
  return True if count_diagonally_right == 3 else False

#asks player for the location and calls insert, print_box, and check functions
#returns True if the player has won

def player_turn(symbol, number, list):

  location = int(input(f"Player {str(number)} enter the number representing the location to place your {symbol} (1-9): "))

  insert(symbol, location, map, list)
  print_box(box)

  if check_columns(symbol, list) or check_rows(symbol, list) or check_diagonally_left(symbol, list)or check_diagonally_right(symbol, list):
    return True, f'Boom! Player {str(number)} won.'



# %%
#main program starts here

#to store crosses and circles

box = [ ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]]


#to map index in the list

map = [[0,0], [0,1], [0,2],
       [1,0], [1,1], [1,2],
       [2,0], [2,1], [2,2]]

circle = "O"
cross = "X"

print_box(box)

num_of_times_played = 0
win = False

while not win and num_of_times_played < 9:

  #player 1 turn

  win = player_turn(circle, 1, box)
  num_of_times_played += 1
  if win or num_of_times_played == 9:
    clear_screen()
    print_box(box)
    print(win[1])
    break
  

  clear_screen()
  print_box(box) 
 
  #player 2 turn
  win = player_turn(cross, 2, box)
  num_of_times_played += 1
  if win or num_of_times_played == 9:
    clear_screen()
    print_box(box)
    print(win[1])
    break

  clear_screen()
  print_box(box)


if not win:
  print_box(box)
  print("Game is drawn.")


