from unicodedata import name


def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


def add_tax(amount, tax_rate=0.10):
    return amount + (amount * tax_rate)


def greet_user(name):
    return "Hello " + name
