"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from cgi import test
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        root = top = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                top.next = list1
                list1 = list1.next
            else:
                top.next = list2
                list2 = list2.next
            top = top.next
        top.next = list1 or list2 # 이부분이 키포인트 인것같음.
        return root.next
            

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

testcase = Solution()
list3 = testcase.mergeTwoLists(list1, list2)

for _ in range(6):
    print(list3.val)
    list3 = list3.next