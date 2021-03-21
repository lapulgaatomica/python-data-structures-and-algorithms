def iterative_binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        middle = (last + first) // 2
        if target == list[middle]:
            return middle
        elif list[middle] < target:
            first = middle + 1
        elif list[middle] > target:
            last = middle - 1
    return None


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(iterative_binary_search(list, 10))
