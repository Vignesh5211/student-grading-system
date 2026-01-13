import csv

def grade(marks):
  if marks >= 95:
      return "S"
  elif marks >= 90:
       return "A"
  elif marks >=80:
       return "B"
  elif marks >=45:
       return "C"
  else:
       return "U"

  rows = []
  for s in students:
      total = s["english"] + s["maths"] +s["science"]
       percentage = total/3
    rows.append({ "name": s["name"], 
                 "english": s["english"], 
                 "maths": s["maths"],
                 "science": s["science"], 
                 "grade_english": grade(s["english"]), 
                 "grade_maths": grade(s["maths"]), 
                 "grade_science": grade(s["science"]),
                 "total": total, "percentage": f"{percentage:.2f}" }) 
# Write to CSV 
with open("student_reports.csv", "w", newline="") as f: 
  writer = csv.DictWriter(f, fieldnames=rows[0].keys())
writer.writeheader() 
writer.writerows(rows) 
print("\nSaved to student_reports.csv")

#read student from csv
import csv

student = []
with open("student_input.csv","r") as f:
  reader = csv.DictReader(f)
   for row in reader:
     student.append({
                "name": row["name"],
                 "english":int(row["english"]),
                  "maths":int(row["maths"]),
                  "science":int(row["science"])
               })
print(f"Loaded {len(student)} students from CSV.")
