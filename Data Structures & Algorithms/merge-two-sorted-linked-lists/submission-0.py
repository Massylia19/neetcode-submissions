# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        end = start

        while list1 and list2: 
            if list1.val < list2.val: 
                end.next = list1
                list1 = list1.next
            else: 
                end.next = list2 
                list2 = list2.next
                
            end = end.next

        if list1 is not None: 
            end.next = list1
        else:
            end.next = list2

        return start.next
        
        
