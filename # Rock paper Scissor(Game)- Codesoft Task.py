import random

def play_game():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    print("🎮 Rock-Paper-Scissors Game (Codesoft Task)\n")

    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in choices:
            print("❌ Invalid choice. Try again.")
            continue

        computer = random.choice(choices)
        print(f"🧍 You: {user} | 💻 Computer: {computer}")

        if user == computer:
            print("⚖ It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'scissors' and computer == 'paper') or \
             (user == 'paper' and computer == 'rock'):
            print("✅ You win!")
            user_score += 1
        else:
            print("❌ You lose!")
            computer_score += 1

        print(f"📊 Score: You {user_score} - {computer_score} Computer")

        again = input("Play again? (yes/no): ").lower()
        if again != 'yes':
            print("\n Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

# Start the game
play_game()
