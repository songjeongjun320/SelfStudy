input = "MCMXCIV"

roman_to_int = []
output = 0

for _ in range(len(input)):
    if input[_] == 'I':
        roman_to_int.append(1)
    elif input[_] == 'V':
        roman_to_int.append(5)
    elif input[_] == 'X':
        roman_to_int.append(10)
    elif input[_] == 'L':
        roman_to_int.append(50)
    elif input[_] == 'C':
        roman_to_int.append(100)
    elif input[_] == 'D':
        roman_to_int.append(500)
    elif input[_] == 'M':
        roman_to_int.append(1000)

roman_to_int.append(0)
_ = 0

while _ < len(roman_to_int) - 1:
    if roman_to_int[_] >= roman_to_int[_+1]:
        output += roman_to_int[_]
    elif roman_to_int[_] < roman_to_int[_+1]:
        output = output + roman_to_int[_+1] - roman_to_int[_]
        _ += 1
    _ += 1

print(output)