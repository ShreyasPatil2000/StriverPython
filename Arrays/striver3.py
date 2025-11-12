from typing import List

class Solution:
    def isSorted(self, nums: List[int]) -> bool:
        #your code goes here
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True
        
if __name__ == "__main__":    
    ob = Solution()
    nums = [13, 46, 24, 52, 20, 9]
    print(ob.isSorted(nums))
    
# Time Complexity: O(N), Space Complexity: O(1)