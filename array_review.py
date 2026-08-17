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