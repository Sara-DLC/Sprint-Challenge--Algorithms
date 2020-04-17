'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # Recursion rules:
    # Needs base case
    # must change its state and move toward the base case
    # must call itself, recursively

    # Base case: length of the word is less than 2 then return 0
    # Taking case of word into consideration look for 'th' if the word between indexes 0 and 2 equal 'th', keep incrementing by 1 <-recursive call starts
    # if no, continue

    if len(word) < 2:
        return 0
    elif word[0:2] == "th":
        return count_th(word[2:]) + 1
    else:
        return count_th(word[1:])
