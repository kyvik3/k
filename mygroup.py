groupmates = [
	{
		"name": "Максим",
		"surname": "Кравец",
		"exams": ["Информатика", "Физика", "Web"],
		"marks": [5, 5, 5]
	},
	{
		"name": "Дмитрий",
		"surname": "Титов",
		"exams": ["Физика", "Web", "КТП"],
		"marks": [5, 3, 4]
	},
	{
		"name": "Кирилл",
		"surname": "Cорокин",
		"exams": ["Философия", "ИС", "КТП"],
		"marks": [5, 4, 5]
	},
	{
		"name": "Тимур",
		"surname": "Дзариев",
		"exams": ["Философия", "ИС", "КТП"],
		"marks": [2, 3, 2]
	},
	{
		"name": "Дарья",
		"surname": "Вязовова",
		"exams": ["3d", "ИС", "Web"],
		"marks": [5, 4, 3]
	},
	{
		"name": "Анастасия",
		"surname": "Алпатова",
		"exams": ["Философия", "ИС", "КТП"],
		"marks": [5, 5, 5]
	},
]

def count_mark(students,mark):
    print ("surname".ljust(15), "marks".ljust(20))
    for student in students:
        marks_list = student["marks"]
        result = (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["surname"].ljust(15), str(student["marks"]).ljust(20))
need = int(input('Input :'))
count_mark(groupmates,need)
