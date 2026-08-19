inventory = {
    "rice": {"price": 55, "quantity": 20},
    "eggs": {"price": 8, "quantity": 3},
    "soap": {"price": 25, "quantity": 15}
}

def total_value(inventory):
    total = 0
    for details in inventory.values():
        total += details["price"] * details["quantity"]
    return total

print(total_value(inventory))

scores = [88, 92, 79, 85]

def average(scores):
    average = sum(scores) / len(scores)
    return average

print(average(scores))


inventory = {
    "rice": {"price": 55, "quantity": 20},
    "eggs": {"price": 8, "quantity": 3},
    "soap": {"price": 25, "quantity": 15}
}

def low_stock(inventory, threshold):
    low = []
    for name, details in inventory.items():
        if details["quantity"] < threshold:
            low.append(name)
    return low

print(low_stock(inventory, 16))

counts = {"the": 3, "cat": 2, "sat": 1}

def most_common(counts):
    highest = 0
    top_word = None
    for word, count in counts.items():
        if count > highest:
            highest = count
            top_word = word 
    return top_word
        
print(most_common(counts))
