input = 40
first_input = input
switch = True
check_list = []

# LeetCode에서 '/'가 안되는 문제

while True:
    # Check that this # was occured before
    for _ in range(len(check_list)):
        if check_list[_] == input:
            switch = False
            print("{0} is not a Happy Number".format(first_input))
            break
        else:
            check_list.append(input)
            
    if input == 1 or switch == False:
        break 
    
    check_list.append(input)
    count = 1
    tmp = input
    updated_input = 0   

    while True:
        if tmp/10 < 1:
            break
        else:
            count += 1
            print(count)
            tmp = tmp/10

    for _ in range(count,0,-1):
        a,b = divmod(input, 10**(_ - 1))
        print("a {0}".format(a))
        print("b {0}".format(b))
        updated_input += a*a
        input -= a * 10 ** (_ - 1)
    
    input = updated_input
if input == 1:
    print(True)