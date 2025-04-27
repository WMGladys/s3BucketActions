import csv

def analyze_student_grades(csv_filepath, grade_threshold):
   
    student_grades = {}

    try:
        with open(csv_filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  

            for row in reader:
                if len(row) == 3:
                    name, age_str, grade_str = row
                    try:
                        age = int(age_str)
                        grade = float(grade_str)
                        if name in student_grades:
                            student_grades[name]['total_grade'] += grade
                            student_grades[name]['count'] += 1
                        else:
                            student_grades[name] = {'total_grade': grade, 'count': 1}
                    except ValueError:
                        print(f"Warning: Skipping invalid data in row: {row}")
                else:
                    print(f"Warning: Skipping row with incorrect number of columns: {row}")

        print(f"\nStudents with an average grade above {grade_threshold}:")
        found_students = False
        for name, data in student_grades.items():
            average_grade = data['total_grade'] / data['count']
            if average_grade > grade_threshold:
                print(f"- {name}: Average Grade = {average_grade:.2f}")
                found_students = True

        if not found_students:
            print("No students found above the specified threshold.")

    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    csv_file = 'students.csv'  

    threshold = 80.0  

    analyze_student_grades(csv_file, threshold)
