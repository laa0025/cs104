import csv
import sys

weights = {"Quiz": 0.10, "Lab": 0.30, "Test1": 0.15, "Test2": 0.15,
           "Project": 0.20, "Final": 0.10}


def compute_grade(grades):
    total = 0
    for category in weights:
        total += grades[category] * weights[category]
    return total


def score_to_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def main():
    if len(sys.argv) != 2:
        print("Usage: python lab5.py grade.csv")
        return

    student_grades = {}
    try:
        with open(sys.argv[1], newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, skipinitialspace=True)
            for row in reader:
                name = row["Name"].strip()
                student_grades[name] = {}
                for category in weights:
                    student_grades[name][category] = float(row[category])
    except (OSError, KeyError, ValueError) as error:
        print("Could not read the grades file:", error)
        return

    if not student_grades:
        print("No student grades found.")
        return

    lines = ["-" * 60,
             f'{"Student Name":<20}{"Final Score":>15}{"Grade":>10}',
             "-" * 60]

    for name, grades in student_grades.items():
        grades["final_score"] = compute_grade(grades)
        grades["grade"] = score_to_letter(grades["final_score"])
        lines.append(f'{name:<20}{grades["final_score"]:>15.2f}{grades["grade"]:>10}')

    lines.append("-" * 60)
    count = len(student_grades)
    lines.append(f"Number of students in class: {count}")

    category_names = {"Quiz": "quiz", "Lab": "lab", "Test1": "test1",
                      "Test2": "test2", "Project": "Capstone Project",
                      "Final": "final exam"}

    for category in weights:
        average = sum(grades[category] for grades in student_grades.values()) / count
        lines.append(f"Class average of {category_names[category]}: {average:.2f} {score_to_letter(average)}")

    class_average = sum(grades["final_score"] for grades in student_grades.values()) / count
    lines.append(f"Class average grade: {class_average:.2f} {score_to_letter(class_average)}")

    report = "\n".join(lines)
    print(report)
    with open("grade_report.txt", "w", encoding="utf-8") as file:
        file.write(report + "\n")
    print("\nReport saved to grade_report.txt")


if __name__ == "__main__":
    main()
