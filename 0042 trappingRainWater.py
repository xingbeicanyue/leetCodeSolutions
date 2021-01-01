"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
               __
       __     | |__  __
   __ | |░░░░░|   |░| |__
__| |░|   |░|           |

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（填充部分表示雨水）。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

提示：
* n == height.length
* 0 <= n <= 3 * 10^4
* 0 <= height[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、数组、双指针
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针，左右指针中间的位置至少能接水至左右指针中较低的高度
        result = 0
        leftIdx, rightIdx = 0, len(height) - 1
        while leftIdx < rightIdx:
            if height[leftIdx] <= height[rightIdx]:
                for i in range(leftIdx + 1, rightIdx):
                    if height[i] > height[leftIdx]:
                        leftIdx = i
                        break
                    result += height[leftIdx] - height[i]
                else:
                    leftIdx = rightIdx
            else:
                for i in range(rightIdx - 1, leftIdx, -1):
                    if height[i] > height[rightIdx]:
                        rightIdx = i
                        break
                    result += height[rightIdx] - height[i]
                else:
                    rightIdx = leftIdx
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(r)
    r = s.trap([4, 2, 0, 3, 2, 5])
    print(r)
