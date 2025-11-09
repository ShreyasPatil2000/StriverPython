from typing import List

class Solution:
    
    def swap(self, nums: List[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]
        
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[low]
        i = low
        j = high
        while i < j: 
            while nums[i] <= pivot and i <= high - 1:
                i += 1
            while nums[j] > pivot and j >= low + 1:
                j -= 1
            if i < j: 
                self.swap(nums, i, j)
        self.swap(nums, low, j)
        return j
    
    def quickSort(self, nums: List[int], low: int, high: int) -> List[int]:
        if(low < high):
            pi = self.partition(nums, low, high)
            self.quickSort(nums, low, pi - 1)
            self.quickSort(nums, pi + 1, high)
        return nums
        
if __name__ == "__main__":    
    ob = Solution()
    nums = [13, 46, 24, 52, 20, 9]
    low = 0
    high = len(nums) - 1
    print(ob.quickSort(nums, low, high))