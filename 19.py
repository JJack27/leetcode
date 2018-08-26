# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        before_node = ListNode(0)
        before_node.next = head
        pointer = head 
        for i in range(n):
            pointer = pointer.next
        if pointer == None:
            return head.next
        else:
            while pointer != None:
                pointer = pointer.next
                before_node = before_node.next
            before_node.next = before_node.next.next
        return head


            



