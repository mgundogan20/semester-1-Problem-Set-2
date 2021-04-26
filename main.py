def printProverb(proverb, madeGuesses, revealedVowelsLocs):
  """
  This is the function to print the proverb.
  Initially create an empty string for the proverb.
  """
  toBePrinted = ""
  """Append the string accordingly. """
  for i, c in zip(range(len(proverb)),proverb):
    if i in revealedVowelsLocs or c in madeGuesses:
      """If the character is revealed or guesses append the string with: letter + whitespace """
      toBePrinted += (c + " ")
    elif c == " ":
      """If the character is a whitespace append the string with: dash + whitespace """
      toBePrinted += ("- ")
    else:
      """If the character is a hidden letter append the string with: underscore + whitespace """
      toBePrinted += ("_ ")
  """Print the resulting proverb. """
  print("Proverb: " + toBePrinted)

def openVowel(proverb, vowelsLocs, revealedVowelsLocs):
  """
  This is the function that is used for revealing a vowel.
  Set the seed for reproducing the same outcomes for each run.
  """
  import random
  random.seed(1)

  """
  proverb: Proverb that the contestant wants to guess.
  vowelsLocs: List of the indices of the vowels in proverb. 
  revealedVowelsLocs: List of the indices of the revealed vowels in proverb. This will be appended.
  
  Find the indices that are not revealed. 
  Choose one of the unrevealed indices randomly.
  Append revealedVowelsLocs.
  Return the revealed vowel (not its index) and modified version of revealedVowelsLocs.
  """

  """YOUR CODE HERE"""
  hiddenVowelsLocs = []
  for i, letter in zip(range(len(vowelsLocs)),vowelsLocs):
      if letter not in revealedVowelsLocs:
          hiddenVowelsLocs.append(letter)
  revealedIndice = hiddenVowelsLocs[random.randint(0,len(hiddenVowelsLocs)-1)]
  revealedVowel = proverb[revealedIndice]
  revealedVowelsLocs.append(revealedIndice)
  """END OF YOUR CODE"""

  return revealedVowel, revealedVowelsLocs
    
def turnRoutine(proverb, madeGuesses, currentScore, vowelsLocs, revealedVowelsLocs):
  """
  This is the function that we call in each turn.
  Set the seed for reproducing the same outcomes for each run.
  Set user choice initially to 0. 
  Set continueGame flag initially to 1.  
  """

  """
  proverb: Proverb that the contestant wants to guess.
  madeGuesses: List of the previously made valid consonant guesses. 
  currentScore: Current score of the contestant.
  vowelsLocs: List of the indices of the vowels in proverb. 
  revealedVowelsLocs: List of the indices of the revealed vowels in proverb.
  """

  import random
  random.seed(1)

  userChoice = "0"
  continueGame = 1

  """Create the list of all consonants."""
  allConsonants =['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm' ,'n' ,'p', 'q', 'r', 's', 't', 'y', 'v', 'w', 'x', 'z']

  """
  Ask user to provide a choice until they input 1, 2 or 3.
  Press 1 to : Guess a consonant
  Press 2 to : Open a vowel
  Press 3 to : Guess the whole proverb

  Keep asking for input until the contestant provides 1, 2 or 3.
  """
  while userChoice not in ["1", "2", "3"]:
    userChoice = input("Press 1 to : Guess a consonant\nPress 2 to : Open a vowel\nPress 3 to : Guess the whole proverb\nYour choice is: ")
    # For the autograder
    userChoice = userChoice.splitlines()[0] 
  

  if userChoice == "1":
    """If user chooses 1, they will make a consonant guess. Take the input, make it lowercase."""
    """YOUR CODE HERE"""
    # guess = 
    guess = input("Please make a consonant guess: ").lower()
    correct_count = 0

    """END OF YOUR CODE"""
    # For the autograder
    guess = guess.splitlines()[0] 
    
    """
    If, the guess is not a consonant deduce 75 points from current score.
    Print: "guess" is not a consonant and you lose 75 points.
    """
    """YOUR CODE HERE"""
    if guess not in allConsonants:
        currentScore -= 75
        print(f"\"{guess}\" is not a consonant and you lose 75 points")
        """END OF YOUR CODE"""
        

        """Else-If, the guess is not in the proverb deduce 75 points from current score.
        Print: Unfortunately your guess "guess" does not appear and you lose 75 points.
        Append the list of madeGuesses with the guess."""

        """YOUR CODE HERE"""
    elif guess not in proverb:
        currentScore -= 75
        print(f"unfortunately your guess \"{guess}\" does not appear and you lose 75 points.")
        """END OF YOUR CODE"""


        """
        Else-If, a guess is made before 
        print: You have already made this guess.
        """
        """YOUR CODE HERE"""
    elif guess in madeGuesses:
        print("You have already made this guess.")
    
        """END OF YOUR CODE"""


        """        
        Else, count how many times thw guess appears in the proverb.
        Increase the current score by this count times a random number between 50 and 150.
        Print: Congratulations the letter "guess" appears "count" times and you are rewarded with "reward" points.
        Append the list of madeGuesses with the guess.
        """
        """YOUR CODE HERE"""
    else:
        for i, letter in zip(range(len(proverb)),proverb):
            if letter == guess:
                correct_count += 1
        madeGuesses.append(guess)
        guess_reward = correct_count*random.randint(50, 150)
        currentScore += guess_reward
        print(f"Congratulations the letter \'{guess}\' appears {correct_count} times and you are rewarded with {guess_reward} points.")
    """END OF YOUR CODE"""

    """At the end of the turn print the proverb."""  
    """YOUR CODE HERE"""
    printProverb(proverb, madeGuesses, revealedVowelsLocs)

    # printProverb(...)
    """END OF YOUR CODE"""
    
  elif userChoice == "2":
    """If user chooses 2, they will reveal a vowel."""
    
    """
    If, all the wovels are revealed 
    Print: You have already unrevealed all the vowels.
    """
    """YOUR CODE HERE"""
    if len(vowelsLocs) == len(revealedVowelsLocs):
        print("You have already unrevealed all the vowels.")
        """END OF YOUR CODE"""
        
        """
        Else, call openVowel function.
        Deduce 250 points from the currentScore.
        Print: Letter + "revealedVowel" + is revealed.
        """
        """YOUR CODE HERE"""
    else:
        currentScore -= 250
        print(f"Letter \'{openVowel(proverb, vowelsLocs, revealedVowelsLocs)[0]}\' is revealed.")

    """END OF YOUR CODE"""

    """At the end of the turn print the proverb."""  
    """YOUR CODE HERE"""
    printProverb(proverb, madeGuesses, revealedVowelsLocs)
    # printProverb(...)
    """END OF YOUR CODE"""
  
  elif userChoice == "3":
    """If user chooses 3, they will try to guess the whole proverb. Take the input, make it lowercase."""
    """YOUR CODE HERE"""
    # guess = 
    guess = input("Please make a guess for the whole proverb: ").lower()
    
    """END OF YOUR CODE"""
    # For the autograder
    guess = guess.splitlines()[0] 

    """If, the guess is correct 
    Count how many numbers are still hidden. (Not revealed vowels and not guessed consonants)
    Increase current score by 200 for each hidden letter.
    Print: You won :)
    """
    """YOUR CODE HERE"""
    print(guess)
    if guess == proverb:
        newFound = len(proverb)
        """
        newFound -= len(revealedVowelsLocs)
        """
        for letter in proverb:
            if letter in madeGuesses or letter == " ":
                newFound -= 1
        currentScore += 200*newFound
        print("You won :)")
        continueGame = 0
        """END OF YOUR CODE"""

        """Else, print: You lost :("""
        """YOUR CODE HERE"""
    else:
        print("You Lost :(")
        """END OF YOUR CODE"""

        """When the final guess is made the game is over. Make continueGame flag 0."""
        continueGame = 0
  
  """
  If currentScore gets below 0 the game is over. Make continueGame flag 0.
  Print: You lost :(
  """
  """YOUR CODE HERE"""
  if currentScore < 0:
      continueGame = 0
      print("You lost :(")

  """END OF YOUR CODE"""

  """At the end of each turn print the current score and a seperator like ***********."""
  print("Your current score is: " + str(currentScore))
  print("\n********************\n")
  
  return (madeGuesses, currentScore, revealedVowelsLocs, continueGame)

  """
  madeGuesses: If the contestant presses 1 and makes a valid consonant guess, this is appended.
  currentScore: Modified by the game rules.
  revealedVowelsLocs: If the contestant presses 2 and did not reveal all the vowels before, this is appended.
  continueGame: Flag is made 0 if the game is over.
  return madeGuesses, currentScore, revealedVowelsLocs, continueGame
  """

