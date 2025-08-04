a = 1.0     
b = -3.0    
c = 2.0     
x = 4.0         
y = a * x**2 + b * x + c
print(f"When x = {x}, y = {y}")
import cmath
target_y = 6.0  
discriminant = b**2 - 4 * a * (c - target_y)
x1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
x2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
print(f"Possible x values for y = {target_y}: {x1}, {x2}")
///COMMENT 1///