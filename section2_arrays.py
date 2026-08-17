arr = [10, 20, 30, 40, 50]
print(arr[3])

def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print(arr[3])
print(find_index(arr, 40))
print(find_index(arr, 99))

arr = [3, 7, 3, 3, 9, 7, 3]

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count



print(count_occurrences(arr, 3))
print(count_occurrences(arr, 7))
print(count_occurrences(arr, 100))