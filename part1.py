class Course:
    id = ""
    year = ""
    semester = ""
    teacher = ""
    
    def __init__(self, id, year, semester, teacher):
        self.id = id
        self.year = year
        self.semester = semester
        self.teacher = teacher
        
    def getTeacher(self):
        return self.teacher
        
class Teacher:
    fname = ""
    lname = ""
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
   
class Student: 
    id = ""
    fname = ""
    lname = ""
    
    grades = []
    
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname
        
    def addCourse(self, course):
        self.grades.append(Grade(self, course, "-"))
        
    def changeGrade(self, course, newGrade):
        for x in self.grades:
            if x.course == course and x.student == self:
                x.grade = newGrade
        
    def getGrade(self, course):
        for x in self.grades:
            if x.student == self and x.course == course:
                return x.grade
    
    def getGPA(self, year, semester):
        runningTotal = ""
        for x in self.grades:
            if x.student == self and x.course.year == year and x.course.semester == semester:
                runningTotal += x.grade
        return runningTotal
        
    def getGrades(self, year, semester):
        result = {}
        for x in self.grades:
            if x.student == self and x.course.year == year and x.course.semester == semester:
                result[x.course.id] = x.grade
        return result
        
    
class Grade:
    student = ""
    course = ""
    grade = ""
    
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade
 
#add some sample data 
t1 = Teacher("Rebecca", "Shrodinger")
t2 = Teacher("Mathew", "West")   
c1 = Course("MATH101", "2016", "Fall", t1)
c2 = Course("MATH102", "2016", "Fall", t2)
s1 = Student("1", "Simon", "Shulgan")
s2 = Student("2", "John", "Fellows")

#get teacher for a given course
print("print teacher for a course")
print(c1.getTeacher().fname)

#enroll students into course and change and show their grade
print("enroll a student into a course and get their grade")
s1.addCourse(c1)
s1.changeGrade(c1, "A")
print(s1.getGrade(c1))

#add more to the student s1
print("enroll the same student into a ntoher course and give them a grade, and then show GPA")
s1.addCourse(c2)
s1.changeGrade(c2,"B")
print(s1.getGrade(c2))
print(s1.getGPA("2016","Fall"))

s1Courses = s1.getGrades("2016","Fall")
print(s1Courses)



