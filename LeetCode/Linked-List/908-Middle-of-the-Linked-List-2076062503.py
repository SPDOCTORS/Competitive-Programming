# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        cnt=0
        while temp:
            cnt+=1
            temp=temp.next
        mid_pos=(cnt)//2+1
        mid_node=head
        for _ in range(1,mid_pos):
            mid_node=mid_node.next
        return mid_node
        