class Gesture():
    def __init__(self) -> None:
        self.name =''
        
    def determine_winner(self,opponent_choice):
        pass

class Rock(Gesture):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Rock'

    def determine_winner(self,opponent_choice):
        if opponent_choice.name == 'Scissors':
            print('Rock crushes Scissors')
            win_result = True
        elif opponent_choice.name == 'Lizard':
            print('Rock crushes Lizard')
            win_result = True
        elif opponent_choice.name == 'Paper':
            print('Paper covers Rock')
            win_result = False
        elif opponent_choice.name == 'Spock':
            print('Spock vaporizes Rock')
            win_result = False
        else:
            print('No valid option')
            win_result = ''
        return win_result

class Paper(Gesture):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Paper'

    def determine_winner(self,opponent_choice):
        if opponent_choice.name == 'Rock':
            print('Paper covers Rock')
            win_result = True
        elif opponent_choice.name == 'Spock':
            print('Paper disproves Spock')
            win_result = True
        elif opponent_choice.name == 'Scissors':
            print('Scissors cuts Paper')
            win_result = False
        elif opponent_choice.name == 'Lizard':
            print('Lizard eats Paper')
            win_result = False
        else:
            win_result = ''
        return win_result

class Scissors(Gesture):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Scissors'

    def determine_winner(self,opponent_choice):
        if opponent_choice.name == 'Paper':
            print('Scissors cuts Paper')
            win_result = True
        elif opponent_choice.name == 'Lizard':
            print('Scissors decapitates Lizard')
            win_result = True
        elif opponent_choice.name == 'Rock':
            print('Rock crushes Scissors')
            win_result = False
        elif opponent_choice.name == 'Spock':
            print('Spock smashes Scissors')
            win_result = False
        else:
            win_result = ''
        return win_result 

class Lizard(Gesture):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Lizard'

    def determine_winner(self,opponent_choice):
        if opponent_choice.name == 'Paper':
            print('Lizard eats Paper')
            win_result = True
        elif opponent_choice.name == 'Spock':
            print('Lizard poisons Spock')
            win_result = True
        elif opponent_choice.name == 'Rock':
            print('Rock crushes Lizard')
            win_result = False
        elif opponent_choice.name == 'Scissors':
            print("Scissors decapitates Lizard")
            win_result = False
        else:
            win_result = ''
        return win_result 

class Spock(Gesture):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Spock'

    def determine_winner(self,opponent_choice):
        if opponent_choice.name == 'Rock':
            print('Spock vaporizes Rock')
            win_result = True
        elif opponent_choice.name == 'Scissors':
            print('Spock smashes Scissors')
            win_result = True
        elif opponent_choice.name == 'Paper':
            print('Paper disproves Spock')
            win_result = False
        elif opponent_choice.name == 'Lizard':
            print('Lizard poisons Spock')
            win_result = False
        else:
            win_result = ''
        return win_result 


