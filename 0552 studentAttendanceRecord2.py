"""
学生出勤记录 II

可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
* 'A'：Absent，缺勤
* 'L'：Late，迟到
* 'P'：Present，到场
如果学生能够同时满足下面两个条件，则可以获得出勤奖励：
* 按总出勤计，学生缺勤（'A'）严格少于两天。
* 学生不会存在连续 3 天或连续 3 天以上的迟到（'L'）记录。
给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况数量。
答案可能很大，所以返回对 10^9 + 7 取余的结果。

示例 1：
输入：n = 2
输出：8
解释：
有 8 种长度为 2 的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。

示例 2：
输入：n = 1
输出：3

示例 3：
输入：n = 10101
输出：183236316

提示：
* 1 <= n <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/student-attendance-record-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：动态规划
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        # 动态规划，长度为n的结果可由n-1的结果推算而来
        # 命名方式：第一个数字为缺勤次数，第二个数字为连续n次迟到结尾
        r00 = r01 = r10 = 1
        r02 = r11 = r12 = 0
        for i in range(n - 1):
            nr00 = (r00 + r01 + r02) % 1000000007
            nr01 = r00
            nr02 = r01
            nr10 = (r00 + r01 + r02 + r10 + r11 + r12) % 1000000007
            nr11 = r10
            nr12 = r11
            r00, r01, r02, r10, r11, r12 = nr00, nr01, nr02, nr10, nr11, nr12
        return (r00 + r01 + r02 + r10 + r11 + r12) % 1000000007


if __name__ == '__main__':
    s = Solution()

    r = s.checkRecord(2)
    print(r)

    r = s.checkRecord(1)
    print(r)

    r = s.checkRecord(10101)
    print(r)
