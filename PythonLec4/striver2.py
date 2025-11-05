class Solution:
    def reverseNumber(self, n):
        c_num = n 
        r_num = 0
        if n < 0: 
            c_num = -c_num
        while c_num > 0:
            r = c_num % 10
            r_num = 10 * r_num + r
            c_num = c_num // 10
        if n < 0:
            return -r_num
        else:
            return r_num

if __name__ == "__main__":    
    ob = Solution()
    print(ob.reverseNumber(9243))