# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        arr = []
        while current!=None:
            arr.append(current)
            if arr.count(current)==2:
                return True
            current = current.next
        return False
        
            
            
        