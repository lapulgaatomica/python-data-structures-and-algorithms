def linear_search(list, target):
    for i, item in enumerate(list):
        if target == item:
            return i
    return None


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(linear_search(list, 11))
