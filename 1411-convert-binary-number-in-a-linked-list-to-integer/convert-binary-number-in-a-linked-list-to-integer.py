# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        arr = []
        while current != None:
            arr.append(current.val)
            current = current.next
        arr.reverse()
        total = 0
        for i in range(len(arr)):
            total+=arr[i]*2**i
        return total
            
            


        