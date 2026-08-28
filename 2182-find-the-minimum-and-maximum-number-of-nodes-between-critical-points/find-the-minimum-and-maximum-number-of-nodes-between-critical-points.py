# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        curr = head
        # traversing throught the list and changing it to array
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr1 = []
        if len(arr)==2:
            return [-1, -1]
        # appending the index
        for i in range(1, len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                arr1.append(i)
            elif arr[i]<arr[i-1] and arr[i]<arr[i+1]:
                arr1.append(i)
        if len(arr1)<2:
            return [-1, -1]
        maximum = arr1[-1]-arr1[0]
        minimum = 1000000
        for i in range(1, len(arr1)):
            temp = arr1[i]- arr1[i-1]
            if temp < minimum:
                minimum = temp
        return [minimum, maximum]

            
            

            
            
