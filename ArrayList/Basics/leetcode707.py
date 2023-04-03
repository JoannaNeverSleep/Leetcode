'''707. Design Linked List'''

# 单链表
class Node(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int

        Goal :  Get the value of the index^{th} node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        for i in range(index):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None

        Goal: Add a node of value val before the first element of the linked list. 
        """
        new_node = Node(val = val, next = self.head.next)
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(val = val)
        self.size += 1


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            new_node = Node(val= val, next = cur.next)
            cur.next = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        cur = self.head
        while index:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.size -= 1
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)