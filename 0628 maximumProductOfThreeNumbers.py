"""
三个数的最大乘积

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:
输入: [1,2,3]
输出: 6

示例 2:
输入: [1,2,3,4]
输出: 24

注意:
1. 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
2. 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、数学
"""

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1, max2, max3, min1, min2 = -1001, -1001, -1001, 1001, 1001  # 最大的3个数 | 最小的2个数
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)


if __name__ == '__main__':
    s = Solution()
    r = s.maximumProduct([1, 2, 3])
    print(r)
    r = s.maximumProduct([1, 2, 3, 4])
    print(r)
