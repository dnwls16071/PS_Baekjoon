# 올 골드 럭비 클럽의 회원들은 성인부 또는 청소년부로 분류된다.
#
# 나이가 17세보다 많거나, 몸무게가 80kg 이상이면 성인부이다. 그 밖에는 모두 청소년부이다. 클럽 회원들을 올바르게 분류하라.

while True:
    name, age, weight = map(str, input().strip().split())
    age = int(age)
    weight = int(weight)
    if name == "#" and age == 0 and weight == 0:
        break
    if age > 17 or weight >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")