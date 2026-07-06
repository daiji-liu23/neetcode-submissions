class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0 
        count = 0
        for i in range(0, len(nums)): 
            
            if nums[i] == 1: 
                count += 1 
            else: 
                if count > max_count: 
                    max_count = count 
                
                count = 0 
            
        if max_count > count: 
            return max_count
        else: 
            return count 
            

        