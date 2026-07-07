# Question 7 - Student Class

class student:

    def __init__(self, name, matric_number, department, level, cgpa):
        self.name = name
        self.matric_number = matric_number
        self.department = department
        self.level = level
        self.cgpa = cgpa

    def calculate_class(self):
        if self.cgpa >= 4.50:
            return "First Class"
        elif self.cgpa >= 3.50:
            return "Second Class Upper"
        elif self.cgpa >= 2.40:
            return "Second Class Lower"
        elif self.cgpa >= 1.50:
            return "Third Class"
        else:
                return "Pass"

    def display_information(self):
        print("Name:", self.name)
        print("Matric_Number:", self.matric_number)
        print("Department:", self.department)
        print("Level:", self.level)
        print("CGPA:", self.cgpa)
        print("Class:", self.calculate_class())
        print("_" *30)

student1 = student("John", "DTS001", "Data Science", "200", 4.80)
student2 = student("Mary", "DTS002", "Data Science", "200", 3.90)
student3 = student("David", "DTS003", "Data Science", "200", 3.00)
student4 = student("Grace", "DTS004", "Data Science", "200", 2.00)
student5 = student("Peter", "DTS005", "Data Science", "200", 1.20)

student1.display_information()
student2.display_information()
student3.display_information()
student4.display_information()
student5.display_information()
