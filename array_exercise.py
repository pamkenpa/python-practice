temps = [68, 72, 75, 70, 74, 71, 73]

def second_highest(arr):
    highest = 0
    second_highest = 0
    for temp in temps:
        if temp > highest:
            highest = temp
        if second_highest > temp:
            second_highest = temp
    return second_highest
print(second_highest(temps))
