def replace_letters_in_string(secret):
    secret_hint =''
    for char in secret:
        secret_hint += '_'
    return secret_hint
#initiating variables
attempts = 0
correct = False
hint = ''
used_letters = set()
#Game
play = input('Would you like to play a game?Y/N ')
while play.lower() == 'y':
    if correct == True:
        print('congratulations you won in {} attempts!'.format(attempts))
        play = 'n'
    #theme
    theme = input('What theme would you like to guess? DISNEY, BOOK OF MORMOM, or MARVEL: ')
    if theme.lower() == 'disney':
        secret = 'ariel'
    elif theme.lower() == 'book of mormon':
        secret = 'nephi'
    elif theme.lower() == 'marvel':
        secret = 'thanos'
    secret_hint = replace_letters_in_string(secret)
    guess = input('your hint is {} '.format(secret_hint) )
    #Guess Logic
    while correct == False:
        while len(secret) != len(guess):
                print('Sorry your guess does not have the same amount of letters as the word try again.')
                guess = input('your hint is {} '.format(secret_hint) )
        if guess.lower() == secret:
                correct = True
        for i in range(len(guess)):  
            if guess[i] == secret[i]:
                hint += guess[i].upper()
                used_letters.add(i)
            elif guess[i] != secret[i] and guess[i] in secret and i not in used_letters:
                hint += guess[i].lower()
                used_letters.add(i)
            else:
                 hint += '_'
        if not correct:
            guess = input('your hint is: {} '.format(hint))
            attempts += 1
    