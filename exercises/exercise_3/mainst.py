from student import Student

if __name__ == "__main__":
    print(Student.count)
    student = Student(name="John Doe", age = 23, matric_num = 12345)
    print(student)
    print(student.get_age())
    student.set_age(age=24)
    print(student.get_age())
    print(student._Student__secret)
    print(student.greet())
    Student.add_student(name="anna", age="10", matric_num="54321")
