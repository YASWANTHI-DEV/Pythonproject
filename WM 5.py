import cmath

def read_multiple_inputs(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [tuple(map(float, line.strip().split())) for line in lines]

def solve_weather_model(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2

def write_multiple_outputs(filename, results):
    with open(filename, 'w') as file:
        for idx, (root1, root2) in enumerate(results, start=1):
            file.write(f"Set {idx}:\n")
            file.write(f"  Time 1: {root1}\n")
            file.write(f"  Time 2: {root2}\n\n")

def main():
    inputs = read_multiple_inputs('input.txt')
    results = [solve_weather_model(a, b, c) for a, b, c in inputs]
    write_multiple_outputs('output.txt', results)
    print(open('output.txt').read())  # Show results in notebook

main()
# Create input.txt for multiple sets
with open('input.txt', 'w') as f:
    f.write('1 -3 -10\n')
    f.write('1 4 4\n')
    f.write('2 5 -3\n')