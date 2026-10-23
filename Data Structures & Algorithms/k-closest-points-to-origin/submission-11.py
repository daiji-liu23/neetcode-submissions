class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        euclid = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(left, right): 
             pivot = right 
             pivotdist = euclid(points[pivot]) 
             i = left 
             for j in range(left, right): 
                if euclid(points[j]) <= pivotdist: 
                    points[i], points[j] = points[j], points[i]
                    i += 1
             points[i], points[right] = points[right], points[i]
             return i 

         
        left, right = 0, len(points) - 1
        pivot = len(points)

        while pivot != k: 
            pivot = partition(left, right)

            if pivot < k: 
                left = pivot + 1 
            else: 
                right = pivot - 1
        
        return points[:k]
        