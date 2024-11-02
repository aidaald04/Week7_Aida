student1 = {
    'name': 'Adam',
    'assignment': [82, 56, 44, 30],
    'test': [78, 77],
    'lab': [78.2, 77.2]
}
student2 = {
    'name': 'Kevin',
    'assignment': [82, 30],
    'test': [],
    'lab': [78.2]
}
submission_rate = {
    'Adam': 6,
    'Kevin': 3
}

if submission_rate['Adam'] < 4:
    student1['final_grade'] = 0
else:
    avg_assignment1 = sum(student1['assignment']) / len(student1['assignment']) if student1['assignment'] else 0
    avg_lab1 = sum(student1['lab']) / len(student1['lab']) if student1['lab'] else 0
    avg_test1 = sum(student1['test']) / len(student1['test']) if student1['test'] else 0
    student1['final_grade'] = (0.3 * avg_assignment1) + (0.5 * avg_lab1) + (0.2 * avg_test1)

if submission_rate['Kevin'] < 4:
    student2['final_grade'] = 0
else:
    avg_assignment2 = sum(student2['assignment']) / len(student2['assignment']) if student2['assignment'] else 0
    avg_lab2 = sum(student2['lab']) / len(student2['lab']) if student2['lab'] else 0
    avg_test2 = sum(student2['test']) / len(student2['test']) if student2['test'] else 0
    student2['final_grade'] = (0.3 * avg_assignment2) + (0.5 * avg_lab2) + (0.2 * avg_test2)
print(student1)
print(student2)

