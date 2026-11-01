
def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


marks = [85, 90, 80]

average = calculate_average(marks)
grade = calculate_grade(average)

print("Average Marks:", average)
print("Grade:", grade)
