import random

def get_computer_selection():
	options = ["rock", "paper", "scissors"]
	return random.choice(options)

user_score = 0
computer_score = 0
tie = 0

while True:

	user_selection = input("\nChoose one among 'rock', 'paper', 'scissors': ").lower()
	computer_selection = get_computer_selection()
	print("\nThe computer chooses: ",computer_selection)

	if((computer_selection == "rock" and user_selection == "paper") or (computer_selection == "paper" and user_selection == "scissors") or (computer_selection == "scissors" and user_selection == "rock")):
		print("\nYou won!!")
		user_score += 1
	elif((computer_selection == "rock" and user_selection == "scissors") or (computer_selection == "scissors" and user_selection == "paper") or (computer_selection == "paper" and user_selection == "rock")):
		print("\nComputer Won!!")
		computer_score += 1
	elif((computer_selection == "rock" and user_selection == "rock") or (computer_selection == "paper" and user_selection == "paper") or (computer_selection == "scissors" and user_selection == "scissors")):
		print("\nIt's a tie....")
		tie += 1

	print(f"\nComputer score is: {computer_score}")
	print(f"Your score is: {user_score}")
	print(f"Tie score is: {tie}")

	play_again = input("\nDo you want to play again? (yes/no): ").lower()
	if play_again != "yes":
		print(f"\nFinal score is: ")
		print(f"Computer score is: {computer_score}")
		print(f"Your score is: {user_score}")
		print(f"Tie score is: {tie}")
		print("Thanks for playing")
		break
