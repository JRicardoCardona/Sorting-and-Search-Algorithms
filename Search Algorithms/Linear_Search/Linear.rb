
# Variable to move through array
index = 0
number = 20

# Array to search
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12,13,14,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
n = list.length

# Loop to search for number
while index < n do
    if list[index] == number
        puts "Number found at index: #{index}"
        break
    end

    index+=1
end



