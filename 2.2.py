student = {
    'name': 'Adam',
    'assignment': [82, 56, 44, 30],
    'lab': [78.2, 77.2],
    'test': [78, 77]
}
subm_check = {}
submitted_active = len(student['assignment']) + len(student['test']) + len(student['lab'])
subm_check[student['name']] = submitted_active
print(subm_check)
