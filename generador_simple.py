def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)