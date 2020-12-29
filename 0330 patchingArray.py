"""
给定一个已排序的正整数数组 nums，和一个正整数 n 。
从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。
请输出满足上述要求的最少需要补充的数字个数。

示例 1:
输入: nums = [1,3], n = 6
输出: 1
解释:
根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
所以我们最少需要添加一个数字。

示例 2:
输入: nums = [1,5,10], n = 20
输出: 2
解释: 我们需要添加 [2, 4]。

示例 3:
输入: nums = [1,2,2], n = 5
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/patching-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：贪心算法
"""

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        result, numIdx = 0, 0
        maxPatch = 1  # 当前能匹配到的最大整数+1
        while maxPatch <= n:
            if numIdx < len(nums) and maxPatch >= nums[numIdx]:
                maxPatch += nums[numIdx]
                numIdx += 1
            else:
                maxPatch += maxPatch
                result += 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.minPatches([1, 3], 6)
    print(r)
    r = s.minPatches([1, 5, 10], 20)
    print(r)
    r = s.minPatches([1, 2, 2], 5)
    print(r)
