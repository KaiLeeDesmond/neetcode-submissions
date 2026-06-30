class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        heap = []
        res = []
        for i in nums:
            hmap[i] = hmap.get(i,0)+1
        
        for x in hmap.keys():
            heapq.heappush(heap,(hmap[x],x))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for y in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res