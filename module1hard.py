grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = (list(students))
list_students.sort()
result = {}

for i in range(len(list_students)):
    score_sum = 0
    for a in range(len(grades[i])):
        current_grade = grades[i]
        score_sum += current_grade[a]
    result[list_students[i]] = score_sum / len(grades[i])
    i += 1
print(result)