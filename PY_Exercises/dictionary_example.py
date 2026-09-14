student = {
    "name": "John Doe",
    "age": 20,              
    "major": "Computer Science",
    "courses": ["CS101", "CS102", "CS103"],
    "gradesInside": {
        "CS101": "A",
        "CS102": "B",
        "CS103": "A"
    }
}
grades = student["gradesInside"]
def average_grade(grades):
    total = 0
    for grade in grades.values():
        if grade == "A":
            total += 4
        elif grade == "B":
            total += 3
        elif grade == "C":
            total += 2
        elif grade == "D":
            total += 1
    return total / len(grades)


           