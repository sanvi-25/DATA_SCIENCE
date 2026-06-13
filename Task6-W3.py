import numpy as np

def top_risky_users(transactions, k):
    normalized = (transactions - np.min(transactions, axis=0)) / (np.max(transactions, axis=0) - np.min(transactions, axis=0))
    risk_score = []

    for row in normalized:
        score = 0.6 * row[0] + 0.3 * row[1] + 0.1 * row[2]
        risk_score.append(score)

    result = []
    for _ in range(k):
        max_index = risk_score.index(max(risk_score))
        result.append(max_index)
        risk_score[max_index] = -1

    return result


r = int(input("Enter number of users: "))

transactions = []

for i in range(r):
    row = list(map(float, input(f"Enter Amount, TimeSpent, FailedAttempts for user {i}: ").split()))
    transactions.append(row)

transactions = np.array(transactions)

k = int(input("Enter k: "))

print(top_risky_users(transactions, k))