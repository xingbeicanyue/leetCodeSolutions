"""
x 的平方根

给你一个非负整数 x ，计算并返回 x 的算术平方根。

由于返回类型是整数，结果只保留整数部分，小数部分将被舍去。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

示例 1：
输入：x = 4
输出：2

示例 2：
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

提示：
0 <= x <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数学、二分查找
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            curVal = mid * mid
            if curVal < x:
                left = mid + 1
            elif curVal > x:
                right = mid - 1
            else:
                return mid
        return right


if __name__ == '__main__':
    s = Solution()

    r = s.mySqrt(4)
    print(r)

    r = s.mySqrt(8)
    print(r)
