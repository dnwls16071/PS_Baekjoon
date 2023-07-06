# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
#
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

N = int(input())
lst = []
for i in range(N):
    word = input()
    lst.append(word)

lst = list(set(lst))
lst.sort(key=lambda x : (len(x), x))
for i in lst:
    print(i)