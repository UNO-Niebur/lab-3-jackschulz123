#RPS.py
#Name: Jack Schulz
#Date: 2-5-2026
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  playAgain = "Y"
  while playAgain == "Y":
    #User can play as many games as they wish.
    computer = random.choice( ["R","P","S"])
    player = input("Pick your weaponn(R, P, S): ")

    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection

    #Determine winner and state what happened to the user
    if computer == "R":
      print("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors")
    
    if player == "R":
      print("Player chose Rock")
    elif player == "P":
      print("Player chose Paper")
    elif player == "S":
      print("Player chose Scissors")
    
      

    if player == "R" and computer == "R":
      print("Tie")
      ties = ties + 1
    if player == "R" and computer == "P":
      print("Computer wins.")
      losses = losses + 1
    if player == "R" and computer == "S":
      print("You win!")
      wins = wins + 1
    if player == "P" and computer == "R":
      print("You win!")
      wins = wins + 1
    if player == "P" and computer == "P":
      print("Tie")
      ties = ties + 1
    if player == "P" and computer == "S":
      print("You lost.")
      losses = losses + 1
    if player == "S" and computer == "R":
      print("You lost.")
      losses = losses + 1
    if player == "S" and computer == "P":
      print("You won!")
      wins = wins + 1
    if player == "S" and computer == "S":
      print("Tie")
      ties = ties + 1
    
    
    
    #Ask the user if they would like to play again.
    playAgain = input("Play again? (Y/N): ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
