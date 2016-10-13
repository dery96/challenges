'''
Implementation of popular game called hangman
there is a word that user have to guess by writng letters
if he miss serveral times, he will lose the game
'''


def generate_output(word, marker=[]):
    '''First inicializate of game generates list with markers of the word
       (every letter have his own maker).'''
    for i in range(len(word)):
        marker.append(0)
    return marker


def draw_board(word, marker=[], output='', number=''):
    '''marker says wich letters are quessed already
       for example 0 - unknown 1 - known (letter)'''
    for i in range(len(word)):
        if marker[i] == 1:
            output += "%s " % (word[i])
            number += "%d " % (i + 1)
        else:
            output += "___ "
            number += " %d  " % (i + 1)
    print "\n"
    print output
    print number


def check_output(typer, word, marker, hangman_mark=0, check_sum=0):
    '''If checking letter is in word, marker of this letter become 1'''
    for i in range(len(word)):
        if word[i] == typer:
            marker[i] = 1
            check_sum += 1
    if check_sum > 0:
        hangman_mark += 1

    return marker


def game_round(example_of_word, find_out_word=False):
    example_of_marker = generate_output(example_of_word)
    hangman = ['left hand', 'right hand',
               'neck', 'body', 'left leg', 'right leg']
    while find_out_word is False:
        draw_board(example_of_word, example_of_marker)
        rounde = raw_input("Podaj litere: ")
        draw_board(rounde, check_output(
            rounde, example_of_word, example_of_marker))

        if sum(example_of_marker) == len(example_of_word):
            print "WYGRALES -> KONIEC GRY"
            find_out_word = True


###############################################################
#
#
# Game Settings
#
#
################################################################

example_of_word = "Tomek"
game_round(example_of_word)
