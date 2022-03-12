"""
最小区间

你有 k 个非递减排列的整数列表。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

示例 1：
输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释：
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。

示例 2：
输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]

示例 3：
输入：nums = [[10,10],[11,11]]
输出：[10,11]

示例 4：
输入：nums = [[10],[11]]
输出：[10,11]

示例 5：
输入：nums = [[1],[2],[3],[4],[5],[6],[7]]
输出：[1,7]

提示：
* nums.length == k
* 1 <= k <= 3500
* 1 <= nums[i].length <= 50
* -10^5 <= nums[i][j] <= 10^5
* nums[i] 按非递减顺序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import defaultdict
from heapq import heapify, heapreplace
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 方法1：维护堆，及堆中的最大最小值
        numRecs = [(nums[i][0], i, 0) for i in range(len(nums))]  # [(值, 所属数组下标, 值在数组中的下标)]
        heapify(numRecs)
        resultRange, result, maxValue = 200001, None, max((numRec[0] for numRec in numRecs))
        while True:
            curNumRec = numRecs[0]
            curNum, curNums, curNumIdx = curNumRec[0], nums[curNumRec[1]], curNumRec[2]
            if maxValue - curNum < resultRange:
                resultRange, result = maxValue - curNum, [curNum, maxValue]
            if curNumIdx == len(curNums) - 1:
                break
            heapreplace(numRecs, (curNums[curNumIdx + 1], curNumRec[1], curNumIdx + 1))
            maxValue = max(maxValue, curNums[curNumIdx + 1])
        return result


        # 方法2：排序 + 双指针
        # numRecs = sorted((num, i) for i, curNums in enumerate(nums) for num in curNums)  # [(值, 所属数组下标)]
        # resultRange, result, left, right, groupNumber, valueNumber = 200001, None, 0, -1, len(nums), len(numRecs)
        # groupCounts = defaultdict(int)  # {数组下标, 数组包含了双指针区间内数字的个数}
        # while True:
        #     # 移动右指针至包含所有数组
        #     while right < valueNumber - 1 and len(groupCounts) < groupNumber:
        #         right += 1
        #         groupCounts[numRecs[right][1]] += 1
        #     if len(groupCounts) < groupNumber:
        #         return result
        #     # 移动左指针至不包含所有数组，同时更新结果
        #     while len(groupCounts) == groupNumber:
        #         if numRecs[right][0] - numRecs[left][0] < resultRange:
        #             resultRange, result = numRecs[right][0] - numRecs[left][0], [numRecs[left][0], numRecs[right][0]]
        #         groupCounts[numRecs[left][1]] -= 1
        #         if groupCounts[numRecs[left][1]] == 0:
        #             del groupCounts[numRecs[left][1]]
        #         left += 1


if __name__ == '__main__':
    s = Solution()
    r = s.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
    print(r)
    r = s.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    print(r)
    r = s.smallestRange([[10, 10], [11, 11]])
    print(r)
    r = s.smallestRange([[10], [11]])
    print(r)
    r = s.smallestRange([[1], [2], [3], [4], [5], [6], [7]])
    print(r)
