def fib_huge(n, m)
  pisano_period_length = calc_pisano_period_length(m)
  pisano_period_remainder = n % pisano_period_length
  calc_fib(pisano_period_remainder) % m
end


def calc_pisano_period_length(m)
  return 0 if m == 0

  fibs = [0, 1, 1]
  pisano_period = [0, 1]
  pisano_period << (1 % m)

  loop do
    next_fib = fibs[-1] + fibs[-2]
    fibs << next_fib
    next_pisano = next_fib % m
    pisano_period << next_pisano

    break if (pisano_period[-2] == 0) && (pisano_period[-1] == 1)
  end

  pisano_period.length - 2
end


def calc_fib(n)
  return 0 if n == 0 
  fibs = [0, 1]
  while fibs.length <= n do
    next_fib = fibs[-1] + fibs[-2]
    fibs << next_fib
  end
  fibs.last
end

if __FILE__ == $0
  a, b = gets.split().map(&:to_i)
  puts "#{fib_huge(a, b)}"
end
