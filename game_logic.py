# game_logic.py
import random

def roll_dice():
    return random.randint(1, 6)

def check_winner1(user_roll, comp_roll):
    print(f"Your dice: {user_roll}")
    print(f"Computer dice: {comp_roll}")
    
    if user_roll > comp_roll:
        return "You win! 🎉"
    elif user_roll < comp_roll:
        return "Computer wins! 🤖"
    else:
        return "It's a draw! 🤝"
def check_winner2(user_roll, user2_roll):
    print(f"user 1 dice: {user_roll}")
    print(f"user 2 dice: {user2_roll}")
    
    if user_roll > user2_roll:
        return "user 1 win! 🎉"
    elif user_roll < user2_roll:
        return "user 2 wins! 🤖"
    else:
        return "It's a draw! 🤝"
    