import cmath  
def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split()
        a, b, c = map(float, data)
    return a, b, c

def solve_quadratic(a, b, c):
    discriminant = cmath.sqrt(b ** 2 - 4 * a * c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2

def write_output(filename, root1, root2):
    with open(filename, 'w') as f:
        f.write(f"Root 1: {root1}\n")
        f.write(f"Root 2: {root2}\n")

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    
    a, b, c = read_input(input_file)
    
    
    root1, root2 = solve_quadratic(a, b, c)
    

    write_output(output_file, root1, root2)

if __name__ == '__main__':
    main()