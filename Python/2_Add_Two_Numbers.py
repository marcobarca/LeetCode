# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        carry = 0
        head = ListNode()
        current = head

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0 
            x = a + b + carry
            current.val = x % 10
            carry = x // 10

            if (l1 and l1.next) or (l2 and l2.next) or carry: 
                current.next = ListNode()
                current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head
