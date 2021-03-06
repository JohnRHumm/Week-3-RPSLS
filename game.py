from contestant import User
from contestant import Wopr
from contestant import Contestant
import time
from validate_input import get_valid_integer
from validate_input import get_y_or_n_from_user
try:
    import matplotlib.pyplot as plt
    import_matplotlib = True
except:
    import_matplotlib = False
try:
    import numpy as np
    import_numpy = True
except:
    import_numpy = False
if import_matplotlib and import_numpy:
    make_plots = True
else:
    make_plots = False
class Game():
    def __init__(self) -> None:
        self.round = 0
        self.keep_playing = True
        self.total_number_of_rounds = 0
        self.number_of_players = -1
        self.number_of_rounds_to_victory = -1
        self.player_1 = Contestant()
        self.player_2 = Contestant()
        self.number_of_ties = 0

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
            # Step 6: Play Game
            winner = self.play_rpsls()
            # Step 7: Display Winner
            self.victory_message()
            # Step 8: Show Game Statistics
            self.show_statistics()
            # Step 9: Play again
            self.play_again()
        
        # Step 10: Goodbye
        self.end_game()

        return

    # Step 1
    def user_greeting(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock. An odd twist on a classic game')
        time.sleep(2)
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
        print('---------------------\n')
        time.sleep(1)
        return

    # Step 3
    def determine_number_of_players(self):
        print('Please enter the number human players')
        print('(0) for no players (computer plays both sides)')
        print('(1) for 1 human player versus the computer')
        print('(2) for human player versus human player')
        user_message = 'Enter a 0,1,or 2: '
        time.sleep(2)
        num = get_valid_integer(user_message,range(0,3),True)
        if num == 0:
            print('Computer will play both sides. Enjoy this exciting game!\n')
        elif num == 1:
            print("It's you versus the computer. Good Luck!!\n")
        else:
            print("Congratulations! You have a friend! You may not have one after this game!!\n")
        time.sleep(2)
        self.number_of_players =  num
        return

    # Step 4
    def determine_number_of_rounds(self):
        print('How long do you want this game to last?')
        user_message = ('Enter the total number of rounds (must be an ODD number 1-5001) ')
        number_of_rounds = get_valid_integer(user_message,range(1,5002,2),True)
        self.number_of_rounds_to_victory = int((number_of_rounds + 1)/2)
        self.total_number_of_rounds = number_of_rounds
        print(f'The first contestant to win {self.number_of_rounds_to_victory} rounds wins the game!\n')
        time.sleep(2)
        return

    # Step 5
    def setup_contestants(self):
        if self.number_of_players == 0:
            self.player_1 = Wopr(' 1.0')
            self.player_2 = Wopr(' 2.0')
        elif self.number_of_players == 1:
            name_1 = input('Please enter the name of Player #1: ')
            self.player_1 = User(name_1)
            self.player_2 = Wopr('')
        else:
            name_1 = input('Please enter the name of Player #1: ')
            self.player_1 = User(name_1) 
            self.player_1.show_choice = False

            name_2 = input('Please enter the name of Player #2: ')
            self.player_2 = User(name_2) 
            self.player_2.show_choice = False

        print(f"It's {self.player_1.name} vs. {self.player_2.name} in a best of {self.total_number_of_rounds} round battle of")
        print('Rock, Paper, Scissors, Lizard, Spock\n')
        time.sleep(2) 
        return   
    
    # Step 6 --> This is the actual game
    def play_rpsls(self):
        while self.player_1.number_of_wins < self.number_of_rounds_to_victory  and self.player_2.number_of_wins < self.number_of_rounds_to_victory:
            self.round += 1
            print(f'\033[1;37;44m Round {self.round} Summary: {self.player_1.name} - {self.player_1.number_of_wins} wins vs. {self.player_2.name} - {self.player_2.number_of_wins} wins \033[0m')
            time.sleep(1)
            players_keep_selecting = True
            while players_keep_selecting:
                gesture_p1 = self.player_1.select_choice()
                time.sleep(1)
                gesture_p2 = self.player_2.select_choice()
                time.sleep(1)
                if gesture_p1.name == gesture_p2.name:
                    print(f'Both contestants chose {gesture_p1.name}\n Please re-select')
                    self.number_of_ties += 1
                    time.sleep(2)
                else:
                    players_keep_selecting = False

            p1_win = gesture_p1.determine_winner(gesture_p2)
            time.sleep(2)
            if p1_win:
                print(f'\033[1;37;41m {self.player_1.name} wins Round {self.round} !!! \033[0m\n')
                self.player_1.number_of_wins += 1
                self.player_1.round_victory_list.append(self.round)
            else:
                print(f'\033[1;30;43m {self.player_2.name} wins Round {self.round} !!! \033[0m\n')
                self.player_2.number_of_wins += 1
                self.player_2.round_victory_list.append(self.round) 
            self.player_1.win_count_by_round.append(self.player_1.number_of_wins)
            self.player_2.win_count_by_round.append(self.player_2.number_of_wins)
            time.sleep(2)

    # Setp 7
    def victory_message(self):
        print(f'\033[1;37;44m  The game is over \033[0m\n')
        if self.player_1.number_of_wins == self.number_of_rounds_to_victory:
            print(f'{self.player_1.name} won the best of {self.total_number_of_rounds} by a score of {self.player_1.number_of_wins} to {self.player_2.number_of_wins} ')
            print(f'\033[1;37;41m Congratulations to {self.player_1.name} \033[0m')
        else:
            print(f'{self.player_2.name} won the best of {self.total_number_of_rounds} by a score of {self.player_2.number_of_wins} to {self.player_1.number_of_wins} ')
            print(f'\033[1;30;43m Congratulations to {self.player_2.name} \033[0m')   
        time.sleep(2) 
        return

    # Step 8 First try at plotting graphs in python need numpy and matplotlib
    def show_statistics(self):
        print('----Game Summary Statistics----')
        print(f'{self.player_1.name} won rounds')
        time.sleep(2)
        print(*self.player_1.round_victory_list,sep =',')
        print(f'{self.player_2.name} won rounds')
        time.sleep(2)
        print(*self.player_2.round_victory_list,sep =',')
        time.sleep(2)
        print(f'There were {self.number_of_ties} ties\n')
        time.sleep(2)
        print(f'\033[1;37;41m {self.player_1.name} Selection Summary \033[0m')
        player1_gesture_summary = self.player_1.summary_of_gesture_choices()
        
        print('')
        time.sleep(3)
        print(f'\033[1;30;43m {self.player_2.name} Selection Summary \033[0m')
        player2_gesture_summary = self.player_2.summary_of_gesture_choices()
        if make_plots:
            print('Close bar chart to continue')
            x_axis = np.arange(len(player1_gesture_summary[0]))
            plt.bar(x_axis - 0.2,player1_gesture_summary[1],width = 0.4,label = self.player_1.name)
            plt.bar(x_axis + 0.2,player2_gesture_summary[1],width = 0.4,label = self.player_2.name)
            plt.xticks(x_axis,player1_gesture_summary[0])
            plt.ylabel('Number of times selected')
            plt.title('Selection Summary')
            plt.legend()
            plt.show()
           
            print('Close graph to continue')
            fig = plt.figure()
            ax = plt.axes()
            ax.plot(range(0,self.round+1),self.player_1.win_count_by_round,label = self.player_1.name)
            ax.plot(range(0,self.round+1),self.player_2.win_count_by_round,label = self.player_2.name)
            plt.title('Win total by round')
            plt.xlabel('Round')
            plt.ylabel('Number of wins')
            plt.legend()
            plt.grid()
            plt.show()
           

        else:
            print('Install numpy and matplotlib libraries to show graphs')
            
        return
    
    # Step 9 
    def play_again(self):
        message_to_user = ('Do you want to play this awesome game again? Y or N: ')
        play_again = get_y_or_n_from_user(message_to_user)
        if play_again == 'Y':
            self.keep_playing = True
            self.round = 0
            self.number_of_ties = 0
            print("Ok... Let's play again!!")
            print("-------------------------------\n")
        else:
            self.keep_playing = False

           
    # Step 10
    def end_game(self):
        print('Thank you for playing Rock, Scissors, Paper, Lizard, Spock!')
        return




        


