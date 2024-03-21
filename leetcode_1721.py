# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        leftpos=head
        rightpos=head
        tmp=head
        leftcount=1
        while tmp:
            if leftcount<k:
                leftcount+=1
                leftpos=leftpos.next
            else:
                if tmp.next:
                    rightpos=rightpos.next
            tmp=tmp.next
        leftpos.val,rightpos.val=rightpos.val,leftpos.val
        return head