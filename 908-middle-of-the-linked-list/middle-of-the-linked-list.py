# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        header = current
        count = 0
        while current!=None:
            count += 1
            current = current.next
        c = 0
        while header!=None:
            c+=1
            if c==(count//2)+1:
                return header
            header = header.next
        
            
            
