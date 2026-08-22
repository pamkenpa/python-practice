# 1

x = 1
y = 2

print(x + y) #addition
print(x - y) #subtraction
print(x / y) #division
print(x * y) #multiplication
print(x // y) #floor division
print(x % y) #modulo
print(x ** y) #exponentation 

# 2
age = 19
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

# 3
n = 0

for i in range(5):
  n += i
print(n)



# 4

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# my own explanation: x is equal to y because they contain the same value [1, 2, 3]. For is, i think because x is not y? because they are two differnt variables?

# 5

def is_none(value):
    return value is None

print(is_none(None))
print(is_none(5))

# 6

print(1 in [1, 2, 3])
print(4 not in [1, 2, 3])