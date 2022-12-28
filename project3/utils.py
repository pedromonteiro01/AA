import string

def get_upper_letters(file):
  # open the text file
  with open(file, 'r') as f:
    text = f.read()

  words = text.split()
  letters = []

  for word in words:
    for char in word: # iterate all chars
      if char not in string.punctuation and char.isalpha(): # check if char is not a punctuation mark
        letters.append(char.upper())

  # return list of all letters
  return letters

get_upper_letters("pg69638.txt")