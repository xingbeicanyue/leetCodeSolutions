"""
优势洗牌

给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。

返回 A 的任意排列，使其相对于 B 的优势最大化。

示例 1：
输入：A = [2,7,11,15], B = [1,10,4,11]
输出：[2,11,7,15]

示例 2：
输入：A = [12,24,8,32], B = [13,25,32,11]
输出：[24,32,8,12]

提示：
* 1 <= A.length = B.length <= 10000
* 0 <= A[i] <= 10^9
* 0 <= B[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/advantage-shuffle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 贪心
        # 对nums2从大到小匹配，如果nums1中存在比其大的数，任意选一即可，简单起见选择nums1中最大的数
        # 如果nums1中不存在比其大的数，则选最小的数，对之后的影响最小
        n = len(nums1)
        sortedNums1 = sorted(nums1)
        sortedNumsIdx2 = sorted(range(n), key=lambda x: nums2[x], reverse=True)
        left, right = 0, n - 1
        result = [0] * n
        for numIdx2 in sortedNumsIdx2:
            if nums2[numIdx2] < sortedNums1[right]:
                result[numIdx2] = sortedNums1[right]
                right -= 1
            else:
                result[numIdx2] = sortedNums1[left]
                left += 1
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.advantageCount([2, 7, 11, 15], [1, 10, 4, 11])
    print(r)

    r = s.advantageCount([12, 24, 8, 32], [13, 25, 32, 11])
    print(r)
