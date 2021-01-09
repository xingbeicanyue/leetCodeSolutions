"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:
* 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
* 要求使用空间复杂度为 O(1) 的原地算法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组
"""

from math import gcd
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 方法1：循环赋值最大公约数次，例如长度为6的数组右移4位，需要循环赋值0->4->2->0, 1->5->3->1共gcd(6,4)=2次
        length = len(nums)
        if length == 0 or k % length == 0:
            return
        for i in range(gcd(length, k % length)):
            nextIdx, lastVal = i, nums[i]
            while True:
                nextIdx = (nextIdx + k) % length
                nums[nextIdx], lastVal = lastVal, nums[nextIdx]
                if nextIdx == i:
                    break


        # 方法2：反转数组
        # if len(nums) == 0:
        #     return
        # k %= len(nums)
        # if k == 0:
        #     return
        # nums.reverse()
        # nums[:k] = nums[k - 1:: -1]
        # nums[k:] = nums[:k - 1: -1]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    print(nums)
    nums = [-1, -100, 3, 99]
    s.rotate(nums, 2)
    print(nums)
