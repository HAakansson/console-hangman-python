import random  # Module for generating random values.
import re  # Module needed using regular expressions.

# ---------- START of variable declarations for my program ----------

words = [
  "boat",
  "car",
  "airplane",
  "truck",
  "bicycle",
  "scooter",
  "motorcycle",
  "train",
  "freight",
  "ship",
  "cruiser"
]

# random.randint(start, stop), returns a random value between the both parameters, and both are included.
secret_word = words[random.randint(0, len(words) - 1)]
max_misses = 11
misses = 0
attempts = 0
public_word = re.sub("\D", "_", secret_word)
word_is_correct = False
used_letters = []

# --------- END of variables declaration ----------

# ---------- START of Help methods ----------

def check_if_letter_is_already_guessed(letter):
  '''
  This method checks if the letter that has been guessed already exists in the used_letter-array.
  '''
  return letter in used_letters

def does_letter_exists(letter):
  '''
  This method checks if the letter that has been guessed exists in the secret_word.
  '''
  return letter in secret_word

def get_indexes_of_letters(letter):
  '''
  This methods returns an array with the indexes of the guessed letter, if it exists that is.
  '''
  indexes = []
  for index in range(len(secret_word)):
    if letter == secret_word[index]:
      indexes.append(index)
  return indexes

def replace_underscores_with_letter(letter):
  '''
  This method takes in a letter and replaces all the underscores that match with the letter. It then returns the new public_word string.
  '''
  indexes = get_indexes_of_letters(letter)
  public_word_array = list(public_word)
  for index in indexes:
    public_word_array[index] = letter
  return "".join(public_word_array)

def guess_letter():
  '''
  The method responsible for taking in an input from the user and return it to the program.
  '''
  guess = None
  regex = re.compile("[^a-zA-Z]")
  guess_again = True

  while guess_again:
    guess = input("Type in your guess: ")
    if check_if_letter_is_already_guessed(guess):
      print("The letter has already been guessed.")
    elif regex.search(guess) and len(guess) > 1:
      print("ERROR - You are only allowed to enter letters and ONE only.")
    elif regex.search(guess):
      print("ERROR - Only letters are allowed.")
    elif len(guess) > 1:
      print("ERROR - Only ONE letter is allowed.")
    else: guess_again = False

  used_letters.append(guess)
  return guess

def print_public_word():
  '''
  Responsible for printing the pubic word, inlucding the underscores for letters to be guessed.
  '''
  # The list(public_word) typecastes the public_word to a list of each individual letter. .join() is a string method that joins all the elements in a given string or list with the given seperator - which is the string that .join() is been applied to. 
  print(" ".join(list(public_word)))

def check_if_secret_word_is_complete():
  return secret_word == public_word

# ---------- END of help methods ----------

# ---------- START of program code ----------

print("Welcome to a game of hangman! The secret word has been set, leeeeet's guess!")
print_public_word()

while not word_is_correct:
  if used_letters:
    print("Used letters: {}".format(used_letters));
    print(f"{max_misses - misses} misses left till you are hanged.m")

  letter = guess_letter()
  attempts += 1

  if does_letter_exists(letter):
    print("HIT!")
    public_word = replace_underscores_with_letter(letter)
    print_public_word()

    if check_if_secret_word_is_complete():
      print("CONGRATULATIONS! You have guessed the entire word!")
      print(f"It took you {attempts} attempts to guess the secret word!")
      word_is_correct = True
      
  else:
    print("MISS!")
    misses += 1
    if misses == max_misses:
      print("GAME OVER! You have been hanged!")
