"""
数组的度

给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:
输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2:
输入: [1,2,2,3,1,4,2]
输出: 6

注意:
* nums.length 在1到50,000区间范围内。
* nums[i] 是一个在0到49,999范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        numberIdxDict = {}  # {数字: [下标]}
        for i, num in enumerate(nums):
            numberIdxDict.setdefault(num, []).append(i)
        maxCount, result = 0, len(nums)
        for idxs in numberIdxDict.values():
            if len(idxs) > maxCount:
                maxCount, result = len(idxs), idxs[-1] - idxs[0]
            elif len(idxs) == maxCount:
                result = min(result, idxs[-1] - idxs[0])
        return result + 1


if __name__ == '__main__':
    s = Solution()
    r = s.findShortestSubArray([1, 2, 2, 3, 1])
    print(r)
    r = s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
    print(r)
