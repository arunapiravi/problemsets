Remove Duplicates from Sorted List II
DescriptionHintsSubmissionsDiscussSolution
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

# Logic: maintain 3 ptrs - prev(first_occurance), first occurance, next non-duplicate number in the list
#  Make prev = None, first = head and last = head.next
# if first.val == last.val, just increment last ptr to get to non-duplicate number, then point prev to last
# if prev == None, which means we have duplicates in the beginning, point head to last.
# if we exited the loop with dup = True, point the prev to last


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### Runtime: O(N), space: 0(1), complexity: medium

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        prev_first = None
        first = head
        last = head.next
        dup = False
        
        while last != None:
            if first.val == last.val:
                last = last.next
                dup = True
            else:
                if dup:
                    # we find duplicates in the beginning
                    if prev_first == None:
                        head = last
                    else:
                        prev_first.next=last
                    dup = False
                    first = last
                    last = last.next
                else:
                    prev_first = first
                    first = first.next
                    last = last.next
        
        if dup:
            # there are duplicates we have to remove
            if prev_first == None:
                head = last
            else:
                prev_first.next=last
        return head
                
