"""
三数之和

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 此处使用简单的双层循环
        # 如果对数字做统计，并对重复数字单独处理可提升速度
        if len(nums) <= 2:
            return []
        sortedNums = sorted(nums)
        if sortedNums[-1] < 0:  # 全都为负数
            return []
        result = []
        for i, num in enumerate(sortedNums):
            if num > 0:  # 之后全都为正数
                break
            if i > 0 and num == sortedNums[i - 1]:
                continue
            lIdx, rIdx = i + 1, len(sortedNums) - 1
            while lIdx < rIdx:
                sumNum = num + sortedNums[lIdx] + sortedNums[rIdx]
                if sumNum < 0:
                    lIdx += 1
                elif sumNum > 0:
                    rIdx -= 1
                else:
                    result.append([num, sortedNums[lIdx], sortedNums[rIdx]])
                    while lIdx < rIdx and sortedNums[lIdx] == sortedNums[lIdx + 1]:
                        lIdx += 1
                    while lIdx < rIdx and sortedNums[rIdx] == sortedNums[rIdx - 1]:
                        rIdx -= 1
                    lIdx += 1
                    rIdx -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(r)
