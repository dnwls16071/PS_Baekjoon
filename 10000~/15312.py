# '이름 궁합'이란 두 사람의 이름을 한 글자씩 번갈아 써 놓고 획수를 그 아래에 적은 뒤, 인접한 숫자끼리 더한 일의 자리 값을 아래에 적어 나가면서 마지막에 남은 두 숫자를 보고 궁합이 맞는 정도를 알아보는 일종의 점이다.
#
# 아직도 '그녀'를 잊지 못한 로맨티스트 종민이는 어느 날 그녀와 이름 궁합을 한 번 해 보기로 했는데, 그 결과는 충격적이었다.
#
#
#
# 이 결과를 도저히 받아들일 수 없었던 종민이는 이것이 틀렸음을 증명하기 위해 열심히 머리를 굴렸고, 다음과 같은 변명거리를 생각해 냈다.
#
# "'그녀'는 한국인이 아니니까 한글로 이름 궁합을 보면 결과가 이상한 것이 당연하지! 세계 공용어인 영어 알파벳으로 이름을 쓰면 결과가 정확하게 나올 거야!"
#
# 그래서 종민이는 알파벳 대문자로 이름을 써 놓고 이름 궁합을 보려고 한다. 그런데, 종민이는 손으로 계산을 하면 실수를 할까 두려워 당신에게 프로그램을 짜 달라고 부탁했다. 종민이를 도와주자! 종민이가 정한 알파벳 대문자의 획수는 힌트를 참고하자.
alphabet = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1, 'M': 2,
            'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}
A = input()
B = input()

li = []
for i in range(len(A)):
    li.append(A[i])
    li.append(B[i])

result = []
for i in range(1, len(li)):
    result.append((alphabet[li[i]] + alphabet[li[i - 1]]) % 10)

temp = []
while True:
    if len(result) == 2:
        break
    for i in range(1, len(result)):
        temp.append((result[i] + result[i - 1]) % 10)
    result = temp
    temp = []

score = ""
for i in result:
    score += str(i)

value = ""
if score[0] == "0":
    value = score[0] + score[1]
    print(value)
else:
    print(int(score))