
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #get frequency
        hashmap = {}
        for n in nums:
            if n in hashmap: hashmap[n] += 1
            else: hashmap[n] = 1

        heap = []
        for k_i, v in hashmap.items():
            heapq.heappush(heap, (-1*v, k_i))


        return [heapq.heappop(heap)[1] for _ in range(k)]
