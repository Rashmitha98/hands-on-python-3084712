greet = "Hello World "
extened_grt = f"{greet}" + "this is a long string"

print(extened_grt)
name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted)

print(formatted.replace("John","Mary"))