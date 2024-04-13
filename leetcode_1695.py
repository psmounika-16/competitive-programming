class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans=0
        score=0
        lst=[]
        for i in nums:
            if i in lst:
                indx=lst.index(i)
                lst=lst[indx+1:]
                score=sum(lst)
            lst.append(i)
            score+=i
            ans=max(ans,score)
        return ans