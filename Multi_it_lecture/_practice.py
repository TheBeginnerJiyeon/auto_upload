def greet(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

greet(name="Alice", age=30, city="New York")
