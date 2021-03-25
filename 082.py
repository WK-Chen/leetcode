# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        n_list = ListNode(-1, head)
        curNode = n_list

        while curNode.next and curNode.next.next:
            if curNode.next.val == curNode.next.next.val:
                cur_val = curNode.next.val
                while curNode.next and curNode.next.val == cur_val:
                    curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return n_list.next