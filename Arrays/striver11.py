from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        index_map = {0: -1}    
        longest = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            # If prefix_sum - k seen before → valid subarray
            if prefix_sum - k in index_map:
                longest = max(longest, i - index_map[prefix_sum - k])

            # Only store FIRST occurrence of prefix_sum
            if prefix_sum not in index_map:
                index_map[prefix_sum] = i

        return longest  

if __name__ == "__main__":
    ob = Solution()
    print(ob.longestSubarray([1, -1, 0], 0))