"""
七进制数

给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

示例 1:
输入: num = 100
输出: "202"

示例 2:
输入: num = -7
输出: "-10"

提示：
* -10^7 <= num <= 10^7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/base-7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数学
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return '-' + self.convertToBase7(-num)
        chars = []
        while num >= 7:
            chars.append(str(num % 7))
            num //= 7
        chars.append(str(num))
        return ''.join(reversed(chars))


if __name__ == '__main__':
    s = Solution()

    r = s.convertToBase7(100)
    print(r)

    r = s.convertToBase7(-7)
    print(r)
