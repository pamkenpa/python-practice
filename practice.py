colors = ["red", "green", "blue", "yellow"]

print(colors[2])
colors[3] = "purple"
print(colors)

dimensions = (1920, 1080)

print(dimensions[1])

car = {"brand": "Toyota", "year": 2020}

print(car["brand"])
car["color"] = "black"
print(car)

student = {
    "name": "Maria",
    "grades": [88, 92, 79],
    "birthday": (2000, 5, 14)
}

print(student["name"])
grades = student["grades"]
print(grades[1])
birth_year = student["birthday"]
print(birth_year[0])

inventory = {
    "rice": {"price": 55, "quantity": 20},
    "eggs": {"price": 8, "quantity": 3},
    "soap": {"price": 25, "quantity": 15}
}

print(inventory["eggs"]["quantity"])
print(inventory["soap"]["price"])

inventory = {
    "rice": {"price": 55, "quantity": 20},
    "eggs": {"price": 8, "quantity": 3},
    "soap": {"price": 25, "quantity": 15}
}

for item, details in inventory.items():
    print(item, details)

for item, details in inventory.items():
    print(item, details["price"])

def total_value(inventory):
    total = 0
    for item, details in inventory.items():
        total += details["price"] * details["quantity"]
    return total

result = total_value(inventory)
print(result)

def low_stock(inventory, threshold):
    low_items = []
    for item, details in inventory.items():
        if details["quantity"] < threshold:
            low_items.append(item)
    return low_items

result = low_stock(inventory, 5)
print(result)