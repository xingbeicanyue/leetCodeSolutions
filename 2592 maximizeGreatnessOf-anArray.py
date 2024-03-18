"""
最大化数组的伟大值

给你一个下标从 0 开始的整数数组 nums 。你需要将 nums 重新排列成一个新的数组 perm 。
定义 nums 的 伟大值 为满足 0 <= i < nums.length 且 perm[i] > nums[i] 的下标数目。
请你返回重新排列 nums 后的 最大 伟大值。

示例 1：
输入：nums = [1,3,5,2,1,3,1]
输出：4
解释：一个最优安排方案为 perm = [2,5,1,3,3,1,1] 。
在下标为 0, 1, 3 和 4 处，都有 perm[i] > nums[i] 。因此我们返回 4 。

示例 2：
输入：nums = [1,2,3,4]
输出：3
解释：最优排列为 [2,3,4,1] 。
在下标为 0, 1 和 2 处，都有 perm[i] > nums[i] 。因此我们返回 3 。

提示：
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""

from collections import Counter
from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # 方法1：
        # 排序后通过双指针同向移动，统计两个指针不同时的计数
        # nums.sort()
        # result = 0
        # left = right = len(nums) - 1
        # while left >= 0:
        #     if nums[right] > nums[left]:
        #         result += 1
        #         right -= 1
        #     left -= 1
        # return result

        # 方法2：
        # 在方法1中，两个指针最大的距离即为最小不匹配数（到最后未到达终点的指针离终点的距离即为最小不匹配数）
        # 因此，总数-最小不匹配数即为所求。而指针在众数最多的数字时取得最小不匹配数。
        return len(nums) - max(Counter(nums).values())


if __name__ == "__main__":
    s = Solution()

    r = s.maximizeGreatness([1, 3, 5, 2, 1, 3, 1])
    print(r)

    r = s.maximizeGreatness([1, 2, 3, 4])
    print(r)
