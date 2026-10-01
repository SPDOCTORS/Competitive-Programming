# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        temp=head
        s=set()
        while temp is not None:
            if temp in s:
                return temp
            s.add(temp)
            temp=temp.next
        return None

        