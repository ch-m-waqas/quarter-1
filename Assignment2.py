# 1. Simple Message
message: str = "Hello, World!"
print(message)

# 2. Simple Messages
message: str = "Hello, World!"
print(message)
message: str = "Hello, Python!"
print(message)

# 3. Personal Message
name: str = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

# 4. Name Cases
name: str = "Eric"
print(name.lower())
print(name.upper())
print(name.title())

# 5. Famous Quote
quote: str = "A person who never made a mistake never tried anything new."
author: str = "Albert Einstein"
print(f"{author} once said, “{quote}”")

# 6. Famous Quote 2
famous_person: str = "Albert Einstein"
message: str = f"{famous_person} once said, “A person who never made a mistake never tried anything new.”"
print(message)

# 7. Stripping Names
name: str = "\t\n Eric \n\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 8. Variable Sum
x: int = 5
y: int = 10
z: int = 15
print(x + y + z)

# 9. Variable Swap
a: int = 1
b: int = 2
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# 10. Favorite Color
favorite_color: str = "Blue"
print(favorite_color)
color: str = favorite_color
print(color)

# 11. Changing Pet Name
pet_name: str = "Buddy"
pet_name = "Max"
print(pet_name)

# 12. Observing Name Error
sunshine: str = "Sunshine"
# print(sunshine)
print(sunshine)


# 13. Reassigning Score
score: int = 100
print(score)
score = 200
print(score)

# 14. City Name
city: str = "New York"
print(city)

# 15. Title Case Text
text: str = "python programming"
print(text.title())

# 16. Lowercase Conversion
mixed_case: str = "PyThOn PrOgRaMmInG"
print(mixed_case.lower())
print(mixed_case.upper())

# 18. Current Temperature
temperature: int = 25
print(f"The current temperature is {temperature} degrees.")

# 19. Printing a Poem
poem: str = """Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""
print(poem)
