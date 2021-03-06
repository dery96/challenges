from random import randint as RANDOM


'''
Generates Words it meant to be character name generator
'''
letters = 'abcdefghijklmnoprstuvwyz'
len_letters = len(letters) - 1
syllabes = ['mon', 'fay', 'shi', 'fag', 'blarg', 'rash', 'izen']


def Generate_Word(word_len=15, word=''):
    '''This function generate Words (Random Letters) with syllabes that it
       could make sense'''

    word_length = RANDOM(5, word_len)
    syllabe_rand = syllabes[RANDOM(0, len(syllabes) - 1)]

    for i in range(0, word_length):
        letter_random = letters[RANDOM(0, len_letters)]
        if i == 0:
            'First letter must be UPPER'
            word += letter_random.upper()
        if i + len(syllabe_rand) >= word_length:
            word += syllabe_rand
            break
        if i > 0:
            word = word + letter_random
    return word


print 'Hello: %s %s' % (Generate_Word(6), Generate_Word(7))
