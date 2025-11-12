from typing import List

class Solution:
    def secondLargestElement(self, nums: List[int]) -> int:
        largest = nums[0]
        N2largest = -9999
        for i in range(1, len(nums)):
            if nums[i] > largest:
                N2largest = largest
                largest = nums[i]
            elif nums[i] < largest and nums[i] > N2largest:
                N2largest = nums[i]
        return N2largest 
    
    def secondSmallestElement(self, nums: List[int]) -> int:
        smallest = nums[0]
        N2smallest = 999999999
        for i in range(1, len(nums)):
            if nums[i] < smallest:
                N2smallest = smallest
                smallest = nums[i]
            elif nums[i] < smallest and nums[i] > N2smallest:
                N2smallest = nums[i]
        return N2smallest
    
if __name__ == "__main__":    
    ob = Solution()
    nums = [13, 46, 24, 52, 20, 9]
    print(ob.secondLargestElement(nums))
    print(ob.secondSmallestElement(nums))
    
# Time Complexity: O(N), Space Complexity: O(1)