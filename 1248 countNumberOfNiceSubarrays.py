"""
统计「优美子数组」

给你一个整数数组 nums 和一个整数 k。
如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
请返回这个数组中「优美子数组」的数目。

示例 1：
输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。

示例 2：
输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。

示例 3：
输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16

提示：
* 1 <= nums.length <= 50000
* 1 <= nums[i] <= 10^5
* 1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIdxs = [-1] + [i for i, num in enumerate(nums) if num & 1] + [len(nums)]  # [奇数下标] + 哨兵
        return sum((oddIdxs[i] - oddIdxs[i - 1]) * (oddIdxs[i + k] - oddIdxs[i + k - 1])
                   for i in range(1, len(oddIdxs) - k))


if __name__ == '__main__':
    s = Solution()
    r = s.numberOfSubarrays([1, 1, 2, 1, 1], 3)
    print(r)
    r = s.numberOfSubarrays([2, 4, 6], 1)
    print(r)
    r = s.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2)
    print(r)
