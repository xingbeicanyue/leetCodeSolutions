"""
和为K的子数组

给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

示例 1：
输入：nums = [1,1,1], k = 2
输出：2

示例 2：
输入：nums = [1,2,3], k = 3
输出：2

提示：
* 1 <= nums.length <= 2 * 10^4
* -1000 <= nums[i] <= 1000
* -10^7 <= k <= 10^7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、哈希表
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和 sum(nums[i:j]) = sum(nums[:j]) - sum(nums[:i])
        sums = defaultdict(int)  # sum(nums[:n])的计数字典
        sums[0] += 1
        result = sum_ = 0
        for num in nums:
            sum_ += num
            result += sums[sum_ - k]
            sums[sum_] += 1
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.subarraySum([1, 1, 1], 2)
    print(r)

    r = s.subarraySum([1, 2, 3], 3)
    print(r)
