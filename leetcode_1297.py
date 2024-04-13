class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict
        d=defaultdict(int)
        for i in range(minSize,maxSize+1):
            for j in range(0,len(s)-i+1):
                s1=s[j:j+i]
                l=set(list(s1))
                if len(l)<=maxLetters:
                    d[s1]+=1
                else:
                    d[s1]=0
        return max(d.values())