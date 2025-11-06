from typing import List

class Solution:
    def reverse(self, arr: list, n: int, i: int) -> List[int]:
        if i >= n // 2:
            return arr
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        return self.reverse(arr, n, i + 1)
    
if __name__ == "__main__":
    ob = Solution()
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    i = 0
    print(ob.reverse(arr, n, i))