"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

示例 1：
    |              |
    |░░░░░░░░░░░░░░|░░░░░|
    |░░|░░░░░░░░░░░|░░░░░|
    |░░|░░░░░|░░░░░|░░░░░|
    |░░|░░░░░|░░|░░|░░░░░|
    |░░|░░░░░|░░|░░|░░|░░|
    |░░|░░|░░|░░|░░|░░|░░|
 |  |░░|░░|░░|░░|░░|░░|░░|
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为填充部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

示例 3：
输入：height = [4,3,2,1,4]
输出：16

示例 4：
输入：height = [1,2,1]
输出：2

提示：
* n = height.length
* 2 <= n <= 3 * 10^4
* 0 <= height[i] <= 3 * 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、双指针
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftIdx, rightIdx, result = 0, len(height) - 1, 0
        while leftIdx < rightIdx:
            if height[leftIdx] <= height[rightIdx]:
                result = max(result, height[leftIdx] * (rightIdx - leftIdx))
                leftIdx += 1
            else:
                result = max(result, height[rightIdx] * (rightIdx - leftIdx))
                rightIdx -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(r)
    r = s.maxArea([1, 1])
    print(r)
    r = s.maxArea([4, 3, 2, 1, 4])
    print(r)
    r = s.maxArea([1, 2, 1])
    print(r)
