"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a 
single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
"""

l1 = [0,1]
l2 = [0]
carry = 0
tmp = 0
output = []

while len(l1) != len(l2):
    l2.append(0)
    print(l2)

for _ in range(len(l2)):
    tmp = l1[_] + l2[_] + carry
    carry = 0
    if tmp >= 10:
        output.append(tmp-10)
        carry = 1
    else:
        output.append(tmp)
    tmp = 0

if carry >= 1:
    output.append(carry)

print(output)

# l1과 l2의 길이가 다를때 어쩔껀지 확인
# 다시 짜야함