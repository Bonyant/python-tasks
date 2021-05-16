def filter_list(l):
    integers = []
    for item in l:
        if type(item) == int:
            integers.append(item)
    return integers