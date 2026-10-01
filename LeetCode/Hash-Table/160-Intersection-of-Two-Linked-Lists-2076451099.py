# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_setting=set()
        while headA is not None:
            node_setting.add(headA)
            headA=headA.next
        while headB is not None:
            if headB in node_setting:
                return headB
            headB=headB.next
        