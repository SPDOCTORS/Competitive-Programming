# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        current=head
        while current is not None:
            arr.append(current.val)
            current=current.next
        l,r=0,len(arr)-1
        while l<r:
            if arr[l]!=arr[r]:
                return False
            l=l+1
            r=r-1
        return True
        