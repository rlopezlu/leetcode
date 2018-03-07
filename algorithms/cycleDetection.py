# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        speed1 = head
        speed2 = head
        while speed1 != None and speed2!= None:
            speed1 = speed1.next
            speed2 = speed2.next
            if(speed2 == None):
                return False
            speed2 = speed2.next
            if (speed1 == speed2):
                return True
        return False
        
