# 회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다. 예를 들어 ‘abba’ ‘kayak’, ‘reviver’, ‘madam’은 모두 회문이다. 만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 “유사회문”(pseudo palindrome)이라고 부른다. 예를 들어 ‘summuus’는 5번째나 혹은 6번째 문자 ‘u’를 제거하여 ‘summus’인 회문이 되므로 유사회문이다.
#
# 여러분은 제시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다. 만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다.

import sys
input = sys.stdin.readline

def function(String, left, right):
    while True:
        if left > right:
            break
        if String[left] == String[right]:
            left += 1
            right -= 1
        else:
            temp1 = String[left:right]
            temp2 = String[left+1:right+1]
            if (temp1 == temp1[::-1]) or (temp2 == temp2[::-1]):
                return 1
            else:
                return 2
    return 0


T = int(input())
for _ in range(T):
    String = input().strip()
    left = 0
    right = len(String) - 1
    print(function(String, left, right))