"""
滑动窗口中位数

中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
例如：
* [2,3,4]，中位数是 3
* [2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。
你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

示例：
给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。

提示：
* 你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
* 与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-median
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：Sliding Window
"""

from collections import defaultdict
from heapq import heapify, heappush, heappop
from typing import List, Dict


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 思路：
        # 维护一个最大堆A和一个最小堆B，A包含窗口中元素排序后的前半部分，B包含后半部分
        # 每次滑动窗口维护A和B
        # 获取中位数时，若k为偶数则中位数为两个堆顶的平均数；若为奇数则B的长度比A大，中位数为B堆顶

        def getValue(heap: List[int], removedNums: Dict[int, int]):
            """ 获取下一个有效值 """
            while True:
                val = heap[0]
                if removedNums[val] == 0:
                    return val
                removedNums[val] -= 1
                heappop(heap)

        if k == 1:
            return nums[:]
        result, firstKNums, right = [], sorted(nums[:k]), k - 1
        smallers = [-firstKNums[i] for i in range(k // 2)]
        heapify(smallers)
        biggers = firstKNums[k // 2:]
        heapify(biggers)
        removedSmallers, removedBiggers = defaultdict(int), defaultdict(int)
        while True:
            if k % 2 == 0:
                result.append((getValue(biggers, removedBiggers) - getValue(smallers, removedSmallers)) / 2)
            else:
                result.append(getValue(biggers, removedBiggers))
            # 移动窗格
            right += 1
            if right >= len(nums):
                return result
            leftNum, rightNum = nums[right - k], nums[right]
            # 移除、添加数据
            if leftNum == rightNum:
                continue
            if leftNum <= -getValue(smallers, removedSmallers):
                removedSmallers[-leftNum] += 1
                if rightNum <= getValue(biggers, removedBiggers):
                    heappush(smallers, -rightNum)
                else:
                    heappush(biggers, rightNum)
                    heappush(smallers, -getValue(biggers, removedBiggers))
                    heappop(biggers)
            else:
                removedBiggers[leftNum] += 1
                if rightNum >= -getValue(smallers, removedSmallers):
                    heappush(biggers, rightNum)
                else:
                    heappush(smallers, -rightNum)
                    heappush(biggers, -getValue(smallers, removedSmallers))
                    heappop(smallers)


if __name__ == '__main__':
    s = Solution()
    r = s.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(r)
