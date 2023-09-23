#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random 

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = []
for _ in range(len(chosen_word)):
  display += "_"
print(display)

# check if there has no more blanks "_"
def check_completion():
  check = True
  for _ in display:
    if _ == "_":
      check = False
  return check

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
life = len(chosen_word)

while not check_completion() and life > 0:
  guess = input("Guess a letter: ").lower()
  right_guess = False
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] =letter
      right_guess = True
  life -= 1
  if not right_guess and life > 0:
    print("Try again")
  print(f"Life remaining: {life}")
  print(display)

#game completed
if check_completion():
    print("You won!!")
else:
  print("You lose")
