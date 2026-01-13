students = []
range_1 = int(input("No of students  :"))

for i in range(range_1):
    name = input("name:")
    english = int(input("english marks:"))
    maths = int(input("maths marks:"))
    science = int(input("science marks:"))

    students.append({
        "name": name,
        "english": english,
        "maths": maths,
        "science": science
    })

def grade(marks):
    if marks >= 95:
       return"S"
    elif marks >= 90:
       return"A"
    elif marks >= 80:
        return"B"
    elif marks >= 45:
        return"C"
    else:
        return"U"
    

for student in students:
    print(f"\nReport for {student['name']}:")
    for subject in ["english","maths","science"]:
        print(f"  {subject.capitalize()} Grade:{grade(student[subject])}")
    total = student["english"] + student["maths"] + student["science"]
    print(f" total: {total}, percentage: {total/3:.2f}%")

 

