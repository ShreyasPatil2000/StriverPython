from typing import List

class Solution:
    def mostFrequentElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        mapper = {}
        for i in nums:
            mapper[i] = mapper.get(i, 0) + 1
        max_count, res = 0, -1
        for value, count in mapper.items():
            if max_count < count:
                res = value
                max_count = count
        return res 

if __name__ == "__main__":
    ob = Solution()
    print(ob.mostFrequentElement([1, 2, 2, 2, 2, 2, 3, 3, 3, 3]))