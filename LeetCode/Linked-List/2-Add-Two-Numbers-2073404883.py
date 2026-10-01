
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        temp=dummy
        carry=0
        while l1 or l2 or carry:
            sum=0
            if l1 :
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            sum+=carry
            carry=sum//10
            node=ListNode(sum%10)
            temp.next=node
            temp=temp.next
        return dummy.next
def printll(head):
    while head is not None:
        print(head.val,end="")
        head=head.next
    print()