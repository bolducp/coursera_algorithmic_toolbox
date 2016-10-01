def calc_fib(n):
    if n == 0:
        return 0

    fibs = [0, 1]
    while len(fibs) <= n:
        next_fib = fibs[-1] + fibs[-2]
        fibs.append(next_fib)
    return fibs[-1]

n = int(input())
print(calc_fib(n))
