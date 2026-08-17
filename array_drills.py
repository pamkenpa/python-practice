scores = [55, 82, 91, 82, 40, 91, 91, 60]

def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(find_index(scores, 91))
