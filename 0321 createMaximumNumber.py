"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。
现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]

示例 2:
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]

示例 3:
输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/create-maximum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：贪心算法、动态规划
"""


class Solution:
    def maxNumber(self, nums1: list, nums2: list, k: int) -> list:
        from collections import deque

        def maxSubNumber(nums: list, k: int) -> deque:
            """ 返回由nums中元素组成的最大k位数字，且相对位置不变
                如：maxSubNumber([1, 5, 2, 3, 4], 3) -> [5, 3, 4]
            """
            # 思路同#402
            result = []
            delCount = len(nums) - k
            for num in nums:
                while result and delCount > 0 and num > result[-1]:
                    result.pop()
                    delCount -= 1
                result.append(num)
            del result[k:]
            return deque(result)

        def merge(nums1: deque, nums2: deque) -> list:
            """ 合并两个数字，返回满足下述条件的最大数字
               * 由两个数字的所有位组成，即长度为两者之和
               * 每个数字中每位的相对位置不变
               如：merge([3, 1, 1, 6], [4, 1, 7]) -> [4, 3, 1, 7, 1, 1, 6]
            """
            result = []
            while nums1 or nums2:
                bigger = nums1 if nums1 > nums2 else nums2
                result.append(bigger.popleft())
            return result

        # 在nums1|2中分别尝试获取长度为(0, k), (1, k-1) ... (k, 0)的最大子数字，然后合并，所有情况中选取最大值
        return max([merge(maxSubNumber(nums1, i), maxSubNumber(nums2, k - i))
                    for i in range(max(0, k - len(nums2)), min(len(nums1) + 1, k + 1))])


if __name__ == '__main__':
    s = Solution()
    r = s.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
    print(r)
    r = s.maxNumber([6, 7], [6, 0, 4], 5)
    print(r)
    r = s.maxNumber([3, 9], [8, 9], 3)
    print(r)
