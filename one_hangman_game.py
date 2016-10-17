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
    print output
    print number


def check_output(typer, word, marker):
    '''If checking letter is in word, marker of this letter become 1'''
    for i in range(len(word)):
        if word[i] == typer:
            marker[i] = 1
    return marker


def game_round(example_of_word, find_out_word=False):
    ################################################
    hangman = ['left hand', 'right hand',
               'neck', 'body', 'left leg', 'right leg']
    ################################################
    example_of_marker = generate_output(example_of_word)
    hangman_mistake = 0
    while find_out_word is False:
        # draw_board(example_of_word, example_of_marker)
        if hangman_mistake == len(hangman):
            print "Failure -> You hangmaned the Men!"
            break
        check_sum = sum(example_of_marker)
        rounde = raw_input("Podaj litere: ")
        example_of_marker = check_output(
            rounde, example_of_word, example_of_marker)

        if check_sum == sum(example_of_marker):
            out = ''
            hangman_mistake += 1
            print "You wrote wrong letter"
            for i in range(hangman_mistake):
                out += '%s, ' % (hangman[i])
            print out

        if sum(example_of_marker) == len(example_of_word):
            print "WYGRALES -> KONIEC GRY"
            find_out_word = True
        draw_board(example_of_word, example_of_marker)


example_of_word = "Tomek"
game_round(example_of_word)
