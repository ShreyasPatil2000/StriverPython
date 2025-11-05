from typing import List

class Solution:
    def divisors(self, n: int) -> List[int]:
        divisors = [1]
        for i in range(2, n // 2):
            if not n%i:
                divisors.append(i)
        divisors.append(n)
        return divisors
    
if __name__ == "__main__":    
    ob = Solution()
    print(ob.divisors(153))