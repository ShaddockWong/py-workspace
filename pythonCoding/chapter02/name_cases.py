name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

name = "eric stone"
print(f"Hello {name.lower()}, would you like to learn some Python today?")
print(f"Hello {name.upper()}, would you like to learn some Python today?")
print(f"Hello {name.title()}, would you like to learn some Python today?")

print(
    'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
)

famous_person = "Albert Einstein"
message = "A person who never made a mistake never tried anything new."
print(f'{famous_person} once said, "{message}"')

name = " \tAlbert Einstein\t\n"
print(name.lstrip())
print(name.rstrip())
print(name.strip())

filename = "python_notes.txt"
print(filename)
print(filename.removesuffix(".txt"))
