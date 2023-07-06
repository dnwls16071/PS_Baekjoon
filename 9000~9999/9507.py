# 꿍은 군대에서 진짜 할짓이 없다. 그래서 꿍만의 피보나치를 만들어보려고 한다. 기존의 피보나치는 너무 단순해서 꿍은 좀더 복잡한 피보나치를 만들어보고자 한다. 그래서 다음과 같은 피보나치를 만들었다. 꿍만의 피보나치 함수가 koong(n)이라고 할 때,

fibonacci = [1, 1, 2, 4]
for i in range(4, 68):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2] + fibonacci[i-3] + fibonacci[i-4])

T = int(input())
for _ in range(T):
    print(fibonacci[int(input())])