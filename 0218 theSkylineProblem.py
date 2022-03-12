"""
天际线问题

城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：
* lefti 是第 i 座建筑物左边缘的 x 坐标。
* righti 是第 i 座建筑物右边缘的 x 坐标。
* height i 是第 i 座建筑物的高度。

你可以假设所有的建筑都是完美的长方形，在高度为 0 的绝对平坦的表面上。

天际线应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标进行排序 。
关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。
此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

示例 1：
输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

示例 2：
输入：buildings = [[0,2,3],[2,5,3]]
输出：[[0,3],[5,0]]

提示：
* 1 <= buildings.length <= 10^4
* 0 <= lefti < righti <= 2^31 - 1
* 1 <= heighti <= 2^31 - 1
* buildings 按 lefti 非递减排序

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-skyline-problem
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 扫描线从左往右，用最大堆维护与扫描线相交的大楼，每次进出大楼时更新关键点
        result = []

        def addResult(x, y: int):
            if len(result) == 0:
                result.append([x, y])
            elif y != result[-1][1]:  # 相同的y坐标不需要记录
                result.append([x, y])

        scanRecs = []  # [(x坐标, 大楼下标, 扫描线是否进入大楼)]
        for i, building in enumerate(buildings):
            scanRecs.append((building[0], i, True))
            scanRecs.append((building[1], i, False))
        scanRecs.sort()
        topHeap = []  # 堆[(-高度, 大楼下标)]
        leaves = [False] * len(buildings)  # [是否已经离开下标对应的大楼]
        for i, scanRec in enumerate(scanRecs):
            buildingIdx = scanRec[1]
            if scanRec[2]:  # 进入
                heappush(topHeap, (-buildings[buildingIdx][2], buildingIdx))
            else:  # 离开
                leaves[buildingIdx] = True
                while len(topHeap) > 0 and leaves[topHeap[0][1]]:  # 移除已经离开的大楼
                    heappop(topHeap)
            if i == len(scanRecs) - 1 or scanRec[0] != scanRecs[i + 1][0]:
                addResult(scanRec[0], -topHeap[0][0] if len(topHeap) > 0 else 0)
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
    print(r)

    r = s.getSkyline([[0, 2, 3], [2, 5, 3]])
    print(r)
