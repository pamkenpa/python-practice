students = {
    "Jim": [88, 92, 79, 85],
    "Anna": [95, 91, 89, 97],
    "Leo": [60, 72, 68, 55],
    "Isa": [80, 84, 78, 82]
}

def average(scores):
    total = sum(scores)
    quantity = len(scores)
    return total / quantity 


def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "F"



def top_students(students):
    highest_avg = 0
    name = None
    for student, scores in students.items():
        avg = average(scores)
        if avg > highest_avg:
            highest_avg = avg
            name = student
    return name



def student_report(students):
    for name, scores in students.items():
        avg = average(scores)
        print(f"{name}: average {avg}, grade {letter_grade(avg)}")

def add_score(students, name, score):
    try:
        students[name].append(score)
    except KeyError:
        print("Student not found.")

add_score(students, "Jim", 90)
print(students["Jim"])

add_score(students, "Marco", 90)