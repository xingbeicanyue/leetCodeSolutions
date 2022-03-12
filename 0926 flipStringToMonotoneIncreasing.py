"""
将字符串翻转到单调递增

如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，
那么该字符串是单调递增的。
我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
返回使 S 单调递增的最小翻转次数。

示例 1：
输入："00110"
输出：1
解释：我们翻转最后一位得到 00111。

示例 2：
输入："010110"
输出：2
解释：我们翻转得到 011111，或者是 000111。

示例 3：
输入："00011000"
输出：2
解释：我们翻转得到 00000000。

提示：
* 1 <= S.length <= 20000
* S 中只包含字符 '0' 和 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flip-string-to-monotone-increasing
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        result = allZeros = zeros = ones = 0  # 0的总个数 | -当前位置（包括）之前0 | 1的个数
        for i, c in enumerate(S):
            if c == '0':
                zeros -= 1
                allZeros += 1
                result = min(result, zeros + ones)
            else:
                ones += 1
        return result + allZeros


if __name__ == '__main__':
    s = Solution()
    r = s.minFlipsMonoIncr('00110')
    print(r)
    r = s.minFlipsMonoIncr('010110')
    print(r)
    r = s.minFlipsMonoIncr('00011000')
    print(r)
