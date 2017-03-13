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
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(letters_guessed) == 0:
      return False
    for i in range(0,len(secret_word)):
      for j in range(0,len(letters_guessed)):
        if secret_word[i] == letters_guessed[j]: # how to enumerate all the letters in b
          break
      if secret_word[i] != letters_guessed[j] and j == len(letters_guessed)-1:
        return False         
    return True
        
      
      
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ''
    if len(letters_guessed) == 0:
      return '_ '*len(secret_word) #Please remember to return result, or when j = 0, i != 0, the second if statement will be excuated 
    
    for i in range(len(secret_word)):
      for j in range(len(letters_guessed)):
        if secret_word[i] == letters_guessed[j]:
          result = result + secret_word[i]
          break
      if secret_word[i] != letters_guessed[j] and j == len(letters_guessed)-1:
        result = result + '_ '        
    return result    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    result = ''
    letters_list = list(string.ascii_lowercase)
    for a in letters_guessed:
      for b in letters_list:
        if a == b:
          letters_list.remove(b)
    result = ''.join(letters_list)
    return result
  
def is_letter_in_word(letter,word):
    '''
    word: string, the secret word to guess.
    letter:string,newly guessed letter
    returns: True if new_letter is in word
    False elsewise 
    
    '''        
    for i in range(len(word)):
      if word[i] == letter:
        return True
      if word[i] != letter and i == len(word)-1:
        return False
        
def num_unique_letters(word):
    '''
    word is a string
    return result = number of unique letters in the word
    '''
    temp_word = []     
    for a in word:
      if a not in temp_word:
        temp_word.append(a)
        
    result = len(temp_word)
    return result
        

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    num_of_guesses = 6
    num_of_warnings = 3
    letters_guessed = []
    vowels = ['a','e','i','o','u']
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    while not is_word_guessed(secret_word,letters_guessed) and num_of_guesses > 0:
      
      print('-------------')
      print('You have', num_of_warnings, 'warnings left.')
      print('You have',num_of_guesses,'guesses left')
      print('Available letters:',get_available_letters(letters_guessed))
      new_letter_guessed = input('Please guess a letter:')
      old_guessed_word = get_guessed_word(secret_word, letters_guessed)
      if not str.isalpha(new_letter_guessed):
        if num_of_warnings != 0:
          num_of_warnings = num_of_warnings - 1
          printinfo(num_of_warnings,old_guessed_word,'That is not a valid letter.')
        else:
          num_of_guesses = num_of_guesses - 1
          printinfo(num_of_warnings,old_guessed_word,'That is not a valid letter.')
      elif new_letter_guessed in letters_guessed:
        if num_of_warnings != 0:
          num_of_warnings = num_of_warnings - 1
          printinfo(num_of_warnings,old_guessed_word,'You already guessed that letter.')
        else:
          num_of_guesses = num_of_guesses - 1
          printinfo(num_of_warnings,old_guessed_word,'You already guessed that letter.')
      else:
        letters_guessed.append(str.lower(new_letter_guessed))
        new_guessed_word = get_guessed_word(secret_word, letters_guessed)
        if is_letter_in_word(str.lower(new_letter_guessed),secret_word):
          print('Good guess:',get_guessed_word(secret_word, letters_guessed))
        elif str.lower(new_letter_guessed) in vowels:
          num_of_guesses = num_of_guesses - 2
          print('Oops! That letter is not in my word:',new_guessed_word)
        else:
          num_of_guesses = num_of_guesses - 1
          print('Oops! That letter is not in my word:',new_guessed_word)
      if is_word_guessed(secret_word,letters_guessed):
        print('-------------')
        print('Congratulations, you won!')
        print('Your total score for this game is:',num_of_guesses * num_unique_letters(secret_word))
      elif not is_word_guessed(secret_word,letters_guessed) and num_of_guesses == 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was else.')
# Whenyou've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_temp = my_word.replace(' ', '')
    if len(my_word_temp) != len(other_word):
      return False
    '''
    4 senarios: my_word_temp[i] == other_word[i] :: bingo
                my_word_temp[i] != other_word[i] and my_word_temp[i] != '_' :: False  
                my_word_temp[i] == '_' and other_word[i] in my_word_temp :: False
                my_word_temp[i] == '_' and other_word[i] not in my_word_temp :: bingo
    '''
    for i in range(len(my_word_temp)):
      if my_word_temp[i] != other_word[i] and my_word_temp[i] != '_':
        return False
      if my_word_temp[i] == '_' and other_word[i] in my_word_temp:
        return False
    return True
      

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    printlist = []
    for word in wordlist:
      if match_with_gaps(my_word,word):
        printlist.append(word)
    if printlist == []: 
      print('No matches found')
    else:
      print(' '.join(printlist))


def print_info(num_of_warnings,old_guessed_word,message):
    '''
    message is a string that tells if failure because of invalid letter or repeated letter
    '''
    if num_of_warnings == 0:
      print('Oops!', message,'You have no warnings left so you lose one guess:',old_guessed_word)
    else:
      print('Oops!', message,'You have', num_of_warnings, 'warnings left:',old_guessed_word)
    

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    num_of_guesses = 6
    num_of_warnings = 3
    letters_guessed = []
    vowels = ['a','e','i','o','u']
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    while not is_word_guessed(secret_word,letters_guessed) and num_of_guesses > 0:
      
      print('-------------')
      print('You have', num_of_warnings, 'warnings left.')
      print('You have',num_of_guesses,'guesses left')
      print('Available letters:',get_available_letters(letters_guessed))
      new_letter_guessed = input('Please guess a letter:')
      old_guessed_word = get_guessed_word(secret_word, letters_guessed)
      if new_letter_guessed == '*':
        print('Possible word matches are:')
        show_possible_matches(old_guessed_word)
      elif not str.isalpha(new_letter_guessed) :
        if num_of_warnings != 0:
          num_of_warnings = num_of_warnings - 1
          print_info(num_of_warnings,old_guessed_word,'That is not a valid letter.')
        else:
          num_of_guesses = num_of_guesses - 1
          print_info(num_of_warnings,old_guessed_word,'That is not a valid letter.')
      elif new_letter_guessed in letters_guessed:
        if num_of_warnings != 0:
          num_of_warnings = num_of_warnings - 1
          print_info(num_of_warnings,old_guessed_word,'You ve already guessed that letter.')
        else:
          num_of_guesses = num_of_guesses - 1
          print_info(num_of_warnings,old_guessed_word,'You ve already guessed that letter.')
      else:
        letters_guessed.append(str.lower(new_letter_guessed))
        new_guessed_word = get_guessed_word(secret_word, letters_guessed)
        if is_letter_in_word(str.lower(new_letter_guessed),secret_word):
          print('Good guess:',new_guessed_word)
        elif str.lower(new_letter_guessed) in vowels:
          num_of_guesses = num_of_guesses - 2
          print('Oops! That letter is not in my word:',new_guessed_word)
        else:
          num_of_guesses = num_of_guesses - 1
          print('Oops! That letter is not in my word:',new_guessed_word)
      if is_word_guessed(secret_word,letters_guessed):
        print('-------------')
        print('Congratulations, you won!')
        print('Your total score for this game is:',num_of_guesses * num_unique_letters(secret_word))
      elif not is_word_guessed(secret_word,letters_guessed) and num_of_guesses == 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was else.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
