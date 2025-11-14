from typing import List

class Solution:
    def unionArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        n = len(nums1)
        m = len(nums2)
        i = j = 0
        
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        nums.extend(nums1[i:])
        nums.extend(nums2[j:])
        return nums
    
    def intersectionArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        for n in nums1:
            if n in nums2:
                nums.append(n)
        return nums
        
if __name__ == "__main__":    
    ob = Solution()
    nums1 = [3, 4, 6, 7, 7, 9, 9]
    nums2 = [1, 5, 7, 7, 8, 8]
    print(ob.unionArray(nums1, nums2))
    print(ob.intersectionArray(nums1, nums2))
    
# Time Complexity: O(N), Space Complexity: O(N)