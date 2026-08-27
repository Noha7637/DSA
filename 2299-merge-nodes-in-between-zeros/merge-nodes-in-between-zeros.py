# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        final = head
        arr = []
        summation = 0
        head=head.next
        while head:
            if head.val!=0:
                summation+=head.val
            elif head.val==0:
                arr.append(summation)
                summation = 0
            head = head.next
        current = final
        for i in range(len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return final.next

                
        