class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        n = len(students) 
        queue = deque(students) 

        res = n 
        for sandwich in sandwiches: 
            count = 0 
            while count < n and queue[0] != sandwich: 
                queue.append(queue.popleft())
                count += 1 
            
            if queue[0] == sandwich: 
                queue.popleft()
                res -= 1 
            else: 
                break

        return res 
        



