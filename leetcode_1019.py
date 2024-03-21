# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        i=0
        l=len(lst)
        ans=[0]*1
        tmp=[]
        while i<l:
            while tmp and lst[tmp[-1]]<lst[i]:
                ans[tmp[-1]]=lst[i]
                tmp.pop()
            tmp.append(i)
            i+=1
        return ans