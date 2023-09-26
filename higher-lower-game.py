from random import randint
import random
from game_data import data
from replit import clear
from art import logo

#function to check highers follower count
def compare_options(option_a, option_b):
  """Compare the follower counts"""
  if option_a["follower_count"] > option_b["follower_count"]:
    return "a"
  else:
    return "b"

score = 0
continue_play = True
option_a = random.choice(data)
option_b = random.choice(data)
multiple = 0
while continue_play:
  print(logo)
  clear()
  def game_play():
    global continue_play
    global score
    global option_a
    global option_b
    global multiple
    #print(f"this is multiple {multiple}")
    #retrieve computer answer
    answer = compare_options(option_a, option_b)
    print(f"Compare A: {option_a['name']}, {option_a['description']} from {option_a['country']}")
    print("""
  .-.   .-..----. 
   \ \_/ /{ {__-` 
    \   / .-._} } 
     `-'  `----'  
                  
  """)
    
    print(f"Compare b: {option_b['name']}, {option_b['description']} from {option_b['country']} \n")
    choice = input("Who has more followers? Type 'A' or 'B':")
    if choice == answer:
#set the new option_a
      if answer == "a":
        #print("yes")
        multiple += 1
#check if option_a has been picked 2 times and set a new random option_a
        if multiple > 2:
          option_a = random.choice(data)
          multiple = 0
        else:
          option_a = option_a
          
      else:
        option_a = option_b
#set a new random option-b       
      option_b = random.choice(data)
      while option_a == option_b:
        option_b = random.choice(data)    
      score += 1
    else:
      continue_play = False
      print(f"Your score: {score}")
      print("game Over")
  print(f"Your score: {score}")
  game_play()    
      
    
    
