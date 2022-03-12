"""
区域和检索 - 数组不可变

给定一个整数数组 nums，处理以下类型的多个查询:

计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的和 ，其中 left <= right

实现 NumArray 类：
* NumArray(int[] nums) 使用数组 nums 初始化对象
* int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的总和，
  包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right])

示例 1：
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]
解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

提示：
* 1 <= nums.length <= 10^4
* -10^5 <= nums[i] <= 10^5
* 0 <= i <= j < nums.length
* 最多调用 10^4 次 sumRange 方法

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self._sums = [0]
        for num in nums:
            self._sums.append(self._sums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self._sums[right + 1] - self._sums[left]


if __name__ == '__main__':
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(0, 2))
    print(numArray.sumRange(2, 5))
    print(numArray.sumRange(0, 5))
