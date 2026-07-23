class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for key, val in freq.items():
            heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for item in heap:
            res.append(item[1])
        return res

        