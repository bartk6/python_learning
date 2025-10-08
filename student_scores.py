# Adding something for git to detect
name_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
}

def grade_check(name,score, ):
    if isinstance(score, int):

        if score >= 90:
            print(f"{name}'s grade: A")
        elif score >= 80:
            print(f"{name}'s grade: B")
        elif score >= 70:
            print(f"{name}'s grade: C")
        elif score >= 60:
            print(f"{name}'s grade: D")
        else:
            print(f"{name}'s grade: F")
    else:
        print(f"{name}'s score is invalid")
for name, score in name_scores.items():
    grade_check(name, score)
