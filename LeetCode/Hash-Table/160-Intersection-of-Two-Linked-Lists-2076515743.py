# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1=headA
        temp2=headB
        cnt1,cnt2=0,0
        while temp1:
            cnt1+=1
            temp1=temp1.next
        while temp2:
            cnt2+=1
            temp2=temp2.next
        if cnt1<cnt2:
            return self.collision(headA,headB,cnt2-cnt1)
        return self.collision(headB,headA,cnt1-cnt2)
    def collision(self,smallerhead,longerhead,lengthdiff):
        temp1,temp2=smallerhead,longerhead
        for _ in range(lengthdiff):
            temp2=temp2.next
        while temp1!=temp2:
            temp1=temp1.next
            temp2=temp2.next
        return temp1        