# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        if l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            if val // 10 == 0:
                return ListNode(val, next=self.addTwoNumbers(l1=l1.next if l1 else None, l2=l2.next if l2 else None))

            else:
                out, carry = self.get_carry_and_unit(val)
                val = out
                return ListNode(val, next=self.addTwoNumbers(l1=l1.next if l1 else None, l2=l2.next if l2 else None, carry=carry))

        else:
            return ListNode(val=carry) if carry > 0 else None

    def get_carry_and_unit(self, val):
        carry = val // 10
        out = val % 10
        return (out, carry)
        