
from heapq import *

class node:
    def __init__(self, point):
        self.point = point
        self.val = math.sqrt(math.pow(point[0],2)+math.pow(point[1],2))
    def __cmp__(self, other):
        return cmp(self.val, other.val)
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        nodes = [node(p) for p in points]
        heapq.heapify(nodes)

        return [heapq.heappop(nodes).point for _ in range(k)]
