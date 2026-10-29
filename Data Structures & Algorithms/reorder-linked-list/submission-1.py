# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        ## Standard pointer approach 

        ## Slow and fast technique to get midpoint 

        slow = head 
        fast = head.next 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        # Slow is now the midpoint 

        # second = slow.next 
        # slow.next = None ## To cut the list in 2 just set first_half.next = None 
        # prev = None 
        # while second: 
        #     tmp = second.next 
        #     second.next = prev 
        #     prev = second 
        #     second = tmp 
        
        # first, second = head, prev 
        # while second: 
        #     tmp1, tmp2 = first.next, second.next 
        #     first.next = second  
        #     second.next = tmp1 
        #     first, second = tmp1, tmp2 
        
        ## Array solution 


        arr = [] 
        curr = head 
        while curr: 
            arr.append(curr)
            curr = curr.next 

        ## arr now stores the entire list 

        left, right = 0, len(arr) - 1 ## point inwards 
        while left < right: 
            arr[left].next = arr[right]
            left += 1 
            
            if left >= right:
                break

            arr[right].next = arr[left]
            right -= 1 
        
        arr[left].next = None
        
         


        

             





        


         
        

        