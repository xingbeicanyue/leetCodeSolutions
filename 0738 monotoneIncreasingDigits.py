"""
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:
输入: N = 10
输出: 9

示例 2:
输入: N = 1234
输出: 1234

示例 3:
输入: N = 332
输出: 299

说明: N 是在 [0, 10^9] 范围内的一个整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/monotone-increasing-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：贪心算法
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = [int(c) for c in str(N)]
        # 找出第一个非递增的位置
        i = 1
        while i < len(digits):
            if digits[i] < digits[i - 1]:
                break
            i += 1
        else:  # 全部递增
            return N
        # 向前每位减1，保持递增为止
        for j in range(i - 1, -1, -1):
            digits[j] -= 1
            if digits[j] >= digits[j - 1]:  # 无所谓j是否为0
                break
        # 转为数字并返回
        result = 0
        for i in range(j + 1):
            result = result * 10 + digits[i]
        for _ in range(j + 1, len(digits)):  # 之后的位用9填充
            result = result * 10 + 9
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.monotoneIncreasingDigits(10)
    print(r)
    r = s.monotoneIncreasingDigits(1234)
    print(r)
    r = s.monotoneIncreasingDigits(332)
    print(r)
