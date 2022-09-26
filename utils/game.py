
class Hangman:
    """Function that will perform the add operation between two numbers (in params).
    :param number_one: An int that will be added to the second parameter.
    :param number_two: An int that will be added to the fist parameter.
    :return: An int that is the result of the two params being added to each other. """

    possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'Labour saving device','Not rocket science','Online piracy','Reinstall the programs','Shop online','Shut down'
    'Use a search engine','Social media networks','State of the art technology','Surfing the web','To click on an icon','To crash','To Log in','To upgrade your computer system',
    'Wireless hotspots','Access to the Internet','Advances in technology','Back up your files','Become rapidly obsolete','Computer literate','Control remotely','Downloading from the Internet'
    'Electronic Funds Transfer','Emerging technology','Glued to the screen','Hacking into the network','Internet access','Internet of Things', 'Internet-enabled', 'Keep a hard copy']
    word_to_find = possible_words.random()
    lives = 5
    well_guessed_letters = []
    wrongly_guessed_letters = ""
    turn_count = 0
    error_count = 0


    def _init_(self):
        pass

    def play(letter):
        if len(letter) == 1 and type(letter) == 'str':
            turn_count += 1
            if letter in word_to_find:
                well_guessed_letters.append(letter)
            else:
                wrongly_guessed_letters.append(letter)
                error_count += 1
        else:
            print("Please type in one letter.")
            
    def start_game():

        if lives != 0 or well_guessed_letters == :
            play()

        elif lives = 0:
            game_over()

        elif well_guessed_letters == :
            well_played()

    def game_over():
        print("GAME OVER")
        
    def well_played():
        print (f"You found the word: {word_to_find} in {turn_count} turns with {error_count} errors!")