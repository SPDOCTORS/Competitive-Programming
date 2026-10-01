# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp1=list1
        temp2=list2
        while temp1:
            arr.append(temp1.val)
            temp1=temp1.next
        while temp2:
            arr.append(temp2.val)
            temp2=temp2.next
        arr.sort()
        dummyNode=ListNode(-1)
        temp=dummyNode
        for val in arr:
            temp.next=ListNode(val)
            temp=temp.next
        return dummyNode.next

        