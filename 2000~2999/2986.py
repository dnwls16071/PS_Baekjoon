# 이 이야기는 고창영이 10살 때 있었던 실화이다.
#
# 창영이는 10살 때 파스칼을 독학했다. 창영이가 공부하던 책에는 다음과 같은 프로그램이 있었다.
#
# readln(N);
# counter := 0;
# for i := N-1 downto 1 do begin
#     counter := counter + 1;
#     if N mod i = 0 then break;
# end;
# writeln(counter);
# 창영이는 N을 입력했을 때, 무엇이 출력될지 궁금해졌다.
#
# 창영이가 입력한 N이 주어졌을 때, 무엇이 출력되는지 구하는 프로그램을 작성하시오.

#1
import sys
input = sys.stdin.readline

N = int(input())

i = 2
Counter = 1
while i * i <= N:
    if N % i == 0:
        Counter = N // i
        break
    i += 1
print(N-Counter)

