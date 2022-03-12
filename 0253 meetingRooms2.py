"""
会议室 II

给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，
为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1：
输入：intervals = [[0,30],[5,10],[15,20]]
输出：2

示例 2：
输入：intervals = [[7,10],[2,4]]
输出：1

提示：
* 1 <= intervals.length <= 10^4
* 0 <= starti < endi <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        meetingsHeap = [intervals[0][1]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= meetingsHeap[0]:  # 延迟弹出，只需弹出1个，即可保证会议室数量不增加
                heappop(meetingsHeap)
            heappush(meetingsHeap, intervals[i][1])
        return len(meetingsHeap)  # 会议室数量不会下降，最终数量即为最大数量


if __name__ == '__main__':
    s = Solution()
    r = s.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
    print(r)
    r = s.minMeetingRooms([[7, 10], [2, 4]])
    print(r)
