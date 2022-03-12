"""
最长连续序列

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

提示：
* 0 <= nums.length <= 10^4
* -10^9 <= nums[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Dict, List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        # 方法1：转为集合，对任意取出的不重复数字向两边延申探索，返回最大区间长度
        numSet, result = set(nums), 0
        while numSet:
            num = numSet.pop()
            minVal, maxVal = num - 1, num + 1
            while minVal in numSet:
                numSet.remove(minVal)
                minVal -= 1
            while maxVal in numSet:
                numSet.remove(maxVal)
                maxVal += 1
            result = max(result, maxVal - minVal - 1)
        return result

        # 方法2：并查集
        # 对访问的数字，分别连接其前后数字，相邻数字即合并为一个群组，最终返回最大群组的元素数
        # disjointSet = {}  # {数字: [父节点数字, 群组元素数（仅根节点有效）]}
        #
        # def getRoot(idx: int) -> List[int]:
        #     """ 获取并查集根节点及群组大小 """
        #     visiteds = []
        #     while idx != disjointSet[idx][0]:
        #         visiteds.append(idx)
        #         idx = disjointSet[idx][0]
        #     for visited in visiteds:
        #         disjointSet[visited][0] = idx
        #     return disjointSet[idx]
        #
        # def connect(idx1: int, idx2: int):
        #     """ 合并并查集中的两个元素 """
        #     r1, r2 = getRoot(idx1), getRoot(idx2)
        #     if r1[0] != r2[0]:
        #         r2[0], r1[1] = r1[0], r1[1] + r2[1]
        #
        # for num in nums:
        #     if num not in disjointSet:
        #         disjointSet[num] = [num, 1]
        #     if num - 1 in disjointSet:
        #         connect(num, num - 1)
        #     if num + 1 in disjointSet:
        #         connect(num, num + 1)
        # return max(disjointSet[num][1] for num in disjointSet if num == disjointSet[num][0]) if disjointSet else 0


if __name__ == '__main__':
    s = Solution()

    r = s.longestConsecutive([100, 4, 200, 1, 3, 2])
    print(r)

    r = s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    print(r)
