from NameGenerator import name

'''
Idea of this short code is that based on popular image, user write a name and
return his name in "Japanese"
'''

letters = 'abcdefghijklmnoprstuvwyz'

dit_upper = {'A': 'Ka', 'C': 'Mi', 'B': 'Zu', 'E': 'Ku', 'D': 'Te', 'G': 'Ji',
             'F': 'Lu', 'I': 'Zi', 'H': 'Ri', 'K': 'Me', 'J': 'Zu', 'M': 'Rin',
             'L': 'Ta', 'O': 'Mo', 'N': 'To', 'P': 'o', 'S': 'Shi', 'R': 'Ke',
             'U': 'Chi', 'T': 'Ari', 'W': 'Ru', 'V': 'Do', 'Y': 'Mei', 'Z': 'Na',
             'a': 'ka', 'c': 'mi', 'b': 'zu', 'e': 'ku', 'd': 'te', 'g': 'ji',
             'f': 'lu', 'i': 'zi', 'h': 'ri', 'k': 'me', 'j': 'zu', 'm': 'rin',
             'l': 'ra', 'o': 'ni', 'n': 'to', 'p': 'no', 's': 'ari', 'r': 'ke',
             'u': 'do', 't': 'chi', 'w': 'mei', 'v': 'ru', 'y': 'na', 'z': 'fu'}


def Jap_Generate(czy=0, original_name=''):
    if czy == 0:
        original_name = raw_input("Podaj Swoje Imie: ")
    else:
        original_name = name.Generate_Word(6)
    jap_name = ''
    for i in original_name:
        jap_name += dit_upper[i]
    print 'Stare imie %s, brzmi teraz %s' % (original_name, jap_name)

Jap_Generate(1)

# Beacouse of lazyness I wrote code to write dict faster
# dite = {}
# for i in letters.upper():
#     print "Litera", i
#     jap_str = raw_input("wpisz: ")
#     if jap_str == "esc":
#         break
#     dite[i] = jap_str
# print dite
