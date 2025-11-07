from typing import List

class Solution:
    def insertionSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            j = i
            while j > 0 and nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
        return nums
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.insertionSort([13, 46, 24, 52, 20, 9]))