data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

oddNumbers = lambda d : d % 2  == 1

print(list(filter(oddNumbers, data)))