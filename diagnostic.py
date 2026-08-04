# #1
# print("Jimdandy")
# print("26 years old")

# #2
# name = input("What is your name? ")
# print(f"Hello, {name.capitalize()}!")

# #3
# x = int(input("x: "))
# y = int(input("y: "))

# print(x + y)
# #i tried inputing "three" it gave this error: ValueError: invalid literal for int() with base 10: 'three'
# #if no number is entered it shows this error: ValueError: invalid literal for int() with base 10: ''
# #4
# num = int(input("Give me a number: "))

# if num % 2 == 0:
#   print("even")
# else:
#   print("odd")

# #5
# for i in range(1, 21):
#   if i % 3 == 0:
#     print("fizz")
#   else:
#     print(i)

# #6
# movie_titles = ["Minions", "Moana", "Avengers", "Hulk", "Spiderman"]

# movies = 1

# for movie in movie_titles:
#   print(f"{movies}. {movie}")
#   movies += 1

# #7
# def celsius_to_fahrenheit(c):
#   convert = c * 9 / 5 + 32
#   return convert


# fahrenheit = celsius_to_fahrenheit(0)
# print(f"{fahrenheit}°F")
# fahrenheit = celsius_to_fahrenheit(2)
# print(f"{fahrenheit}°F")
# fahrenheit = celsius_to_fahrenheit(3)
# print(f"{fahrenheit}°F")

#8
countries = {"Japan": "Tokyo", "Philippines": "Manila", "U.S.A": "Washington D.C"}

for country in countries:
  print(country)