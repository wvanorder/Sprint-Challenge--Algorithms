'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # base case of no letters left
    if len(word) == 0:
        return 0
    # check to see if the first two letters are 'th'
    if word[0:2] == 'th':
        # return the method call starting at the third letter left of the word (working towards base case) + 1
        return 1 + count_th(word[2:])
    # remove the first letter as we pass the word into the method again (towards base case)
    return count_th(word[1:])
    # TBC

    pass
