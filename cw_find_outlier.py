# Find The Parity Outlier

def find_outlier(integers):
    oddSum = 0
    evenSum = 0
    for num in integers:
        if num % 2 == 0:
            evenSum += 1
        else:
            oddSum += 1
    if evenSum > oddSum:
        for even in integers:
            if even % 2 != 0:
                return even
    else:
        for odd in integers:
            if odd % 3 != 0:
                return odd

# def find_outlier(integers):
#     evens = []
#     odds = []
#     for i in integers:
#         if i % 2 > 0:
#             odds.append(i)
#         if i % 2 == 0:
#             evens.append(i)
#     if len(evens) > len(odds):
#         return odds[0]
#     else:
#         return evens[0]