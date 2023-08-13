# 창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.
#
# 삼각형의 세 각을 입력받은 다음,
#
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.

angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())

if angle_1 == 60 and angle_2 == 60 and angle_3 == 60:
    print("Equilateral")
elif angle_1 + angle_2 + angle_3 == 180 and ((angle_1 == angle_2) or (angle_1 == angle_3) or (angle_2 == angle_3)):
    print("Isosceles")
elif angle_1 + angle_2 + angle_3 == 180 and angle_1 != angle_2 != angle_3:
    print("Scalene")
elif angle_1 + angle_2 + angle_3 != 180:
    print("Error")