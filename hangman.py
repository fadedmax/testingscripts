

def get_guess():

  dashes = "-" * len(secret_word)
  guesses_left = 10
  

  while guesses_left > -1 and not dashes == secret_word:
    
    print(dashes)
    print (str(guesses_left))

    guess = input("Guess:")
    

    if len(guess) != 1:
      print ("Your guess must have exactly one character!")
      

    elif guess in secret_word:
      print ("That letter is in the secret word!  ***")
      dashes = update_dashes(secret_word, dashes, guess)
      

    else:
      print ("That letter is not in the secret word!  XXX")
      guesses_left -= 1
    
  if guesses_left < 0:
    print ("You lose. The word was: " + str(secret_word))
    start()
  

  else:
    print ("Congrats! You win. The word was: " + str(secret_word))
    print ("Begginging Next Game")
    start()
    

def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     # Adds guess to string if guess is correctly
      
    else:
      # Add the dash at index i to result if it doesn't match the guess
      result = result + cur_dash[i]
      
  return result

def start():
  import random
  choicefile=open("words_alpha.txt","r")
  linelist=[]
  for line in choicefile:
      linelist.append(line) 
  choice=random.choice(linelist)
  secret_word = choice
  get_guess()

start()

