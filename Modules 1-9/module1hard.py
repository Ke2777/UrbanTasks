grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = (list(students))
list_students.sort()
result = {}

for i in range(len(list_students)):
    current_grade = grades[i]
    result[list_students[i]] = sum(current_grade) / len(current_grade)
    i += 1
print(result)