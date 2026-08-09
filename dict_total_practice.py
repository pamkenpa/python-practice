scores = {"math": 88, "science": 91, "art": 75, "pe": 95}

def average_scores(scores):
    total = 0
    for subject, score in scores.items():
        total += score
    return total / len(scores)

result = average_scores(scores)
print(result)