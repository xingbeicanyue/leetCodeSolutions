"""
组合

给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2：
输入：n = 1, k = 1
输出：[[1]]

提示：
* 1 <= n <= 20
* 1 <= k <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 方法1：
        # 使用组合函数
        return [list(nums) for nums in combinations(range(1, n + 1), k)]

        # 方法2：
        # 回溯
        # result, nums = [], []
        #
        # def addNumber(startNum: int):
        #     if len(nums) == k:
        #         result.append(nums[:])
        #         return
        #     for i in range(startNum, n + 1):
        #         nums.append(i)
        #         addNumber(i + 1)
        #         nums.pop()
        #
        # addNumber(1)
        # return result


if __name__ == '__main__':
    s = Solution()

    r = s.combine(4, 2)
    print(r)

    r = s.combine(1, 1)
    print(r)
