# 어제, 지민이는 몰래 리조트에 갔다가 입구에 걸려있는 복권 광고를 하나 보았다.
#
# “1부터 N까지의 수 중에 서로 다른 M개의 수를 골라보세요. 저희도 1부터 N까지의 수 중에 서로 다른 M개의 수를 고를건데, 적어도 K개의 수가 같으면 당첨입니다.!”
#
# 지민이는 돌아오면서 자신이 복권에 당첨될 확률이 궁금해졌다.
#
# 지민이가 복권에 당첨될 확률을 구하는 프로그램을 작성하시오.

from itertools import combinations

def calculate_probability(n, m, k):
    # Generate all possible combinations of M numbers from 1 to N
    all_combinations = list(combinations(range(1, n+1), m))

    # Initialize a counter for the number of winning combinations
    num_winning_combinations = 0

    # Check each pair of combinations for at least K matching numbers
    for i in range(len(all_combinations)):
        for j in range(i+1, len(all_combinations)):
            matching_numbers = set(all_combinations[i]).intersection(set(all_combinations[j]))
            if len(matching_numbers) >= k:
                num_winning_combinations += 1

    # Calculate the probability of winning
    total_combinations = len(all_combinations)
    probability = num_winning_combinations / (total_combinations * (total_combinations-1) / 2)

    return probability

# Example usage:
N, M, K = map(int, input().strip().split())
probability = calculate_probability(N, M, K)
print(probability)