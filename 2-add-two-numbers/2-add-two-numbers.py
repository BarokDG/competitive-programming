# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        
        while l1.next != None:
            num1 += str(l1.val)
            l1 = l1.next
            
        num1 += str(l1.val)
        num1 = int(num1[::-1])
        
        while l2.next != None:
            num2 += str(l2.val)
            l2 = l2.next
        
        num2 += str(l2.val)
        num2 = int(num2[::-1])
        
        result = num1 + num2
        result = str(result)[::-1]
        
        newListNode = ListNode()
        newListNode.val = result[0]
        
        tempNode = newListNode
        
        for i in range(1, len(result)):
            tempNode.next = ListNode()
            tempNode.next.val = result[i]
            tempNode.next.next = None
            tempNode = tempNode.next
            
        return newListNode
