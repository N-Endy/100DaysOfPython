from courses import Course
import sys


print("Press (1) for GPA calculation")
print("Press (0) to end process")


user_input = input("Select an action to perform: ")
# while user_input != 1 and user_input != 0:
#     user_input = input("Select an action to perform: ")
    

if user_input == "1":
    number_of_courses = int(input("How many courses would you like to enter: "))
    
    while number_of_courses <= 0:
        print("Invalid input. Please enter a positive integer for Number of Courses.")
        number_of_courses = int(input("How many courses would you like to enter: "))
        
    courses = []

    for i in range(0, number_of_courses):
        
        # Input course code
        print(f"Entry number: {i + 1}")
        course_code = input("Enter course code e.g Math-101: ")
        
        # Input course unit
        course_unit = int(input("Enter course unit. Range 1 - 5: "))
        while course_unit < 1 or course_unit > 5:
            print("Invalid input. Please enter a positive integer for Course Unit.")
            course_unit = int(input("Enter course unit. Range 1 - 5: "))
            
        # Input score
        score = int(input("Enter Score. Range 0 - 100: "))
        while score < 0 or score > 100:
            print("Invalid input. Please enter a score between 0 and 100.")
            score = int(input("Enter Score. Range 0 - 100: "))
            
        # Initialize new course and add to list
        courses.append(Course(course_code, course_unit, score))
        
    # Display details for eac course in array
    print("\nCourse Details:")
    # Header
    header = "{:<15} | {:<12} | {:<5} | {:<5} | {:<12} | {:<15}".format(
    "Course Code", "Course Unit", "Score", "Grade", "Grade Point", "Quality Point")
    print(header)

    # Separator line
    separator_line = "-" * 80
    print(separator_line)
    
    # Calculate GPA
    total_course_units = 0
    total_quality_points = 0
    gpa = 0.0
    
    for course in courses:
        total_course_units += course.course_unit
        total_quality_points += course.quality_point
        
        gpa = total_quality_points / total_course_units
        
        # Header
        header = "{:<15} | {:<12} | {:<5} | {:<5} | {:<12} | {:<15}".format(
        course.course_code, course.course_unit, course.score, course.grade, course.grade_point, course.quality_point)
        print(header)

        # Separator line
        separator_line = "-" * 80
        print(separator_line)
        
        
    print(f"Your GPA is: {gpa}")
    print("GPA is calculated using the formula:")
    print("(Total Quality Points) / (Total Course Units)")
    print("\n")
elif user_input == "0":
    sys.exit(0)
