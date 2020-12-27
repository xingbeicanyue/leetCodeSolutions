"""
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

示例 1：
输入：n = 3, k = 3
输出："213"

示例 2：
输入：n = 4, k = 9
输出："2314"

示例 3：
输入：n = 3, k = 1
输出："123"

提示：
* 1 <= n <= 9
* 1 <= k <= n!

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数学、回溯算法
"""

from functools import reduce


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [i + 1 for i in range(n)]
        resultDigit = 0
        count = reduce(lambda x, y: x * y, range(1, n + 1), 1)
        for digitLeft in range(n, 0, -1):
            count //= digitLeft
            curIdx = (k - 1) // count
            resultDigit = resultDigit * 10 + digits[curIdx]
            digits.pop(curIdx)
            k -= count * curIdx
        return str(resultDigit)


if __name__ == '__main__':
    s = Solution()
    r = s.getPermutation(3, 3)
    print(r)
    r = s.getPermutation(4, 9)
    print(r)
    r = s.getPermutation(3, 1)
    print(r)
