try:
    age = int(input("Enter your age: "))
    print("You are", age, "years old")
except ValueError:
    print("That's not a valid number.")

def safe_divide(a, b):
    try:
        quotient = a / b
        return quotient
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
    

        
    