from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        res = l = r = total = 0
        n = len(nums)

        while r < n:
            total += nums[r]
            while total > k and l < r:
                total -= nums[l]
                l += 1
            if total == k:
                res = max(res, r - l + 1)
            r += 1
        return res 

if __name__ == "__main__":
    ob = Solution()
    print(ob.longestSubarray([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3))
    
# Time Complexity: O(N), Space Complexity: O(1)