# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next==None:
            return head
        dummy1 = ListNode(0)
        dummy1.next = head
        current = dummy1
        arr1 = []
        arr2 = []
        count = 0
        while current:
            if count==left:
                break
            arr1.append(current)
            current = current.next
            count+=1 
        print(arr1)
        while current:
            if count==right:
                arr2.append(current)
                break
            arr2.append(current)
            current = current.next
            count+=1
        nextt = current.next
        dummy = ListNode(0)
        cur = dummy
        arr2.reverse()
        for i in range(len(arr2)):
            cur.next = arr2[i]
            cur = cur.next
        arr1[-1].next = dummy.next
        cur.next = nextt
        return dummy1.next
