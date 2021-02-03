"""
子数组最大平均数 I

给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例：
输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

提示：
* 1 <= k <= n <= 30,000。
* 所给数据范围 [-10,000，10,000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subarray-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = acc = sum(nums[:k])
        for i in range(k, len(nums)):
            acc += (nums[i] - nums[i - k])
            result = max(result, acc)
        return result / k


if __name__ == '__main__':
    s = Solution()
    r = s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
    print(r)
