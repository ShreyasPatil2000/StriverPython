from typing import List

class Solution:
    def largestElement(self, nums: List[int])-> int:
        maximum = nums[0]
        for i in range(1, len(nums)):
            maximum = max(maximum, nums[i])
        return maximum
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.largestElement([13, 46, 24, 52, 20, 9]))
    
# Time Complexity: O(N), Space Complexity: O(1)