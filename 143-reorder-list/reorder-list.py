# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return
        # finding the middle part 1
        head1 = head
        head2 = head
        count = 0
        while head1:
            head1=head1.next
            count+=1
        # finding the middle part 2 
        c = 0
        while head2:
            if c==count//2 - 1:
                break
            else:
                head2 = head2.next
                c+=1
        # reversing the nodes after the middle
        newhead = head2.next
        prev = None
        while newhead!=None:
            temp = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = temp
        head2.next = None
        # merging the two
        head1 = head
        head2 = prev
        while head2!=None:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp

            
            
            
        
        

        
        
        
        