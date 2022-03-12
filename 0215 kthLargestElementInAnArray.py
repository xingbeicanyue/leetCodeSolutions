"""
数组中的第K个最大元素

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

提示：
* 1 <= k <= nums.length <= 10^4
* -10^4 <= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from heapq import heapify, heappop, heappushpop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 方法1：
        # 建立大小为k的最小堆，遍历数据并维护堆
        # 时间复杂度：O(nlg(k))
        heap = nums[:k]
        heapify(heap)
        for i in range(k, len(nums)):
            heappushpop(heap, nums[i])
        return heap[0]


        # 方法2：
        # 原地建立最大堆，pop k-1次后取堆顶元素
        # 时间复杂度：θ(n + klg(n))
        # heap = [-num for num in nums]
        # heapify(heap)
        # for _ in range(1, k):
        #     heappop(heap)
        # return -heap[0]


        # 方法3：
        # 快速选择
        # 最低时间复杂度：O(n^2)  平均时间复杂度：θ(n)
        # def fastChoose(left, right, k: int):
        #     key = nums[left]
        #     left2, right2 = left, right
        #     while left2 < right2:
        #         while left2 < right2 and nums[right2] >= key:
        #             right2 -= 1
        #         nums[left2] = nums[right2]
        #         while left2 < right2 and nums[left2] < key:
        #             left2 += 1
        #         nums[right2] = nums[left2]
        #     nums[left2] = key
        #     topN = right - left2 + 1  # key是[left, right]中的第几大元素
        #     if topN == k:
        #         return key
        #     elif topN > k:
        #         return fastChoose(left2 + 1, right, k)
        #     else:
        #         return fastChoose(left, left2 - 1, k - topN)
        # return fastChoose(0, len(nums) - 1, k)


if __name__ == '__main__':
    s = Solution()

    r = s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    print(r)

    r = s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(r)
