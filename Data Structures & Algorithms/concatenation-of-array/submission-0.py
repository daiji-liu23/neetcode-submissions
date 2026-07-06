class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst_length = len(nums)
        for i in range(0, lst_length): 
            nums.append(nums[i])
        
        return nums 

        