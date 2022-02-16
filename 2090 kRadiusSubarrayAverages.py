"""
半径为 k 的子数组平均值

给你一个下标从 0 开始的数组 nums ，数组中有 n 个整数，另给你一个整数 k 。
半径为 k 的子数组平均值是指：nums 中一个以下标 i 为 中心且半径为 k 的子数组中所有元素的平均值，
即下标在 i - k 和 i + k 范围（含 i - k 和 i + k）内所有元素的平均值。
如果在下标 i 前或后不足 k 个元素，那么半径为 k 的子数组平均值是 -1 。

构建并返回一个长度为 n 的数组 avgs ，其中 avgs[i] 是以下标 i 为中心的子数组的半径为 k 的子数组平均值 。
x 个元素的平均值是 x 个元素相加之和除以 x ，此时使用截断式整数除法，即需要去掉结果的小数部分。

例如，四个元素 2、3、1 和 5 的平均值是 (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75，截断后得到 2 。

示例 1：
输入：nums = [7,4,3,9,1,8,5,2,6], k = 3
输出：[-1,-1,-1,5,4,4,-1,-1,-1]
解释：
- avg[0]、avg[1] 和 avg[2] 是 -1 ，因为在这几个下标前的元素数量都不足 k 个。
- 中心为下标 3 且半径为 3 的子数组的元素总和是：7 + 4 + 3 + 9 + 1 + 8 + 5 = 37 。
  使用截断式 整数除法，avg[3] = 37 / 7 = 5 。
- 中心为下标 4 的子数组，avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4 。
- 中心为下标 5 的子数组，avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4 。
- avg[6]、avg[7] 和 avg[8] 是 -1 ，因为在这几个下标后的元素数量都不足 k 个。

示例 2：
输入：nums = [100000], k = 0
输出：[100000]
解释：
- 中心为下标 0 且半径 0 的子数组的元素总和是：100000 。
  avg[0] = 100000 / 1 = 100000 。

示例 3：
输入：nums = [8], k = 100000
输出：[-1]
解释：
- avg[0] 是 -1 ，因为在下标 0 前后的元素数量均不足 k 。

提示：
* n == nums.length
* 1 <= n <= 10^5
* 0 <= nums[i], k <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-radius-subarray-averages
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、滑动窗口
"""

from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k * 2:
            return [-1] * len(nums)
        result = [-1] * k
        windowWidth = k * 2 + 1
        sumVal = sum(nums[i] for i in range(windowWidth))
        result.append(sumVal // windowWidth)
        for i in range(windowWidth, len(nums)):
            sumVal += nums[i] - nums[i - windowWidth]
            result.append(sumVal // windowWidth)
        result.extend([-1] * k)
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3)
    print(r)

    r = s.getAverages([100000], 0)
    print(r)

    r = s.getAverages([8], 100000)
    print(r)
