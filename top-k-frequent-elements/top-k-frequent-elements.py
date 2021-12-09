class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        h = {}
        for n in nums:
            if n in h.keys():
                h[n]+=1
            else:
                h[n]=1
        h={k: v for k, v in sorted(h.items(), key=lambda item: item[1])}
        h=[key for key in h.keys()]
        return [key for key in h[-k:]]
                