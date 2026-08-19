# 1

x = 1
y = 2.0
word = "python"
gwapo_ko = True
kwarta_nako = None

print(type(x))
print(type(y))
print(type(word))
print(type(gwapo_ko))
print(type(kwarta_nako))

# 2

x = 1
print(type(x))
x = "one"
print(type(x))

# 3

a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

# 4

x = 0
y = "0"
z = None

print(x)
print(y)
print(z)
print(bool(x))
print(bool(y))
print(bool(z))

# 5

if False:
  n = 2
print(n)

# NameError: name 'n' is not defined, I used a variable that is for an "if" statement
