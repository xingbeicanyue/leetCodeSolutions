"""
一和零

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中最多有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

示例 1：
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

示例 2：
输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。

提示：
* 1 <= strs.length <= 600
* 1 <= strs[i].length <= 100
* strs[i] 仅由 '0' 和 '1' 组成
* 1 <= m, n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ones-and-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、字符串、动态规划
"""

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 01背包问题，容量限制为m、n；价值均为1
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # [[dp[i][j]表示m=i,n=j的限制下最大子集大小]]
        for s in strs:
            count0, count1 = s.count('0'), s.count('1')
            for i in range(m, count0 - 1, -1):
                for j in range(n, count1 - 1, -1):
                    if i >= count0 and j >= count1:
                        dp[i][j] = max(dp[i][j], dp[i - count0][j - count1] + 1)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()

    r = s.findMaxForm(['10', '0001', '111001', '1', '0'], 5, 3)
    print(r)

    r = s.findMaxForm(['10', '0', '1'], 1, 1)
    print(r)
