from typing import List

class Solution:
    def selectionSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            min_idx = i
            for j in range(i, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]  
            
        return nums
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.selectionSort([13, 46, 24, 52, 20, 9]))