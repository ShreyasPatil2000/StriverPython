from typing import List

class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(n-1-i):
                if(nums[j] > nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]    
                    swapped = True 
            if swapped == False:
                break      
        return nums
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.bubbleSort([13, 46, 24, 52, 20, 9]))