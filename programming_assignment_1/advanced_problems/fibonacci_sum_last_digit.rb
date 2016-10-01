def fib_sum_last_digit(n)
  return n if n <= 1
  calc_fibs(n).inject(0, :+) % 10
end

def calc_fibs(n)
  return 0 if n == 0 
  fibs = [0, 1]
  while fibs.length <= n do
    next_fib = fibs[-1] + fibs[-2]
    fibs << next_fib
  end
  fibs
end

if __FILE__ == $0
  n = gets.to_i
  puts "#{fib_sum_last_digit(n)}"
end
