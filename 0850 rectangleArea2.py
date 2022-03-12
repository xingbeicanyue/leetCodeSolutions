"""
矩形面积 II

我们给出了一个（轴对齐的）二维矩形列表rectangles。
对于rectangle[i] = [xi1, yi1, xi2, yi2]，其中(xi1, yi1)是该矩形左下角的坐标，(xi2, yi2)是该矩形右上角的坐标。
计算平面中所有rectangles所覆盖的总面积。任何被两个或多个矩形覆盖的区域应只计算一次。
返回总面积。因为答案可能太大，返回10 ^ 9 + 7 的模。

示例 1：
输入：rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
输出：6

示例 2：
输入：rectangles = [[0,0,1000000000,1000000000]]
输出：49
解释：答案是 1018 对 (10 ^ 9 + 7) 取模的结果，即 49 。

提示：
* 1 <= rectangles.length <= 200
* rectanges[i].length = 4
* 0 <= xi1, yi1, xi2, yi2 <= 10^9
* 矩形叠加覆盖后的总面积不会超越2^63 - 1，这意味着可以用一个 64 位有符号整数来保存面积结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rectangle-area-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # 使用扫描线法，将矩形左右边界分别作为检查点，按x坐标升序排序；使用线段树维护扫描线与矩形相交的总长度
        # 扫描线在矩形左边界时在线段树中加入区间，右边界则移除区间，两者均要计算相邻检查点间矩形的面积
        # 所有检查点间矩形面积之和即为所求

        class SegmentTreeNode:
            """ 线段树节点 """
            def __init__(self, bottom: int, top: int):
                self.leftChild = self.rightChild = None
                self.bottom, self.top = bottom, top
                self.count = 0  # 完全覆盖此节点区间的矩形数 + 子节点count之和

        def createSegmentTree() -> SegmentTreeNode:
            """ 创建线段树 """
            ys = {rec[1] for rec in rectangles} | {rec[3] for rec in rectangles}  # 所有的y坐标
            sortedYs = sorted(ys)
            nodes = [SegmentTreeNode(sortedYs[i], sortedYs[i + 1]) for i in range(len(sortedYs) - 1)]

            def createNode(sIdx: int, eIdx: int) -> SegmentTreeNode:
                """ 创建包含nodes[sIdx, eIdx]的线段树节点 """
                if sIdx == eIdx:
                    return nodes[sIdx]
                result = SegmentTreeNode(nodes[sIdx].bottom, nodes[eIdx].top)
                midIdx = (sIdx + eIdx) // 2
                result.leftChild = createNode(sIdx, midIdx)
                result.rightChild = createNode(midIdx + 1, eIdx)
                return result
            return createNode(0, len(nodes) - 1)

        def addOrRemoveSegment(node: SegmentTreeNode, bottom: int, top: int, addCount: int):
            """ 在线段树中添加或移除区域 """
            if node.bottom < top and node.top > bottom:  # 节点与添加区域有交集
                if node.bottom < bottom or node.top > top:  # 节点没有被添加区域完全覆盖时需要传递至子节点
                    addCount = addOrRemoveSegment(node.leftChild, bottom, top, addCount) +\
                               addOrRemoveSegment(node.rightChild, bottom, top, addCount)
                node.count += addCount
                return addCount
            return 0

        def getSegmentLen(node: SegmentTreeNode) -> int:
            """ 获取线段树中区间总长度 """
            if node.count == 0:
                return 0
            elif (node.leftChild is None) or (node.count > node.leftChild.count + node.rightChild.count):  # 全覆盖
                return node.top - node.bottom
            else:
                return getSegmentLen(node.leftChild) + getSegmentLen(node.rightChild)

        segmentTree = createSegmentTree()
        scanlines = []  # [扫描线]  # 扫描线: (x坐标, 下边界y坐标, 上边界y坐标, 是否矩形左边界)
        for rec in rectangles:
            scanlines.append((rec[0], rec[1], rec[3], True))
            scanlines.append((rec[2], rec[1], rec[3], False))
        scanlines.sort()  # 扫描线按x坐标升序排序
        result = 0
        for i, scanline in enumerate(scanlines):
            if i > 0 and scanline[0] > scanlines[i - 1][0]:
                result += (scanline[0] - scanlines[i - 1][0]) * getSegmentLen(segmentTree)
            if scanline[3]:
                addOrRemoveSegment(segmentTree, scanline[1], scanline[2], 1)
            else:
                addOrRemoveSegment(segmentTree, scanline[1], scanline[2], -1)
        return result % 1000000007


if __name__ == '__main__':
    s = Solution()

    r = s.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]])
    print(r)

    r = s.rectangleArea([[0, 0, 1000000000, 1000000000]])
    print(r)
