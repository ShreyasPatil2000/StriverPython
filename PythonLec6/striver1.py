from typing import List

class Solution:
    def countFrequencies(self, nums: List[int]) -> List[List[int]]:
        mapper = {}
        for i in nums:
            mapper[i] = mapper.get(i, 0) + 1
        count_list = []
        for i in mapper:
            count_list.append([i, mapper[i]])
        return count_list

if __name__ == "__main__":
    ob = Solution()
    print(ob.countFrequencies([1, 2, 2, 3, 3, 3, 4, 4]))