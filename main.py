from gesture import Paper
from gesture import Lizard
from contestant import User
from contestant import Wopr

# paper = Paper()
# print (f'P1 = {paper.name}')
# lizard = Lizard()
# print (f'P2 = {lizard.name}')

# result = paper.determine_winner(lizard)
# i = 1

u1 = User('JH')
joshua = Wopr('1')



c1 = u1.select_choice()

c2 = joshua.select_choice()
result_of_battle = c1.determine_winner(c2)

# result_of_battle = u1.gesture_list[c1].determine_winner(joshua.gesture_list[c2])
print(f'{result_of_battle}')
i = 1