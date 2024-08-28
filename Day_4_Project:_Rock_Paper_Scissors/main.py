import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______) 
         _______)  
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______) 
       __________)
      (____)
---.__(___)
'''
             #   0     1       2
game_images = [rock, paper, scissors]  
user_input  = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_input = random.randint(0,2)
print(f"Computer choose {game_images[computer_input]}")
if user_input > 2 or user_input < 0 :
    print("Your input is invalid : You lose")
else:    
    print ("You choose")
    print (game_images[user_input])

if user_input  == 0 and  computer_input  == 1:
    print ("You loose!")
elif user_input == 1 and computer_input == 0:
    print ("You win!")
elif user_input == 1 and computer_input == 2 :
    print("You loose!")
elif user_input == 2 and computer_input == 1:
    print("You win!")
elif user_input == 0 and computer_input == 2:
    print ("You win!")
elif user_input == 2 and computer_input == 0:
    print ("You lose!")
else:
    print("Match draw!")

    
