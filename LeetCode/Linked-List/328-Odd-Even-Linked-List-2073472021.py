class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        array = []

        temp = head
        while temp:
            array.append(temp.val)
            temp = temp.next.next if temp.next else None

        temp = head.next
        while temp:
            array.append(temp.val)
            temp = temp.next.next if temp.next else None

        temp = head
        i = 0
        while temp:
            temp.val = array[i]
            temp = temp.next
            i += 1

        return head

        
        