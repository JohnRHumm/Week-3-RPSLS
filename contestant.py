from validate_input import get_valid_integer

class Contestant:
    def __init__(self) -> None:
        self.battle_list = ['Rock','Paper','Scissors','Lizard','Spock']
        self.battle_selection = ''
        self.number_of_wins = 0
        self.current_round_selection =''


class User(Contestant):
    def __init__(self,name) -> None:
        self.name =  name
    
    def battle_round(self):
        index = 0
        print(f'{self.name} can choose from the following options: ')
        for option in self.battle_list:
            index += 1


            

        



