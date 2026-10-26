class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ## Binary search both lists within lists 

        left_outer, right_outer = 0, len(matrix) - 1 
        left_inner, right_inner = 0, len(matrix[0]) - 1 

        ## First Handle Outer Case
        while left_outer <= right_outer:
            mid_outer = (left_outer + right_outer) // 2  
            if matrix[mid_outer][left_inner] > target: 
                right_outer = mid_outer - 1 
            elif matrix[mid_outer][right_inner] < target: 
                left_outer = mid_outer + 1
            
            else:   
                arr_contains_target = matrix[mid_outer]  
                break            
        
        if left_outer > right_outer: 
            return False

        while left_inner <= right_inner: 
            mid_inner = (left_inner + right_inner) // 2
            if arr_contains_target[mid_inner] > target: 
                right_inner = mid_inner - 1 
            elif arr_contains_target[mid_inner] < target: 
                left_inner = mid_inner + 1
            else: 
                return True
        
        return False
                


        