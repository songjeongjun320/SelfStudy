input = 19
tmp = input
updated_input = 0
count = 1

while True:
    if input == 1:
        break    

    while True:
        if tmp/10 < 1:
            break
        else:
            count += 1
            print(count)
            tmp = tmp/10

    for _ in range(count,-1,-1):
        a,b = divmod(input, 10^(count))
        updated_input += a*a
        print(a*a)
        input -= a * 10 ^ (count-1)
    
    input = updated_input
if input == 1:
    print(True)
    print(True)