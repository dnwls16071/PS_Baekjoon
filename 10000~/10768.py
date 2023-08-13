# 2월 18일은 올해 CCC에 있어서 특별한 날이다.
#
# 사용자로부터 정수인 월과 일을 입력받아 날짜가 2월 18일인지 전인지 후인지를 출력하는 프로그램이다.
#
# 만약 날짜가 2월 18일 전이면, "Before"을 출력한다. 만약 날짜가 2월 18일 후면, "After"을 출력한다. 만약 2월 18일이라면 "Special" 을 출력한다.

month = int(input())
day = int(input())

if month < 2 or (month == 2 and day < 18):
    print("Before")
elif month > 2 or (month == 2 and day > 18):
    print("After")
else:
    print("Special")
