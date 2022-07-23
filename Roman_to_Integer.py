input = "LVIII"

roman_to_int = []

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

print(roman_to_int)