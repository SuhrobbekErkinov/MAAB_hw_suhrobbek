import csv
from collections import defaultdict

def create_grades_file():
    grades_data = [
        ["Name", "Subject", "Grade"],
        ["Alice", "Math", 85],
        ["Bob", "Science", 78],
        ["Carol", "Math", 92],
        ["Dave", "History", 74]
    ]
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(grades_data)

def read_grades():
    grades = []
    with open("grades.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Grade"] = int(row["Grade"])  # Convert grade to integer
            grades.append(row)
    return grades

def calculate_average_grades(grades):
    subject_grades = defaultdict(list)
    for entry in grades:
        subject_grades[entry["Subject"]].append(entry["Grade"])
    return {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

def write_average_grades(average_grades):
    with open("average_grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg_grade in average_grades.items():
            writer.writerow([subject, round(avg_grade, 2)])

def main():
    create_grades_file()
    grades = read_grades()
    average_grades = calculate_average_grades(grades)
    write_average_grades(average_grades)
    print("Average grades have been calculated and saved to average_grades.csv.")

if __name__ == "__main__":
    main()
