from contestant import User
from contestant import Wopr
import time
from validate_input import get_valid_integer

class Game():
    def __init__(self) -> None:
        self.round = 0
        self.keep_playing = True
        self.total_number_of_rounds = 0
        self.number_of_players = -1
        self.number_of_rounds_to_victory = -1

    def run_game(self):

        while self.keep_playing:
            
            if self.total_number_of_rounds == 0:
                # Step 1: Display Welcome Message    
                self.user_greeting()
                # Step 2: Display Rules
                self.display_rules()
                
            # Step 3: Prompt User for # Players
            self.determine_number_of_players()
            # Step 4: Ask user how many rounds
            self.determine_number_of_rounds()
            # Step 5: Set up the contestant classes
            self.setup_contestants()
        #     # Step 6: Play Game
        #     winner = self.play_rpsls()
        #     # Step 7: Display Winner
        #     self.victory_message()
        #     # Step 8: Play again
        #     self.play_again()
        
        # # Step 9: Goodbye
        # self.end_game()

        return

    # Step 1
    def user_greeting(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock. An odd twist on a classic game')
        return

    # Step 2
    def display_rules(self):
        print('Rules of the Game \n---------------------')
        print('Each user gets to select either Rock/Scissors/Paper/Lizard/Spock')
        print('The results are:')
        time.sleep(1)
        print('ROCK crushes SCISSORS')
        time.sleep(1)
        print('SCISSORS cuts PAPER')
        time.sleep(1)
        print('PAPER covers ROCK')
        time.sleep(1)
        print('ROCK crushes LIZARD')
        time.sleep(1)
        print('LIZARD poisons SPOCK')
        time.sleep(1)
        print('SPOCK smashes SCISSORS')
        time.sleep(1)
        print('SCISSORS decapitates LIZARD')
        time.sleep(1)
        print('LIZARD eats PAPER')
        time.sleep(1)
        print('PAPER disproves SPOCK')
        time.sleep(1)
        print('SPOCK vaporizes ROCK')
        time.sleep(1)
        print('Play continues in a best of format until one player beats the other')
        return

    def determine_number_of_players(self):
        print('Please enter the number human players')
        print('(0) for no players (computer plays both sides)')
        print('(1) for 1 human player versus the computer')
        print('(2) for human player versus human player')
        user_message = 'Enter a 0,1,or 2: '
        num = get_valid_integer(user_message,range(0,3),True)
        if num == 0:
            print('Computer will play both sides. Enjoy this exciting game!')
        elif num == 1:
            print("It's you versus the computer. Good Luck!!")
        else:
            print("Congratulations! You have a friend! You may not have one after this game!!")
        self.number_of_players =  num
        return

    def determine_number_of_rounds(self):
        print('How long to you want this game to last?')
        user_message = ('Enter the total number of rounds (must be an ODD number) ')
        number_of_rounds = get_valid_integer(user_message,range(1,1000,2),True)
        self.number_of_rounds_to_victory = round(number_of_rounds/2)
        self.total_number_of_rounds = number_of_rounds
        return

    def setup_contestants(self):
        if self.number_of_players == 0:
            player_1 = Wopr('-1')
            player_2 = Wopr('-2')
        elif self.number_of_players == 1:
            name_1 = input('Please enter the name of Player #1: ')
            player_1 = User(name_1)
            player_2 = Wopr()
        else:
            name_1 = input('Please enter the name of Player #1: ')
            player_1 = User(name_1) 

            name_2 = input('Please enter the name of Player #2: ')
            player_2 = User(name_2) 

        print(f"It's {player_1.name} vs. {player_2.name} in a best of {self.total_number_of_rounds} round battle of")
        print('Rock, Paper, Scissors, Lizard, Spock') 
        return   
    

        


