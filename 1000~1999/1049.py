# Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다. 따라서 새로운 줄을 사거나 교체해야 한다. 강토는 되도록이면 돈을 적게 쓰려고 한다. 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
#
# 끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때, 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.

N, M = map(int, input().split())
li = []
for _ in range(M):
    package_price, single_price = map(int, input().split())
    li.append([package_price, single_price])

package_li = sorted(li, key = lambda x : x[0])
single_li = sorted(li, key = lambda x : x[1])

result = []
if N % 6 == 0:
    # 패키지로 사는 가격보다 낱개롤 사는 가격이 저렴할 때
    if package_li[0][0] * (N // 6) > single_li[0][1] * N:
        result.append(single_li[0][1] * N)
    else:
        result.append(package_li[0][0] * (N // 6))
else:
    if package_li[0][0] * ((N // 6) + 1) > single_li[0][1] * N:
        result.append(single_li[0][1] * N)
    else:
        result.append(package_li[0][0] * ((N // 6) + 1))
    result.append(package_li[0][0] * (N // 6) + single_li[0][1] * (N % 6))
print(min(result))