"""
计算各个位数不同的数字个数

给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。

示例:
输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 1位数9个，2位数9*9个，3位数9*9*8个，4位数9*9*8*7个...
        if n == 0:
            return 1
        result, cur = 9, 9
        for i in range(1, n):
            cur *= (10 - i)
            result += cur
        return result + 1


if __name__ == '__main__':
    s = Solution()
    r = s.countNumbersWithUniqueDigits(2)
    print(r)
