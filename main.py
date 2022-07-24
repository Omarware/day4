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

#Write your code below this line 👇
import random

user_choice = int(input("Please choose, 1 for rock, 2 for paper or 3 for scissors: "))
if user_choice > 3:
  print("Invalid choice")
else:
  computer_choice = random.randint(1,3)
  if computer_choice == 1:
    computer_choice = rock
  elif computer_choice == 2:
    computer_choice = paper
  else:
    computer_choice = scissors

  if user_choice == 1:
    user_choice = rock
  elif computer_choice == 2:
    user_choice = paper
  else:
    user_choice = scissors  

  if user_choice == rock and computer_choice == rock:
    print("The user has chosen\n" + user_choice + "\nThe computer has chosen\n" + computer_choice + "\nIt is a tie")
  elif user_choice == rock and computer_choice == paper:
    print("The user has chosen\n" + user_choice + "\nThe computer has chosen\n" + computer_choice + "\nThe Computer wins")
  elif user_choice == rock and computer_choice == scissors:
    print("The user has chosen\n" + user_choice + "\nThe computer has chosen\n" + computer_choice + "\nThe User wins")
  elif user_choice == paper and computer_choice == rock:
    print("The user has chosen\n" + user_choice + "\nThe computer has chosen\n" + computer_choice + "\nThe User wins")
  elif user_choice == paper and computer_choice == paper:
    print("The user has chosen\n" + user_choice + "\nThe computer has chosen\n" + computer_choice + "\nIt is a tie")
  elif user_choice == paper and computer_choice == scissors:
    print("The user has chosen\n" + user_choice + "\nThe computer has chosen\n" + computer_choice + "\nThe Computer wins")
  elif user_choice == scissors and computer_choice == rock:
    print("The user has chosen\n" + user_choice + "\nThe computer has chosen\n" + computer_choice + "\nThe Computer wins")
  elif user_choice == scissors and computer_choice == paper:
    print("The user has chosen\n" + user_choice + "\nThe computer has chosen\n" + computer_choice + "\nThe User wins")
  elif user_choice == scissors and computer_choice == scissors:
    print("The user has chosen\n" + user_choice + "\nThe computer has chosen\n" + computer_choice + "\nIt is a tie")
  else:
    print("Unknown error")