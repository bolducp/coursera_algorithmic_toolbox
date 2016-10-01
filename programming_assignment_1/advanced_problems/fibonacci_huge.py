import sys

def get_fibonacci_huge(n, m):
    pisano_period_length = get_pisano_period_length(m)
    pisano_period_remainder = n % pisano_period_length
    return get_fibonacci(pisano_period_remainder) % m
   
def get_pisano_period_length(m):
    if m == 0:
        return 0

    fibs = [0, 1, 1]
    pisano_period = [0, 1]
    pisano_period.append(1 % m)

    while not (pisano_period[-2] == 0 and pisano_period[-1] == 1):
        next_fib = fibs[-1] + fibs[-2]
        fibs.append(next_fib)
        next_pisano = next_fib % m
        pisano_period.append(next_pisano)

    return len(pisano_period) - 2

def get_fibonacci(n):
    if n == 0:
        return 0

    fibs = [0, 1]
    while len(fibs) <= n:
        next_fib = fibs[-1] + fibs[-2]
        fibs.append(next_fib)
    return fibs[-1]
    

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
