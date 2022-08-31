class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cal_distance(point):
            return point[0] * point[0] + point[1] * point[1]
        
        points.sort(key=cal_distance)
        
        return points[0:k]