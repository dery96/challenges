from random import randint as RANDOM


letters = 'abcdefghijklmnoprstuvwyz'
len_letters = len(letters) - 1
syllabes = ['mon', 'fay', 'shi', 'fag', 'blarg', 'rash', 'izen']


def Generate_Word(word_len=15, word=''):
    '''This function generate Words (Random Letters) with syllabes that it
       could make sense'''

    word_length = RAND(5, word_len)
    syllabe_rand = syllabes[RAND(0, len(syllabes) - 1)]

    for i in range(0, word_length):
        letter_random = letters[RAND(0, len_letters)]
        if i == 0:
            word += letter_random.upper()
        if i + len(syllabe_rand) >= word_length:
            word += syllabe_rand
            break
        if i > 0:
            word = word + letter_random
    return word


print 'Hello: %s %s' % (Generate_Word(6), Generate_Word(7))
