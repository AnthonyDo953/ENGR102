def parta(numbers):
    numbersSorted = sorted(numbers)
    # [1, 2, 3, 4, 5, 6, 7, 8]
    output = [numbersSorted[0], numbersSorted[len(numbersSorted) - 1]]
    if len(numbersSorted) % 2 == 0:
        output.insert(1, (numbersSorted[int(len(numbersSorted) / 2)] + numbersSorted[int(len(numbersSorted) / 2 - 1)]) / 2)
    else:
        output.insert(1, numbersSorted[int(len(numbersSorted) / 2)])
    return output

print(parta([1,2,4,5,6]))