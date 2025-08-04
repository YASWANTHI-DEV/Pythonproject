
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
x = float(input("Enter a value for x: "))
y = a * x**2 + b * x + c
print(f"When x = {x}, y = {y}")
import cmath  
target_y = float(input("Enter a value for y to solve for x: "))
discriminant = b**2 - 4 * a * (c - target_y)
x1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
x2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
print(f"Possible x values for y = {target_y}: {x1}, {x2}")