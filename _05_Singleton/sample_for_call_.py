class Example:
    def __init__(self):
        print("Instance Created for example")

    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")


# Instance created
e = Example()

# __call__ method will be called
e()


class Product:
    def __init__(self):
        print("Instance Created for Product")

    # Defining __call__ method
    def __call__(self, a, b):
        print(a * b)


# Instance created
ans = Product()

# __call__ method will be called
ans(10, 20)
