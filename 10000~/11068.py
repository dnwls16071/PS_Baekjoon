# 어떤 수를 왼쪽부터 읽어도, 오른쪽부터 읽어도 같을 때 이 수를 회문인 수라고 한다. 예를 들어, 747은 회문인 수이다. 255도 회문인 수인데, 16진수로 표현하면 FF이기 때문이다. 양의 정수를 입력받았을 때, 이 수가 어떤 B진법 (2 ≤ B ≤ 64)으로 표현하면 회문이 되는 경우가 있는지 알려주는 프로그램을 작성하시오. B진법이란, 한 자리에서 수를 표현할 때 쓸 수 있는 수의 가짓수가 B라는 뜻이다. 예를 들어, 십진법에서 B는 10이다.

T = int(input())
for _ in range(T):
    number = int(input())
    ans = []
    for B in range(2, 65):
        lst = []
        temp = number
        while True:
            if temp == 0:
                break
            else:
                lst.append(temp % B)
                temp //= B
        for i in range(len(lst)//2):
            if lst[i] != lst[-1-i]:
                ans.append("X")
                break
    if len(ans) == 63:
        print(0)
    else:
        print(1)