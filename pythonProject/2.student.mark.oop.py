class Student:
    def __init__ (self, stID, stname, DoB, mark): #stname = student name
        self.stID = stID
        self.stname = stname
        self.DoB = DoB
        self.mark = mark

    def get_studentID (self):
        print("StudentId:", self.stID)

    def get_stname (self):
        print("Student name:", self.stname)

    def get_DoB (self):
        print("DoB:", self.DoB)

    def set_mark(self, mark):
        self.mark = mark

    def get_mark(self):
        # st_ID = input("Student Id:")
        cs_ID = input("Course Id:")
        print("Mark:", self.mark)

class Course:
    def __init__ (self,courseID, csname): #cs name = course name
        self.csID = courseID
        self.csname = csname

    def get_courseID(self):
        return self.courseID

    def get_csname(self):
        return self.csname

class Class (Student, Course):
    def __init__ (self,num_st, num_cs):
        self.__num_st = num_st
        self.__num_cs = num_cs.student.mark.oop.math.py

    def get_num_st (self):
        return self.num_st

    def get_num_cs (self):
        return self.num_cs

a = Student("BI12-024", "VA", "4/10/2003", 10)
a.get_studentID()
a.get_stname()
a.get_DoB()
a.get_mark()

