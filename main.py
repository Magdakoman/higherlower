import random
from art import logo
from art import vs
from game_data import data
from replit import clear


print(logo)
name= ''
country= ''
description= ''
follower_count= ''
answer=''
winner = ''
end_game= False
score = 0
def draw_participant():
    return random.choice(data)

def print_participant(participant):
    return f": {participant['name']}, a {participant['description']}, from {participant['country']}"


def compare_participant(participant1, participant2):
  global winner
  global end_game
  global score
  print("Compare A" + {print_participant(participant1)})
  print(vs)
  print("Against B" + {print_participant(participant2)})
  answer = input("Who has more followers? Type 'A' or 'B'").lower()
  if answer == "a":
    if participant1['follower_count'] > participant2['follower_count']:
      print("Answer correct")
      winner = participant1
      score += 1
    else:
      print("Incorrect. Game over.")
      end_game = True
  else:
    if participant1['follower_count'] < participant2['follower_count']:
      print(f"Answer correct. Your score is {score}")
      winner = participant2
    else:
      print(f"Incorrect. Game over, your score is {score}")
      end_game = True

participantA = draw_participant()
participantB= draw_participant()

compare_participant(participantA, participantB)

while not end_game:
  new_participant = draw_participant()
  clear()
  compare_participant(winner, new_participant)




