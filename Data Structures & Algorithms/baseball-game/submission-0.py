class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0 
        stack = []
        for i in range(0, len(operations)): 
            try: 
                num = int(operations[i])
                stack.append(num) 
            except ValueError: 
                if operations[i] == "+": 
                    sum1 = stack[-1] + stack[-2]
                    stack.append(sum1) 
                elif operations[i] == 'D': 
                    double = stack[-1] * 2
                    stack.append(double)
                else: 
                    stack.pop()
            
        for i in range(0, len(stack)): 
            score += stack[i] 

        return score







            
            

        