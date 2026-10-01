# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        pos=2
        mini=float('inf')
        first=-1
        prev_critcil=-1
        while curr.next:
            next_node=curr.next
            if (curr.val>next_node.val and curr.val>prev.val) or (curr.val<next_node.val and curr.val<prev.val):
                if first==-1:
                    first=pos
                    prev_critical=pos
                else:
                    distance=pos-prev_critical
                    mini=min(mini,distance)
                    prev_critical=pos
            prev=curr
            curr=curr.next
            pos+=1
        if mini==float('inf'):
            return[-1,-1]
        maxi=prev_critical-first
        return [mini,maxi]


        