def is_isogram(string):
    string = string.lower()
    for item in string:
        if string.count(item) > 1 :
            return False
    return True