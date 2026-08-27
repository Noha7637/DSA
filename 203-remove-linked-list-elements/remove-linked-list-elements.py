# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        arr = []
        while head:
            if head.val!=val:
                arr.append(head.val)
            head = head.next
        dummy = ListNode(0)
        current = dummy
        for i in range(len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return dummy.next