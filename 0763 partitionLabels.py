"""
划分字母区间

字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

示例：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

提示：
* S的长度在[1, 500]之间。
* S只包含小写字母 'a' 到 'z' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-labels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 贪心
        # 统计每个字符首次和最终出现的位置，作为一个区间
        # 因为任意字母区间要属于划分后的任一区间内，因此所有区间求并，得到的结果区间即为划分方式

        # 统计字母出现位置的区间 -> charSEIdxs
        charSEIdxs = {}  # {字符: [第一次出现的下标, 最后一次出现的下标]}
        for i, c in enumerate(s):
            if c in charSEIdxs:
                charSEIdxs[c][1] = i
            else:
                charSEIdxs[c] = [i, i]
        # 求并
        result = []
        seIdxs = sorted(charSEIdxs.values(), key=lambda x: x[0])
        curSVal = curEVal = 0
        for seIdx in seIdxs:
            if seIdx[0] <= curEVal:
                curEVal = max(curEVal, seIdx[1])
            else:
                result.append(curEVal - curSVal + 1)
                curSVal, curEVal = seIdx[0], seIdx[1]
        result.append(curEVal - curSVal + 1)
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.partitionLabels('ababcbacadefegdehijhklij')
    print(r)
