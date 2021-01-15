"""
所有蚂蚁掉下来前的最后一刻

有一块木板，长度为 n 个 单位 。一些蚂蚁在木板上移动，每只蚂蚁都以每秒一个单位的速度移动。
其中，一部分蚂蚁向左移动，其他蚂蚁向右移动。
当两只向不同方向移动的蚂蚁在某个点相遇时，它们会同时改变移动方向并继续移动。假设更改方向不会花费任何额外时间。
而当蚂蚁在某一时刻 t 到达木板的一端时，它立即从木板上掉下来。
给你一个整数 n 和两个整数数组 left 以及 right 。两个数组分别标识向左或者向右移动的蚂蚁在 t = 0 时的位置。
请你返回最后一只蚂蚁从木板上掉下来的时刻。

示例 1：
T = 0    A->  B->     <-C  <-D
         0    1    2    3    4

T = 1            <-B
              A->  C-><-D
         0    1    2    3    4

T = 1.5         B-> <-C
              <-A     D->
         0    1    2    3    4

T = 2            <-B
            <-A    C->  D->
         0    1    2    3    4

T = 3  <-A  <-B         C->  D->
         0    1    2    3    4

T = 4  <-B                   C->
         0    1    2    3    4

T = 5
         0    1    2    3    4
输入：n = 4, left = [4,3], right = [0,1]
输出：4
解释：如上图所示：
-下标 0 处的蚂蚁命名为 A 并向右移动。
-下标 1 处的蚂蚁命名为 B 并向右移动。
-下标 3 处的蚂蚁命名为 C 并向左移动。
-下标 4 处的蚂蚁命名为 D 并向左移动。
请注意，蚂蚁在木板上的最后时刻是 t = 4 秒，之后蚂蚁立即从木板上掉下来。（也就是说在 t = 4.0000000001 时，木板上没有蚂蚁）。

示例 2：
  *->  *->  *->  *->  *->  *->  *->  *->
  0    1    2    3    4    5    6    7
输入：n = 7, left = [], right = [0,1,2,3,4,5,6,7]
输出：7
解释：所有蚂蚁都向右移动，下标为 0 的蚂蚁需要 7 秒才能从木板上掉落。

示例 3：
  <-*  <-*  <-*  <-*  <-*  <-*  <-*  <-*
    0    1    2    3    4    5    6    7
输入：n = 7, left = [0,1,2,3,4,5,6,7], right = []
输出：7
解释：所有蚂蚁都向左移动，下标为 7 的蚂蚁需要 7 秒才能从木板上掉落。

示例 4：
输入：n = 9, left = [5], right = [4]
输出：5
解释：t = 1 秒时，两只蚂蚁将回到初始位置，但移动方向与之前相反。

示例 5：
输入：n = 6, left = [6], right = [0]
输出：6

提示：
* 1 <= n <= 10^4
* 0 <= left.length <= n + 1
* 0 <= left[i] <= n
* 0 <= right.length <= n + 1
* 0 <= right[i] <= n
* 1 <= left.length + right.length <= n + 1
* left 和 right 中的所有值都是唯一的，并且每个值只能出现在二者之一中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/last-moment-before-all-ants-fall-out-of-a-plank
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：脑筋急转弯、数组
"""

from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left) if left else 0, n - min(right) if right else 0)


if __name__ == '__main__':
    s = Solution()
    r = s.getLastMoment(4, [4, 3], [0, 1])
    print(r)
    r = s.getLastMoment(7, [], [0, 1, 2, 3, 4, 5, 6, 7])
    print(r)
    r = s.getLastMoment(7, [0, 1, 2, 3, 4, 5, 6, 7], [])
    print(r)
    r = s.getLastMoment(9, [5], [4])
    print(r)
    r = s.getLastMoment(6, [6], [0])
    print(r)
