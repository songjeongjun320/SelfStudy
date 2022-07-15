"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a 
single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

"""
l1 = [9,9,9,9,9]
l2 = [5,6,4]
carry = 0
tmp = 0
output = [0,0,0]

for _ in range(3):
    tmp = l1[_] + l2[_] + carry
    if tmp >= 10:
        output[_] = tmp-10
        carry = 1
    else:
        output[_] = tmp

print(output)

# l1과 l2의 길이가 다를때 어쩔껀지 확인