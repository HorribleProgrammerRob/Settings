##################################################
# Rob Ranieri
# HW Problem 1
##################################################

import random

possibleChoices = ['stick', 'john', 'pencil', 'rubber', 'glove', 'brown', 'fox',
                   'jumps', 'over', 'lazy', 'dog', 'manner', 'house', 'love', 
                   'peace', 'object']

possibleChoices = [
    'stick',
    'john',
    'pencil',
    'rubber',
    'glove',
    'brown',
    'fox',
    'jumps'
    'over',
    'lazy',
    'dog',
    'manner',
    'house',
    'love',
    'peace',
    'object'
]
randomWord = random.choice(possibleChoices)

outputBox = '[' + ','.join("'_'" for x in range(len(randomWord))) + ']'

# To map a character from a word to a particular _ character(s), you have to
# find out the indexes of each of the underscores in outputBox, and change
# the proper ones accordingly.

# Ex.   r u b b e r
#       ['_', '_', '_', '_', '_', '_']
# If the user guesses b, we have to change the 3rd and 4th underscore to b.

outputBoxUnderscores = [index for index, char in enumerate(outputBox) if char == '_']

# We need to loop 10 times or until player wins.
# We can use a for-else loop with break.
# Print the starting game output.
print('Your guess so far is: {}'.format(outputBox))

for guesses in range(10, 0, -1):
    guess = input('> ') # I like the prompt better.     
    print('You have {} chances left'.format(guesses)) # This will make the guesses left illogical, but w/e.
    
    if guess in randomWord:
        # He guessed right, determine how many are in the word.
        outputBoxList = list(outputBox) # Str's aren't mutable.
        for i in range((randomWord.count(guess))):
            outputBoxList[outputBoxUnderscores[randomWord.find(guess)]] = guess
        
        outputBox = ''.join(outputBoxList)

    # I'd break here if got it right:
    if outputBox.count('_') == 0:
        # He guessed them all correct.
        print('You got it buddy: {}'.format(outputBox))
        break

    print('Your guess so far is: {}'.format(outputBox))
else: # For loop traversed entirely
    print('Game over buddy')
    print('Losses so far: 1')
    
