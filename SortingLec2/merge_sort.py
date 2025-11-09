from typing import List

class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[: mid]
        right = nums[mid: ]
        sortedLeft = self.mergeSort(left)
        sortedRight = self.mergeSort(right)
        return self.merge(sortedLeft, sortedRight)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.mergeSort([13, 46, 24, 52, 20, 9]))