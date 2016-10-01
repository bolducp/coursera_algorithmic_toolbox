# Uses python3
def calc_fib(n):
    fibs = [0, 1]
    while len(fibs) <= n:
        next_fib = fibs[-1] + fibs[-2]
        fibs.append(next_fib)
    return fibs[-1]

n = int(input())
print(calc_fib(n))
