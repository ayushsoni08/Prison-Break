def main():
    score = int(input("Score: "))
    grade = getGrade(score)
    print(f"Grade {grade}")


def getGrade(score):
    # if score >= 90 and score <= 100:
    #     grade = "A"
    # elif score >= 80 and score < 90:
    #     grade = "B"
    # elif score >= 70 and score < 80:
    #     grade = "C"
    # elif score >= 60 and score < 70:
    #     grade = "D"
    # else:
    #     grade = "F"

    #small question
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    else:
        grade = "F"

    #better
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade

main()