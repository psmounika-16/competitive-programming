class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans=math.inf
        lastseen={}
        for i,card in enumerate(cards):
            if card in lastseen:
                ans=min(ans,i-lastseen[card]+1)
            lastseen[card]=i
        return -1 if ans==math.inf else ans 