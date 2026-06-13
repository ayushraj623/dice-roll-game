# main.py
import game_logic as gl # Importing your package

def display_menu():
    print("\n" + "="*25)
    print("   DICE ROLL MENU")
    print("="*25)
    print("1. Play Game")
    print("2. multiplaer mode")
    print("3. exit")
    print("="*25)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1 ,2 or 3): ")

        if choice == '1':
            # --- Game Interaction ---
            user_roll =gl.roll_dice() 
            
                
                # Using the logic from your imported package
            comp_roll = gl.roll_dice()
            result = gl.check_winner1(user_roll, comp_roll)
                
            print(f"\nResult: {result}")
        elif choice =='2':
            user1dice=gl.roll_dice()
            user2dice=gl.roll_dice()
            result=gl.check_winner2(user1dice,user2dice)
            print(f"\nResult:{result}")                
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break  # Breaks the infinite loop
            
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()