class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1,2,3,4,5,6] -> [6,1,2,3,4,5] -> [5,6,1,2,3,4] -> [4,5,6,1,2,3] -> [3,4,5,6,1,2] 

        # Rotated between n times -> original array 
        # Min element always starts at beginning, moves to position n after rotation? 

        
        left, right = 0, len(nums) - 1 # Max rotations is len(nums) 
        
        smallest = nums[0]

        while left <= right: 
            mid = (left + right) // 2 
            if nums[mid] < smallest: 
                smallest = nums[mid] 
                right = mid - 1
            elif nums[mid] >= smallest:
                left = mid + 1 
        
        return smallest 
