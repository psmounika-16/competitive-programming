# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp=ListNode()
        res=tmp
        sum=0
        head=head.next
        while head:
            if head.val!=0:
                sum+=head.val
            else:
                tmp2=ListNode()
                tmp2.val=sum
                tmp.next=tmp2
                tmp=tmp.next
                sum=0
            head=head.next
        res=res.next
        return res