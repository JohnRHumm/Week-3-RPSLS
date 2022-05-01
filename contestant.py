from validate_input import get_valid_integer
from gesture import Rock
from gesture import Paper
from gesture import Scissors
from gesture import Lizard
from gesture import Spock

class Contestant:
    def __init__(self) -> None:
        self.number_of_wins = 0
        rock = Rock()
        paper = Paper()
        scissors = Scissors()
        lizard = Lizard()
        spock = Spock()
        self.gesture_list = [rock,paper,scissors,lizard,spock]
        self.round_victory_list = []
        self.win_count_by_round = [0]
        self.show_choice = True
    
    def select_choice(self):
        pass

    def summary_of_gesture_choices(self):
        summary_list = []
        gesture_list = []
        number_list = []
        for gesture in self.gesture_list:
            print(f'{gesture.name} --> {gesture.number_of_times_selected} times')
            gesture_list.append(gesture.name)
            number_list.append(gesture.number_of_times_selected)
        summary_list = (gesture_list,number_list)
        return summary_list


class User(Contestant):
    def __init__(self,name) -> None:
        super().__init__()
        self.name =  name
    
    def select_choice(self):
        index = 0
        print(f'{self.name} can choose from the following options: ')
        for gesture in self.gesture_list:
            index += 1
            print(f'{index}: {gesture.name}')
        message_to_user = (f'Please select a number between 1 and {index} ')
        user_choice = get_valid_integer(message_to_user,range(1,index+1),True)
        selected_gesture_index = user_choice - 1
        selected_gesture = self.gesture_list[selected_gesture_index]
        self.gesture_list[selected_gesture_index].number_of_times_selected += 1
        if self.show_choice:
            print(f'{self.name} has selected {self.gesture_list[selected_gesture_index].name}')
        return selected_gesture

class Wopr(Contestant):
    def __init__(self,name) -> None:
        super().__init__()
        self.name =  'Joshua' + name
    
    def select_choice(self):
        index = 0
        for gesture in self.gesture_list:
            index += 1
        user_choice = get_valid_integer('',range(1,index+1),False)
        selected_gesture_index = user_choice - 1
        selected_gesture = self.gesture_list[selected_gesture_index]
        self.gesture_list[selected_gesture_index].number_of_times_selected += 1
        print(f'{self.name} has selected {self.gesture_list[selected_gesture_index].name}')
        return selected_gesture

            

        



