import random
import Play_Music_Module
lis = ["Rock", "Paper", "Scissor"]
A = random.choice(lis)
print("WELCOME TO ROCK PAPER SCISSOR GAME")
print("___________________________________")
name = input("Enter your name please: ")
print("___________________________________")
rounds = 9
user_score = 0
computer_score = 0
print(f"You Have Total {rounds +1} rounds")
print(f"Your Score is {user_score}")
print(f"Computer's Score is {computer_score}")
print("____________________________________")

while rounds <= 10:

    choice = input("Please choose one of the following:\n'Rock'\n'Paper'\n'Scissor': ").title()
    print("____________________________________")
    if choice == 'Rock' and A == 'Rock':
        print("Match Drawn")
        print("No one Got the point")
        print(f"Your Score is {user_score}")
        print(f"Computer's Score is {computer_score}")
        print(f"{rounds} rounds left")
        print("____________________________________")
        Play_Music_Module.draw_music()

    elif choice == "Rock" and A == 'Paper':
        print("You Loose")
        print(f"You choose {choice} and computer chooses {A}")
        print("Computer got the point")
        print(f"Your Score is {user_score}")
        computer_score += 1
        print(f"Computer's score is {computer_score}")
        print(f"{rounds} rounds left")
        print("____________________________________")
        Play_Music_Module.loosing_music()

    elif choice == "Rock" and A == 'Scissor':
        print("You Won")
        print(f"You choose {choice} and computer chooses {A}")
        print("You got the point")
        user_score += 1
        print(f"Your Score is {user_score}")
        print(f"Computer's score is {computer_score}")
        print(f"{rounds} rounds left")
        print("____________________________________")
        Play_Music_Module.win_music()

    elif choice == "Paper" and A == 'Rock':
        print("You Won")
        print(f"You choose {choice} and computer chooses {A}")
        print("You got the point")
        user_score += 1
        print(f"Your Score is {user_score}")
        print(f"Computer's score is {computer_score}")
        print(f"{rounds} rounds left")
        print("____________________________________")
        Play_Music_Module.win_music()

    elif choice == "Paper" and A == 'Paper':
        print("Match drawn")
        print(f"You choose {choice} and computer chooses {A}")
        print("No one got the point")
        print(f"Your Score is {user_score}")
        print(f"Computer's score is {computer_score}")
        print(f"{rounds} rounds left")
        print("____________________________________")
        Play_Music_Module.draw_music()

    elif choice == "Paper" and A == 'Scissor':
        print("You Lost")
        print(f"You choose {choice} and computer chooses {A}")
        print("Computer got the point")
        print(f"Your Score is {user_score}")
        computer_score += 1
        print(f"Computer's score is {computer_score}")
        print(f"{rounds} rounds left")
        print("____________________________________")
        Play_Music_Module.loosing_music()

    elif choice == "Scissor" and A == 'Rock':
        print("You Lost")
        print(f"You choose {choice} and computer chooses {A}")
        print("Computer got the point")
        print(f"Your Score is {user_score}")
        computer_score += 1
        print(f"Computer's score is {computer_score}")
        print(f"{rounds} rounds left")
        print("____________________________________")
        Play_Music_Module.loosing_music()

    elif choice == "Scissor" and A == 'Paper':
        print("You Won")
        print(f"You choose {choice} and computer chooses {A}")
        print("You got the point")
        user_score += 1
        print(f"Your Score is {user_score}")
        print(f"Computer's score is {computer_score}")
        print(f"{rounds} rounds left")
        print("____________________________________")
        Play_Music_Module.win_music()

    elif choice == "Scissor" and A == 'Scissor':
        print("Match Drawn")
        print(f"You choose {choice} and computer chooses {A}")
        print("No one got the point")
        print(f"Your Score is {user_score}")
        print(f"Computer's score is {computer_score}")
        print(f"{rounds} rounds left")
        print("____________________________________")
        Play_Music_Module.draw_music()

    else:
        print("Invalid Input. Please Try Again")
        print("____________________________________")
        Play_Music_Module.alert_music()
        continue

    if rounds == 0:
        print("GAME OVER")
        break
    rounds = rounds - 1

# Making Match Report
print("___________MATCH RESULT_____________")
print("Total Rounds Played: 10")
print(f"{name.upper()} got {user_score} points")
print(f"Computer got {computer_score} points")
if user_score > computer_score:
    print(f"CONGRATULATIONS!!!\n{name.upper()} WON")
    Play_Music_Module.victory_music()
elif user_score < computer_score:
    print(f"OOOPS!!!\nComputer Won\nBetter Luck Next Time")
    Play_Music_Module.defeat_music()
elif user_score == computer_score:
    print(f"WOOW!!!\n{name.upper()} and Computer got same points\nMATCH DRAWN")
    Play_Music_Module.match_drawn_music()



