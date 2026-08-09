inventory = {
    "rice": {"price": 55, "quantity": 2},
    "eggs": {"price": 8, "quantity": 3},
    "soap": {"price": 25, "quantity": 15}
}

def total_value(inventory):
    total = 0 
    for product, details in inventory.items():
        product_total = details["quantity"] * details["price"]
        total += product_total
    return total


def low_stock(inventory, threshold):
    low_stock_item = []
    for product, details in inventory.items():
        if details["quantity"] < threshold:
            low_stock_item.append(product)
    return low_stock_item

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

value = total_value(inventory)
low = low_stock(inventory, 5)
cost = restock_cost(inventory, 5)

print("Total inventory value:", value)
print("Low stock items:", low)
print("Cost to restock:", cost)


        

