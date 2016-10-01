import sys

def lcm(a, b):
    product = a * b 
    gdc = get_gcd(a, b)
    return product / gdc

def get_gcd(a, b):
    while b > 0:
        remainder = a % b
        a = b
        b = remainder
    return a

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))


