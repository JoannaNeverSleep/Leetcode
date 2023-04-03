'''203. Remove Linked List Elements'''

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        Goal : remove all the nodes of the linked list that has Node.val == val, and return the new head.
        """
        dummyhead = ListNode(next = head)
        cur = dummyhead
        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyhead.next
