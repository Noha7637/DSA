# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        arr = []
        while headA:
            arr.append(headA)
            headA = headA.next
        while headB:
            arr.append(headB)
            headB = headB.next
        freq = Counter(arr)
        for k, v in freq.items():
            if v==2:
                return k
        return None



        



