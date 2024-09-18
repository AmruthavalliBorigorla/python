def intro():
    print("\nWelcome to 'Choose Your Own Adventure'!")
    print("You are standing at the edge of a dark forest. You can either:")
    print("1. Enter the forest.")
    print("2. Walk along the path beside the forest.")
    return choice_input(["1", "2"])

def enter_forest():
    print("\nYou walk into the dark forest. After a few minutes, you come across a fork in the road. Do you:")
    print("1. Take the path to the left.")
    print("2. Take the path to the right.")
    return choice_input(["1", "2"])

def walk_path():
    print("\nYou walk along the path beside the forest and reach a small village. There is a tavern and a marketplace. Do you:")
    print("1. Go to the tavern.")
    print("2. Explore the marketplace.")
    return choice_input(["1", "2"])

def left_path():
    print("\nYou take the left path and find a hidden treasure chest! You open it and find gold coins.")
    print("Congratulations! You have won the game by finding treasure!")
    play_again()

def right_path():
    print("\nYou take the right path and encounter a wild bear. You try to run, but it's too late. The bear catches up to you.")
    print("You have lost the game!")
    play_again()

def tavern():
    print("\nYou enter the tavern and meet a mysterious stranger. They offer you a drink and ask if you want to hear about a secret treasure. Do you:")
    print("1. Accept the drink and listen to the story.")
    print("2. Politely decline and leave the tavern.")
    return choice_input(["1", "2"])

def marketplace():
    print("\nYou explore the marketplace and buy some useful supplies for your journey. You feel more prepared for what lies ahead.")
    print("Congratulations! You have successfully prepared for future adventures!")
    play_again()

def accept_drink():
    print("\nYou accept the drink and listen to the stranger's story. They tell you about a hidden treasure deep in the forest.")
    print("Excited, you decide to set out on a new adventure. Good luck!")
    play_again()

def decline_drink():
    print("\nYou politely decline and leave the tavern. As you exit, you realize that sometimes it's better to stay safe.")
    print("The game ends here. Thanks for playing!")
    play_again()

def choice_input(valid_choices):
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please try again.")

def play_again():
    print("\nWould you like to play again?")
    choice = input("Enter 'yes' to play again or 'no' to quit: ").strip().lower()
    if choice == 'yes':
        start_game()
    else:
        print("Thanks for playing! Goodbye.")
        exit()

def start_game():
    choice = intro()

    if choice == "1":
        choice = enter_forest()
        if choice == "1":
            left_path()
        elif choice == "2":
            right_path()
    elif choice == "2":
        choice = walk_path()
        if choice == "1":
            choice = tavern()
            if choice == "1":
                accept_drink()
            elif choice == "2":
                decline_drink()
        elif choice == "2":
            marketplace()

if __name__ == "__main__":
    start_game()
