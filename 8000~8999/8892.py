# 팰린드롬은 어느 방향으로 읽어도 항상 같은 방법으로 읽을 수 있는 단어이다. 예를 들어, civic, radar, rotor, madam은 팰린드롬이다.
#
# 상근이는 단어 k개 적혀있는 공책을 발견했다. 공책의 단어는 ICPC 문제가 저장되어 있는 서버에 접속할 수 있는 비밀번호에 대한 힌트이다. 비밀번호는 k개의 단어 중에서 두 단어를 합쳐야 되고, 팰린드롬이어야 한다. 예를 들어, 단어가 aaba, ba, ababa, bbaa, baaba일 때, ababa와 ba를 합치면 팰린드롬 abababa를 찾을 수 있다.
#
# 단어 k개 주어졌을 때, 팰린드롬을 찾는 프로그램을 작성하시오.

from itertools import combinations
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

T = int(input())
for _ in range(T):
    k = int(input())
    palindrome_li = []
    li = []
    for _ in range(k):
        string = input()
        li.append(string)
    combine_list = combinations(li, 2)
    for a, b in combine_list:
        combine_string1 = a + b
        combine_string2 = b + a
        if palindrome(combine_string1):
            palindrome_li.append(combine_string1)
        if palindrome(combine_string2):
            palindrome_li.append(combine_string2)
    if palindrome_li == []:
        print(0)
    else:
        print(palindrome_li[0])