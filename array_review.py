def has_value(arr, target):
    for num in arr:
        if num == target:
            return True
    return False


temps = [68, 72, 75, 70, 74]
print(has_value(temps, 70))
print(has_value(temps, 99))

temp = [68, 72, 75, 70, 74]
temps.append(80)
print(temps)

temps.insert(1, 100)
print(temps)

temps = [68, 72, 75, 70, 74]
temps.remove(75)
print(temps)

prices = [45, 12, 78, 33, 9]
print(max(prices))
print(min(prices))

path_a = 12
path_b = 8

print(max(path_a, path_b))
print(min(path_a, path_b))

temps = [68, 72, 75, 70, 74, 71, 73]

def second_highest(arr):
    highest = max(arr[0], arr[1])
    second_highest = min(arr[0], arr[1])
    for num in arr[2:]:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest:
            second_highest = num
    return second_highest

print(second_highest(temps))

            