# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            if head.val not in arr:
                arr.append(head.val)
            head = head.next
        dummy = ListNode(0)
        current = dummy
        for i in range(len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return dummy.next
    