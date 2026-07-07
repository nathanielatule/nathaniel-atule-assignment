# class student

class student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 70:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 50:
            return "C"
        elif self.marks >= 45:
            return "D"
        elif self.marks >= 40:
            return "E"
        else:
            return "F"

student1 = student("John", "DS001", 85)

print("Name:", student1.name)
print("Roll Number:", student1.roll_number)
print("Marks:", student1.marks)
print("Grade:", student1.calculate_grade())
