"""
无重叠区间

给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:
1. 可以认为区间的终点总是大于它的起点。
2. 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例 1:
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

示例 2:
输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

示例 3:
输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

提示:
* 1 <= intervals.length <= 10^5
* intervals[i].length == 2
* -5 * 10^4 <= starti < endi <= 5 * 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 贪心算法
        # 按右区间坐标升序排序，保留第1个区间，之后遍历时若发现有2个区间相交则删除后面一个
        # 因为两者相交必然要删除其中一个，若保留右区间坐标小的那个，后续产生的相交数必然更优或等优
        if len(intervals) == 0:
            return 0
        sortedIntervals = sorted(intervals, key=lambda x: x[1])
        lastVal, result = sortedIntervals[0][0], 0
        for interval in sortedIntervals:
            if interval[0] < lastVal:
                result += 1
            else:
                lastVal = interval[1]
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
    print(r)

    r = s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
    print(r)

    r = s.eraseOverlapIntervals([[1, 2], [2, 3]])
    print(r)
