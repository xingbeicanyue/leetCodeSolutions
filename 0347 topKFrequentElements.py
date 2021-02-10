"""
前 K 个高频元素

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：
* 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
* 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
* 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
* 你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：堆、哈希表
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 思路：
        # 统计数字出现次数，然后遍历所有数字并使用大小为k的堆维持前k多的数字
        # 此处直接使用Counter的接口
        return [num[0] for num in Counter(nums).most_common(k)]


if __name__ == '__main__':
    s = Solution()
    r = s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(r)
    r = s.topKFrequent([1], 1)
    print(r)
