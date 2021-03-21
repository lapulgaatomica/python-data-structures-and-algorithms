def recursive_binary_search(list, target):
    if list:
        middle = len(list) // 2
        if list[middle] == target:
            return True
        elif list[middle] < target:
            return recursive_binary_search(list[middle + 1:], target)
        elif list[middle] > target:
            return recursive_binary_search(list[:middle-1], target)
    return False


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(recursive_binary_search(list, 1))
