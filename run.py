import pyfiglet
from LuckyNumber import LuckyNumbers
from resources.game_rule import games

# Define a variable which contains the instruction to use.

init_question = '''
Please choose the game you want to generate number from.
[1] Lotto 6/42
[2] Mega Lotto 6/45
[3] Super Lotto 6/49
[4] Grand Lotto 6/55
[5] Ultra Lotto 6/58
'''

thank_you_message = '''
Thank you for using this simple lotto number generator.
Feel free to use the code in your own learnings.
'''

# This function intented to display banner every time this python file run.
def show_banner():
    # Assigning the string to display in the banner.
    ascii_title = pyfiglet.figlet_format("Lotto Number Generator")

    # Now printing the banner and the instruction.
    print(ascii_title)
    print(init_question)

def main():
    # This while loop will be used like do while loop.
    while True:
        # First it will ask client desired game.
        lotto_game = input("Enter the number : ")
        
        # It will just proceed if the user enter valid input otherwise it
        # will continue asking for the right input.
        if lotto_game in games.keys():
            break  
    
    # We are now instantiating the class LuckyNumbers
    new_number_set = LuckyNumbers(lotto_game)

    # Here we assign the return value of the called property (generate_number)
    # of the class LuckyNumbers
    lucky_number = new_number_set.generate_number()

    # Here we will diplay the randomly pick 6 digit number in a list form.
    print(lucky_number)

# This function serves as the starting point of this simple application.
def start():
    show_banner() 
    lotto_game = None     # This will hold the value of the user input.

    main()
    
    while True:
        # We will ask the user if he/she wish to generate again.
        try_again = input("You want to generate again? [y/n] : ")
        
        # This If else condition will decide if the user which to continue or not.
        if try_again in ['Y','y']:
            main()
        elif try_again in ['N','n']:
            break
        else:
            pass

    message = pyfiglet.figlet_format("Goodbye God blessed")
    print(message)
    print(thank_you_message)

if __name__ == "__main__":
    start()
