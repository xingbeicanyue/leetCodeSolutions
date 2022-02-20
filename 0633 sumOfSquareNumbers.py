"""
平方数之和

给定一个非负整数 c，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

示例 2：
输入：c = 3
输出：false

提示：
* 0 <= c <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-square-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数学、双指针、二分查找
"""

from math import ceil


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 双指针，左值从0增加，右值从int(c**0.5)开始减少
        # 另外费马平方和定理也可以解此题
        left, right = 0, int(c ** 0.5)
        while left <= right:
            val = left * left + right * right
            if val < c:
                left = ceil((c - right * right) ** 0.5)  # left很可能连续加1，直接数值计算会更快
            elif val > c:
                right -= 1  # 通常right不会连续减1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()

    r = s.judgeSquareSum(5)
    print(r)

    r = s.judgeSquareSum(3)
    print(r)
