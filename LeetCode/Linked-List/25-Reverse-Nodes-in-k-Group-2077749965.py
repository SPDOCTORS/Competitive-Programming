# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        temp=head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
    def kthNode(self,temp,k):
        k-=1
        while temp is not None and k>0:
            temp=temp.next
            k-=1
        return temp
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        prevl=None
        while temp is not None:
            kthNode=self.kthNode(temp,k)
            if kthNode is None:
                if prevl:
                    prevl.next=temp
                break
            nextNode=kthNode.next
            kthNode.next=None
            self.reverse(temp)
            if temp==head:
                head=kthNode
            else:
                prevl.next=kthNode
            prevl=temp
            temp=nextNode
        return head
        