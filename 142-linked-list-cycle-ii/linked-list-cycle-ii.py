# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        arr = []
        count = 0
        while current!=None:
            arr.append(current)
            if arr.count(current)==2:
                return current
            current = current.next
        return None