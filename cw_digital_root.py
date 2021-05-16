# Sum of Digits / Digital Root

def digital_root(n):
    while n > 9:
        n = sum(int(i) for i in str(n))
    return n