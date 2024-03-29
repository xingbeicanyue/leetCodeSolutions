"""
目标和

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 - 中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例：
输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
一共有5种方法让最终目标和为3。

提示：
* 数组非空，且长度不会超过 20 。
* 初始的数组的和不会超过 1000 。
* 保证返回的最终结果能被 32 位整数存下。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        @lru_cache(None)
        def doFindWays(eIdx: int, target: int) -> int:
            """ 由nums[:eIdx+1]组成target的方法数 """
            if eIdx == 0:
                return (nums[0] == target) + (nums[0] == -target)
            return doFindWays(eIdx - 1, target - nums[eIdx]) + doFindWays(eIdx - 1, target + nums[eIdx])

        # 此处使用类似深度优先搜索的形式，也可以转为类似背包算法的形式
        sum_ = sum(nums)
        if (sum_ + S) % 2 == 1 or sum_ < abs(S):
            return 0
        return doFindWays(len(nums) - 1, S)


if __name__ == '__main__':
    s = Solution()
    r = s.findTargetSumWays([1, 1, 1, 1, 1], 3)
    print(r)
