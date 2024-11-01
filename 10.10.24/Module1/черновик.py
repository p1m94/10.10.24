grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # Список
print(type(grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #   Множество
sorted_students = sorted(students) # Сортировка учеников по алфавиту
students_grades = {}
for a, b in zip(sorted_students, grades):
    students_grades[a] = sum(b) / len(b)
print(students_grades)