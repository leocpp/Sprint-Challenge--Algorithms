'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):

    count = 0
    # TBC
    pos = word.find('th')

    if pos == -1:
        return 0

    return 1  + count_th(word[pos+2:])

word = 'thththt'

print(count_th(word))
word = 'aathtaahtht'

print(count_th(word))
