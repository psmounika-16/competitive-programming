class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        d=defaultdict(int)
        l=[]
        for i in range(0,len(s)-10+1):
            s1=s[i:i+10]
            d[s1]+=1
            if d[s1]==2:
                l+=[s1]
        return l
