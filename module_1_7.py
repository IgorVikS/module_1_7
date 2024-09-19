grades = [[5, 3, 4, 5, 4], [2, 2, 3, 2, 3], [4, 5, 4, 5, 2], [4, 4, 3, 4], [5, 5, 5, 4, 5], [3, 5, 3,4]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron', 'Fredy'}
def get_aver_grade(students: set, grades: list) -> dict:
    grades_of_students = {}
    students = sorted(students)
    for i in range(len(students)):
         grades_of_students[students[i]] = sum(grades[i]) / len(grades[i])
    return grades_of_students
res = get_aver_grade(students, grades)
print(res)