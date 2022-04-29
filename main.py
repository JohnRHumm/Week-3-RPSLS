from gesture import Paper
from gesture import Lizard

paper = Paper()
print (f'P1 = {paper.name}')
lizard = Lizard()
print (f'P2 = {lizard.name}')

result = paper.determine_winner(lizard)
i = 1