# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# creates a single node in the linked list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        current = head
        while current:
            array.append(current.val)
            current = current.next
        reverse = array[::-1] # reverse the array

        # make new array
        if not reverse:
            return None
        new_head = ListNode(reverse[0])
        current = new_head
        for val in reverse[1:]:
            current.next = ListNode(val)
            current = current.next
        return new_head
        