def greet():
    """A simple function that prints hello
    :return: None
    """
    print("Hello")

greet()
greet()

def greet2(name):
    print(f"Hello {name}")

greet2("James")
greet2("Bob")

def average(a,b):
    """
    Average the 2 numbers
    :param a: first number
    :param b: second number
    :return: floar, average of a and b
    """
    average= (a+b)/2
    return average #This is how a function "gives back" a value
print(average(10,20))

def divide(x,y):
    """
    Divide x by y
    :param x: first number
    :param y: second number
    :return: float, the division result
    """
    if y == 0:
        return None
    return x/y
print(divide(10,20))
print(divide(10,0))
print(divide(10,1))
print(divide(y=1, x=10))
print(divide(30))

def bond (first_name, last_name):
    return f"{first_name} {last_name}"
def introduce(name):
    print(f"The name is {name}")

print(bond("James","Smith"))
print(introduce(bond("James","Smith")))
introduce(bond())
