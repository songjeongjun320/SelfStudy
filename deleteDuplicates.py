"""
Given the head of a sorted linked list, delete all
duplicates such that each element appears only once.
Return the linked list sorted as well.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        left = head
        while head:
            if head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return left

testcase = Solution()

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

print(testcase.deleteDuplicates(head))