from typing import List

class Solution:
    def linearSearch(self, nums: List[int], k: int)-> bool:
        if k in nums:
            return True
        return False
    
    # for i in nums:
    #   if i == k:
    #       return True
    # return False
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.linearSearch([13, 46, 24, 52, 20, 9], 23))
    
# Time Complexity: O(N), Space Complexity: O(1)