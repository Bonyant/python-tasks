def order(sentence):
    if len(sentence) == 0:
        return ""
    array = sentence.split(" ")
    print(array)
    n = 0
    resStr = " "*(len(array)-1)
    resArr = resStr.split(" ")
    while n < len(array):
        for i, el in enumerate(array[n]):
            if el.isdigit():
                resArr[int(el) - 1] = array[n]
        n += 1
    resStr = " ".join(resArr)
    return resStr