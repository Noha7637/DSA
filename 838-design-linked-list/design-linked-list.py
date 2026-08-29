class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if index<0:
            return -1
        current = self.head
        count = 0
        while current:
            if count==index:
                return current.val
            current = current.next
            count+=1
        if index>count-1:
            return -1
    def addAtHead(self, val: int) -> None:
        newhead = ListNode(val)
        newhead.next = self.head
        self.head = newhead
    def addAtTail(self, val: int) -> None:
        newnode = ListNode(val)
        if not self.head:
            self.head = newnode
            return 
        current = self.head
        prev = None
        while current:
            prev = current
            current = current.next
        prev.next = newnode

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
        else:
            current = self.head
            count = 0
            newnode = ListNode(val)
            while current:
                if count == index-1:
                    temp = current.next
                    current.next = newnode
                    newnode.next = temp
                    break
                current = current.next
                count += 1
    def deleteAtIndex(self, index: int) -> None:
        if not self.head or index<0:
            return 
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            count = 0
            while current:
                if index == count:
                    prev.next = current.next
                    break
                prev = current
                current = current.next
                count+=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)