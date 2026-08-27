# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenarr = []
        oddarr = []
        count = 0
        while head:
            count += 1
            if count%2==0:
                evenarr.append(head.val)
            elif count%2!=0:
                oddarr.append(head.val)
            head = head.next
        dummy = ListNode(0)
        current = dummy
        for i in range(len(oddarr)):
            current.next = ListNode(oddarr[i])
            current = current.next
        for j in range(len(evenarr)):
            current.next = ListNode(evenarr[j])
            current = current.next
        return dummy.next
    
            
            



        