class Solution:
    def count(self, n: int) -> int:
        t = 0
        while n!=0:
            n = n//10
            t += 1
        return t
    
    def isArmstrong(self, n: int) -> bool:
        c_num = n
        count = self.count(c_num)
        sum = 0
        while c_num != 0:
            r = c_num % 10
            sum += pow(r, count)
            c_num //= 10
        if sum == n: 
            return True
        else:
            return False
    
if __name__ == "__main__":    
    ob = Solution()
    print(ob.isArmstrong(153))