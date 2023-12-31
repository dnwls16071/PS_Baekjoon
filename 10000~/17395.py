# 당신에게 자연수 x0와 N이 주어졌다. 지금부터 당신은 이 자연수 x0를 N번의 '변환'을 통해 0으로 바꿀 것이다. 변환이란, 양의 정수를 이진법으로 표기하여, 1개 이상의 1을 0으로 바꾸는 작업이다. 예를 들어 9를 이진법으로 나타내면 1001(2)인데, 9는 0(0000(2)), 1(0001(2)), 또는 8(1000(2))로 변환될 수 있다. 바뀐 자릿수는 밑줄로 표기되었다. 여러분의 목표는 xi를 변환하여 xi+1를 만드는 과정을 반복해, xN을 0으로 만드는 것이다.
#
# 위 조건을 만족하는 수열 X = x0, x1, x2, ..., xN는 존재하지 않을 수도 있지만, 여러 개가 존재할 수도 있다. 만약 존재한다면, 각 수열별로 인접한 원소들의 차들의 집합 D(X) = {x0-x1, x1-x2, ..., xN-1-xN}를 정의하자. 이 집합의 원소들의 최대값과 최소값의 차이를 최소화하도록, 수열 X를 만들고자 한다. 즉, 가능한 모든 수열 Xi 중 (D(Xi)에 속한 원소의 최댓값 - D(Xi)에 속한 원소의 최솟값)이 최소가 되는 Xi를 찾고자 한다.
#
# 이상해보일 수 있는 문제지만, 당신은 대답해야 한다. 과연 1초안에 답할 수 있을까?

