# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode(0)
        result = answer
        carry = 0
        sum = l1.val + l2.val + carry
        print(l1.val)
        print(sum)
        if sum > 9:
            answer.val = sum % 10 + carry
            carry = sum // 10
            answer.next = ListNode(carry)
            answer = answer.next
        else:
            answer.val = sum
        l1 = l1.next
        l2 = l2.next
        
        while(l1 != None and l2 != None):
            sum = l1.val + l2.val + carry
            if carry == 0:
                answer.next = ListNode(carry)
                answer = answer.next

            if sum > 9:
                answer.val = sum % 10
                
                carry = sum // 10
                answer.next = ListNode(carry)
                answer = answer.next
            else:
                answer.val = sum
                carry = 0
            l1 = l1.next
            l2 = l2.next
            
        while(l1 != None):
            if carry == 0:
                answer.next = ListNode(carry)
                answer = answer.next
            sum = l1.val + carry
            if sum > 9:
                answer.val = sum % 10
                carry = sum // 10
                answer.next = ListNode(carry)
                answer = answer.next
            else:
                answer.val = sum
                carry = 0
            l1 = l1.next

        while(l2 != None):
            if carry == 0:
                answer.next = ListNode(carry)
                answer = answer.next
            sum = l2.val + carry
            if sum > 9:
                answer.val = sum % 10
                carry = sum // 10
                answer.next = ListNode(carry)
                answer = answer.next
            else:
                answer.val = sum
                carry = 0
            l2 = l2.next
                
        return result