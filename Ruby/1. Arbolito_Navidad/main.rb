altura = 9

altura.times do |i|
    espacios = " " * (altura - i - 1)
    asteriscos = "*" * (2 * i + 1)
    puts espacios + asteriscos
end


3.times do
    puts " " * (altura - 2) + "| |"
end