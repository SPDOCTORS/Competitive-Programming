# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return None
        cnt=0
        temp=head
        while temp:
            cnt+=1
            temp=temp.next
        mid=cnt//2
        temp=head
        for _ in range(1,mid):
            temp=temp.next
        if temp.next:
            middle=temp.next
            temp.next=temp.next.next
            del middle
        return head
        