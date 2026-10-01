# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp=head
        cnt=1
        while temp.next:
            temp=temp.next
            cnt+=1
        temp.next=head
        k=k%cnt
        end=cnt-k
        while end>0:
            temp=temp.next
            end-=1
        head=temp.next
        temp.next=None
        return head
    
        