def main():
  """Set the seed for reproducing the same outcomes for each run."""
  import random
  random.seed(1) 
  
  """Create an empty list to hold proverbs to be read."""
  proverbsList = []

  """
  Open the txt file that stores proverbs.
  Read the file line by line.
  Add the proverbs to the list.
  Keep reading until the following line returns None.
  """
  with open('proverbs.txt') as proverbsFile:
    line = proverbsFile.readline()
    proverbsList.append(line)
    while line:
      line = proverbsFile.readline()
      proverbsList.append(line)

  """"
  Select a random proverb from the list.
  Delete the last character, which is a fullstop and make it all lowercase.
  Set initial current score to 200.
  Create the list of all vowels.
  """        
  proverb = proverbsList[random.randrange(len(proverbsList))]
  proverb = proverb[:-1].lower()
  currentScore = 200
  allVowels = ['o', 'i', 'y', 'e', 'a','u']
  
  """
  Create an empty list to hold the indices of the vowels in the proverb.
  If the letter is a vowel keep its location in vowelsLocs list.
  """
  vowelsLocs = []
  for i, letter in zip(range(len(proverb)),proverb):
    if letter in allVowels:
      vowelsLocs.append(i)

  """"
  Create an empty list to hold previosuly made guesses.
  Create an empty list to hold the indices of previosuly revealed vowels. 
  Create a flag to control continuation of the game, set it to 1. 
  """
  madeGuesses = []
  revealedVowelsLocs = []
  continueGame = 1
  
  """Print a welcome message."""
  print("\nWelcome to the game of WHEEL OF FORTUNE")

  """Print the proverb."""
  printProverb(proverb, madeGuesses, revealedVowelsLocs)

  """While the continueGame flag is 1, call turnRoutine function. Be careful with the inputs and outputs of the turnRoutine function."""
  """YOUR CODE HERE"""
  while continueGame == 1:
      loopList = turnRoutine(proverb, madeGuesses, currentScore, vowelsLocs, revealedVowelsLocs,)
      madeGuesses = loopList[0]
      currentScore = loopList[1]
      revealedVowelsLocs = loopList[2]
      continueGame = loopList[3]
  """END OF YOUR CODE"""
  
  """
  At the end of the game print the full proverb.
  Return current score.
  """
  print("The proverb was: " + proverb)

  return currentScore

if __name__ == "__main__":
  # Run main.
  main()