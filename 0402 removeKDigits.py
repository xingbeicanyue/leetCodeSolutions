"""
移掉K位数字

给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:
num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。

示例 1 :
输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。

示例 2 :
输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。

示例 3 :
输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-k-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、贪心算法
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        # 将数字依次加入队列中，如果队列非递增，则先移除队列尾部的数再加入（保证队列递增）
        digits = []
        for d in num:
            while digits and k > 0 and d < digits[-1]:
                digits.pop()
                k -= 1
            digits.append(d)
        # digits已是单调递增序列（非严格），若移除的数字还未满额，则移除最后几位
        return ''.join([str(digits[i]) for i in range(len(digits) - k)]).lstrip('0') or '0'


if __name__ == '__main__':
    s = Solution()
    r = s.removeKdigits('1432219', 3)
    print(r)
    r = s.removeKdigits('10200', 1)
    print(r)
    r = s.removeKdigits('10', 2)
    print(r)
