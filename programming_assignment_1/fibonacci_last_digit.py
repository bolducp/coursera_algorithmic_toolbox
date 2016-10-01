# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    fibs_last_digits = [0, 1]

    while len(fibs_last_digits) <= n:
        next_fib_last_digit = (fibs_last_digits[-2] + fibs_last_digits[-1]) % 10
        fibs_last_digits.append(next_fib_last_digit)

    return fibs_last_digits[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
