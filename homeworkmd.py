

def Sqft_calc(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    
    return length * width

def calculate_circumference(radius):
    
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    
    pi = 3.141592653589793
    return 2 * pi * radius