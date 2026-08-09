scores = {"math": 88, "science": 91, "art": 75, "pe": 95}

def average_scores(scores):
    total = 0
    for subject, score in scores.items():
        total += score
    return total / len(scores)

result = average_scores(scores)
print(result)

scores = {"math": 88, "science": 91, "art": 75, "pe": 95}

def highest_score(scores):
    highest = 0
    highest_subject = None
    for subject, score in scores.items():
        if score > highest:
            highest = score
            highest_subject = subject
    return highest_subject

result = highest_score(scores)
print(result)
