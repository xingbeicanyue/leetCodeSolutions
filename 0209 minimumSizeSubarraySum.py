"""
长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。
如果不存在符合条件的子数组，返回 0。

示例：
输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

进阶：
* 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 滑动窗口
        result, leftIdx = len(nums), 0
        for rightIdx, num in enumerate(nums):
            s -= num
            if s <= 0:
                while s <= 0:
                    s += nums[leftIdx]
                    leftIdx += 1
                result = min(result, rightIdx - leftIdx)
        return result + 2 if result < len(nums) else 0


if __name__ == '__main__':
    s = Solution()
    r = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(r)
