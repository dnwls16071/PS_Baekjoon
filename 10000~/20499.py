# 아무래도 우리 팀 다리우스가 고수인 것 같다. 그의
# $K/D/A$를 보고 그가 「진짜」인지 판별해 보자.
#
#  
# $K+A < D$이거나,
# $D = 0$이면 그는 「가짜」이고, 그렇지 않으면 「진짜」이다.

record = list(input().strip().split("/"))

if int(record[0]) + int(record[2]) < int(record[1]) or int(record[1]) == 0:
    print("hasu")
else:
    print("gosu")