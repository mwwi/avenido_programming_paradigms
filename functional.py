def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)

def find_highest_grade(grades):
    return max(grades)

def find_lowest_grade(grades):
    return min(grades)

def count_above_threshold(grades, threshold):
    count = sum(1 for grade in grades if grade > threshold)
    return count

def main():
    # Allowing user to input grades
    grades = []
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        grade = float(input(f"Enter grade for student {i+1}: "))
        grades.append(grade)

    # Calculate average grade
    average_grade = calculate_average(grades)
    print("Average grade:", average_grade)

    # Find highest grade
    highest_grade = find_highest_grade(grades)
    print("Highest grade:", highest_grade)

    # Find lowest grade
    lowest_grade = find_lowest_grade(grades)
    print("Lowest grade:", lowest_grade)

    # Count number of students with grades above a certain threshold
    threshold = float(input("Enter the threshold grade: "))
    count_above_threshold_value = count_above_threshold(grades, threshold)
    print("Number of students with grades above", threshold, ":", count_above_threshold_value)

if __name__ == "__main__":
    main()
