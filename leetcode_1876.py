class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        windowsize=3
        slidingwindowcount=len(s)-windowsize+1
        index=0
        count=0
        while slidingwindowcount>0:
            lst=[]
            temstr=s[index:windowsize+index]
            for i in temstr:
                if i in lst:
                    break
                else:
                    lst.append(i)
            else:
                count+=1
            index+=1
            slidingwindowcount-=1
        return count