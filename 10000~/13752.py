# 히스토그램은 데이터를 시각적으로 표현한 것이다. 막대로 구성되며 각 막대의 길이는 데이터 양의 크기를 나타낸다. 일부 데이터가 주어지면 히스토그램을 생성하시오.

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

for i in lst:
    print("=" * i)