grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # Список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #   Множество
sorted_students = sorted(students) # Сортировка учеников по алфавиту
average_grades = {} # Создание словаря . Способ 1. Использование цикла For - in
for student, grade_list in zip(sorted_students, grades):
    average_grades[student] = sum(grade_list) / len(grade_list)
print(average_grades)

def calculate_average(student_grade): # Способ 2. Использование функции def - return
    student_name, grade_list = student_grade
    return (student_name, sum(grade_list) / len(grade_list))

# Создаем словарь с помощью zip и dict
average_grades = dict(map(calculate_average, zip(sorted_students, grades)))
print(average_grades)


t = 'input'
print(t[10])