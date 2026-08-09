inventory = {
    "rice": {"price": 55, "quantity": 2},
    "eggs": {"price": 8, "quantity": 3},
    "soap": {"price": 25, "quantity": 15}
}

def restock_cost(inventory, threshold):
    total = 0
    for product, price_quantity in inventory.items():
        quantity = price_quantity["quantity"]
        price = price_quantity["price"]
        if quantity < threshold:
            units_needed = threshold - quantity
            units_cost = units_needed * price
            total += units_cost
    return total
    
    

result = restock_cost(inventory, 5)
print(result)

