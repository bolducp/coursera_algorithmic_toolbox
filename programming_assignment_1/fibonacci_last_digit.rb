def fib_last_digit(n)
  fibs_last_digits = [0, 1]
  while fibs_last_digits.length <= n do
    next_fib_last_digit = (fibs_last_digits[-1] + fibs_last_digits[-2]) % 10
    fibs_last_digits << next_fib_last_digit
  end
  fibs_last_digits.last
end

if __FILE__ == $0
  n = gets.to_i
  puts "#{fib_last_digit(n)}"
end
