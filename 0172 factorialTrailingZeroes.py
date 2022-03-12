"""
阶乘后的零

给定一个整数 n ，返回 n! 结果中尾随零的数量。

提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

示例 1：
输入：n = 3
输出：0
解释：3! = 6 ，不含尾随 0

示例 2：
输入：n = 5
输出：1
解释：5! = 120 ，有一个尾随 0

示例 3：
输入：n = 0
输出：0

提示：
* 0 <= n <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 统计分解质因数后5的次数即为0的个数
        result, f = 0, 5
        while f <= n:
            result += n // f
            f *= 5
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.trailingZeroes(3)
    print(r)

    r = s.trailingZeroes(5)
    print(r)

    r = s.trailingZeroes(0)
    print(r)
