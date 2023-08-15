# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):

  c=[]  
  for i in secret_word:
    if i in letters_guessed:
      c.append(i)
  if sorted(c) == sorted(secret_word):
    return True
  return False
'''secret_word = 'apple' 
letters_guessed = ['e', 'p', 'l', 'p', 'e', 'a'] 
print(is_word_guessed(secret_word, letters_guessed)) '''     




def get_guessed_word(secret_word, letters_guessed):
  c=[]
  x=[]
  for i in secret_word:
    if i in letters_guessed:
      c.append(i)
  for i in secret_word:
    if i in c:
      x.append(i)
    else:
      x.append("_ ")  
  return ''.join(x)
'''secret_word = 'apple'  
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
print(get_guessed_word(secret_word, letters_guessed)) '''
  

    


def get_available_letters(letters_guessed):
  x=list(string.ascii_lowercase)
  p=[]
  for i in x:
    if i in letters_guessed:
      pass
    else:
      p.append(i) 
  return ''.join(p)   


    
    
    

def hangman(secret_word):
  #word=choose_word(wordlist)
  warn=3
  guesses=6
  print("Welcome to the game Hangman! ")
  print("I am thinking of a word that is" ,len(secret_word) ," letters long.")
  print("You have", warn , " warnings left.")
  letters_g =[]
  while(True):
    if(guesses ==0):
      print("Oops! That letter is not in my word: ",get_guessed_word(secret_word,letters_g))
      print("-------------  ")
      print("Sorry, you ran out of guesses. The word was ", secret_word)
      break
    print("-------------  ")
    print("You have ", guesses ," guesses left.")
    print("Available letters: " , get_available_letters(letters_g))
    x=str(input("Please guess a letter "))
    if x in letters_g:
      if(warn == 0):
        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
        guesses-=1
        print(get_guessed_word(secret_word,letters_g))
      else:

        warn -=1
        print("Oops! You've already guessed that letter. You have ", warn ," warnings left: \n",get_guessed_word(secret_word,letters_g)) 
    else:

      letters_g.append(x)
      
    
      if  x in secret_word:

        print("Good guess: " , get_guessed_word(secret_word,letters_g))
        if is_word_guessed(secret_word,letters_g) == True:
          score=guesses * len(set(secret_word))
          print("Congratulations, you won! ")
          print("Your total score for this game is: ",score)
          break

       
      elif str.isalpha(x) == False:
        if(warn ==0):
          guesses -= 1
        warn -= 1
        print("Oops! That is not a valid letter.  You have ", warn ," warnings left: ", get_guessed_word(secret_word,letters_g))
      else:
        if(x in ["a","e","i","o","u"]):
          guesses -=2
          print("Oops! That letter is not in my word \n Please guess a letter:",get_guessed_word(secret_word,letters_g))
        else:
          guesses -=1  
          print("Oops! That letter is not in my word \n Please guess a letter:",get_guessed_word(secret_word,letters_g))
        


   

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
  x=my_word.replace(" ","")
  
  if len(x) == len(other_word):
    for i,k in zip(list(x),list(other_word)):
      if i == k or i == "_":
        pass
      else:
        return False
    return True
  else:
    return False    
match_with_gaps("te_ t", "tact") 
print("a")
match_with_gaps("a_ _ le", "banana")
  



def show_possible_matches(my_word):
  x=len(my_word.replace(" ",""))
  p=[]
  for i in wordlist:
    if x ==len(wordlist):
      p.append(i)
     
  if not p:
    print("No matches found")
  else:
    return p  





def hangman_with_hints(secret_word):

  warn=3
  guesses=6
  print("Welcome to the game Hangman! ")
  print("I am thinking of a word that is" ,len(secret_word) ," letters long.")
  print("You have", warn , " warnings left.")
  letters_g =[]
  while(True):
    if(guesses ==0 or guesses < 0):
      print("Oops! That letter is not in my word: ",get_guessed_word(secret_word,letters_g))
      print("-------------  ")
      print("Sorry, you ran out of guesses. The word was ", secret_word)
      break
    print("-------------  ")
    print("You have ", guesses ," guesses left.")
    print("Available letters: " , get_available_letters(letters_g))
    x=str(input("Please guess a letter "))
    if x in letters_g:
      if(warn == 0):
        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
        guesses-=1
        print(get_guessed_word(secret_word,letters_g))
      else:

        warn -=1
        print("Oops! You've already guessed that letter. You have ", warn ," warnings left: \n",get_guessed_word(secret_word,letters_g)) 
    else:

      letters_g.append(x)
      
    
      if  x in secret_word:

        print("Good guess: " , get_guessed_word(secret_word,letters_g))
        if is_word_guessed(secret_word,letters_g) == True:
          score=guesses * len(set(secret_word))
          print("Congratulations, you won! ")
          print("Your total score for this game is: ",score)
          break

       
      elif str.isalpha(x) == False and x != "*":
        if(warn ==0):
          guesses -= 1
        warn -= 1
        print("Oops! That is not a valid letter.  You have ", warn ," warnings left: ", get_guessed_word(secret_word,letters_g))
      elif x == "*"  :
        print(show_possible_matches(get_guessed_word(secret_word,letters_g)))
      else:
        if(x in ["a","e","i","o","u"]):
          guesses -=2
          print("Oops! That letter is not in my word \n Please guess a letter:",get_guessed_word(secret_word,letters_g))
        else:
          guesses -=1  
          print("Oops! That letter is not in my word \n Please guess a letter:",get_guessed_word(secret_word,letters_g))
        


    


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
   secret_word = choose_word(wordlist)
   hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
