"""
求众数 II

给定一个大小为n的整数数组，找出其中所有出现超过 ⌊n/3⌋ 次的元素。

示例1：
输入：[3,2,3]
输出：[3]

示例 2：
输入：nums = [1]
输出：[1]

示例 3：
输入：[1,1,1,3,3,2,2,2]
输出：[1,2]

提示：
* 1 <= nums.length <= 5 * 10^4
* -10^9 <= nums[i] <= 10^9

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、哈希表、计数、排序
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 类似于Boyer-Moore投票算法
        num1 = num2 = 1000000001
        count1 = count2 = 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1, count1 = num, 1
            elif count2 == 0:
                num2, count2 = num, 1
            else:
                count1 -= 1
                if count1 == 0:
                    num1 = 1000000001
                count2 -= 1
        # 检验
        result = []
        minCount = len(nums) // 3
        if count1 > 0 and nums.count(num1) > minCount:
            result.append(num1)
        if count2 > 0 and nums.count(num2) > minCount:
            result.append(num2)
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.majorityElement([3, 2, 3])
    print(r)

    r = s.majorityElement([1])
    print(r)

    r = s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2])
    print(r)
