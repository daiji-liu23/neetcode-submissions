class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## [1,4,3,2] -> 1 banada in the 0th pile, 4 banana in the 1st pile 

        ## Every hour eat a pile, pick an k such that you can eat all bananas within every pile, basically pick an  min(k) > all numbers in piles 

        # 8 -> 6 -> 4 -> 3 

        ## Binary search 

        def check_eats(mid):
            hours = 0
            for p in piles: 
                hours += (p + mid - 1) // mid
            return hours 
            
        low, high = 1, max(piles) 
        while low <= high: 
            mid_val = (low + high) // 2 
            if check_eats(mid_val) <= h: 
                high = mid_val - 1
                res = mid_val
            elif check_eats(mid_val) > h: 
                low = mid_val + 1 

        return res

        
             

