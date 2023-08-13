# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

lst = ['a','e','i','o','u','A','E','I','O','U']

while True:
    sentence = input().strip()
    if sentence == "#":
        break
    answer = 0
    for i in sentence:
        if i in lst:
            answer += 1
    print(answer)