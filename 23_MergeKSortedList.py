# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        first = ListNode(None)
        pointer = first
        min_value = 0
        min_index = 0
        num_pop = 0
        new_list = []
        for i in range(len(lists)):
            if (lists[i] != None):
                new_list.append(lists[i])
                continue

        while new_list != []:
            min_value = new_list[0].val
            min_index = 0
            # find the minimal value and its index
            for i in range(len(new_list)):
                if(new_list[i].val < min_value):
                    min_value = new_list[i].val
                    min_index = i
            new_list[min_index] = new_list[min_index].next
            if (new_list[min_index] == None):
                new_list.pop(min_index)
            pointer.val = min_value
            if(new_list != []):
                temp = ListNode(None)
                pointer.next = temp
                pointer = temp
        if (first.val == None):
            return []
        return first
