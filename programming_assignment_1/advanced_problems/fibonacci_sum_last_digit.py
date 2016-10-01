import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    fibs_sum = sum(get_fibonacci(n))
    return fibs_sum % 10

def get_fibonacci(n):
    if n == 0:
        return 0
    fibs = [0, 1]
    while len(fibs) <= n:
        next_fib = fibs[-1] + fibs[-2]
        fibs.append(next_fib)
    return fibs
    

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(fibonacci_sum_naive(n))

print(fibonacci_sum_naive(100))
