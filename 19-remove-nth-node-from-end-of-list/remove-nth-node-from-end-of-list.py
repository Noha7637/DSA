# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.pop(len(arr)-n)
        dummy = ListNode(0)
        current = dummy
        for i in range(len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return dummy.next