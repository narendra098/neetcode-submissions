import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = []
        cnt = Counter(nums)

        for num, count in cnt.items():
            heapq.heappush(hp, (count, num))
            if len(hp) > k:
                heapq.heappop(hp)
        
        return [num for count, num in hp]
        
        