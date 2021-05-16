def two_sum(numbers, target):
    print(numbers, target)
    n = 0
    result = []
    print(len(numbers))
    while n < len(numbers):
        for i in range(len(numbers)):
            if numbers[n] != numbers[i] and numbers[n] + numbers[i] == target:
                result.append(n)
                result.append(i)
                print(result)
                return result
            elif numbers[n] == numbers[i]:
                i += 1
                if numbers[n] + numbers[i] == target:
                    result.append(n)
                    result.append(i)
                    return result
        n += 1