def gcd(a, b)
  while b > 0 do
    remainder = a % b
    a = b
    b = remainder
  end
  a
end

if __FILE__ == $0
  a, b = gets.split().map(&:to_i)
  puts "#{gcd(a, b)}"
end

