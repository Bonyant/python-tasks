from collections import Counter

def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    diff = word - letters
    return len(diff) == 0