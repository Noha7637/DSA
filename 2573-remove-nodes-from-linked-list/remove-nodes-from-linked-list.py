# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        curr = prev
        maxi = 0
        arr = []
        while curr:
            if curr.val>=maxi:
                maxi = curr.val
                arr.append(maxi)
            curr = curr.next
        arr.reverse()
        dummy = ListNode(0)
        now = dummy
        for i in range(len(arr)):
            now.next = ListNode(arr[i])
            now = now.next
        return dummy.next


            
            
         