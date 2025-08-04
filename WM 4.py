import cmath

def read_input(filename):
    with open(filename, 'r') as file:
        a,b,c = map(float, file.readline().strip().split())
        return a, b, c

def solve_weather_model(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2

def write_output(filename, root1, root2):
    with open(filename, 'w') as file:
        file.write("Weather threshold crossed at:\n")
        file.write(f"Time 1: {root1}\n")
        file.write(f"Time 2: {root2}\n")

def main():
    a, b, c = read_input('input.txt')
    root1, root2 = solve_weather_model(a, b, c)
    write_output('output.txt', root1, root2)
    print(open('output.txt').read())  # Display output

main()
# Create a dummy input.txt file for testing
with open('input.txt', 'w') as f:
    f.write('1.0 5.0 6.0')