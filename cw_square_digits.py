# Square Every Digit

def square_digits(num):
    number = list(str(num))
    for i in range(len(number)):
        number[i] = int(number[i])
        number[i] **= 2
    return int("".join(map(str, number)))