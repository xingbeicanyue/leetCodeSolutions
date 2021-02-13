"""
和为K的子数组

给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

说明 :
* 数组的长度为 [1, 20,000]。
* 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、哈希表
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sum(nums[i:j]) = sum(nums[:j]) - sum(nums[:i])
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
