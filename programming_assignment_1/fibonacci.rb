def calc_fib(n)
  if n == 0 return 0

  fibs = [0, 1]
  while fibs.length <= n do
    next_fib = fibs[-1] + fibs[-2]
    fibs << next_fib
  end
  fibs.last
end

if __FILE__ == $0
  n = gets.to_i
  puts "#{calc_fib(n)}"
end
