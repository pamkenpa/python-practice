# 1

total = 150

if total > 50:
  print("20%")
elif total > 100:
  print("5%")

# 2

age = 15

if age >= 18:
  print("Adult")
else:
  print("Minor")

print("Adult" if age >= 18 else "Minor")

# 3

quantity = 0

if quantity:
  print(f"You have {quantity} AC's")

if quantity is not None:
  print(f"You have {quantity} AC's")

# 4

age = 26

if 18 < age < 29:
  print("Age nimo")
else:
  print("not your age!")

if 18 < age and age < 29:
  print("Age nimo")
else:
  print("not your age!")

# 5

print(bool([]))
print(bool([0])) #bc a list containing one falsy is still truthy

