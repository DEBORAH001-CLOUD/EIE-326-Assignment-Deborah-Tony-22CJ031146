def get_grade_point(letter_grade):
    grade_points = {
        'A': 5.0,
        'B': 4.0,
        'C': 3.0,
        'D': 2.0,
        'F': 0.0
    }
    return grade_points.get(letter_grade.upper(), None)

def compute_gpa():
    total_points = 0
    number_courses = 6

    print("Enter the letter grades for 6 courses (A, B, C, D, F):")

    for i in range(1, number_courses + 1):
        while True:
            grade = input(f"Course {i} grade: ")
            grade_point = get_grade_point(grade)
            if grade_point is not None:
                total_points += grade_point
                break
            else:
                print("Invalid grade entered. Please enter A, B, C, D, or F.")

    gpa = total_points / number_courses
    print(f"\nThe student's GPA is: {gpa:.2f}")

compute_gpa()