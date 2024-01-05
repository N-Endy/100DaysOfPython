class Course():
    def __init__(self, courseCode, courseUnit, score):
        self.course_code = courseCode
        self.course_unit = courseUnit
        self.score = score
        self.quality_point = 0.0
        self.grade_point = 0
        self.grade = ""
        self.calculate_grade()
        
    def calculate_grade(self):
        
        if self.score >= 70 and self.score <= 100:
            self.grade = "A"
            self.grade_point = 5.0
        elif self.score >= 60 and self.score <= 69:
            self.grade = "B"
            self.grade_point = 4.0
        elif self.score >= 50 and self.score <= 59:
            self.grade = "C"
            self.grade_point = 3.0
        elif self.score >= 45 and self.score <= 49:
            self.grade = "D"
            self.grade_point = 2.0
        elif self.score >= 40 and self.score <= 44:
            self.grade = "E"
            self.grade_point = 1.0
        elif self.score < 40 and self.score >= 0:
            self.grade = "F"
            self.grade_point = 0.0
        self.quality_point = self.course_unit * self.grade_point