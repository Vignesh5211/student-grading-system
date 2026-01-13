students = []
range_1 = 0

while True:
   try:
       range_1 = int(input("No of students:"))
       if range_1 <=0:
           print("Enter a positive number.")
           continue
       break
except ValueError:
      print("Invalid Number . Try again.")

for i in range(range_1):
    print(f"\nStudent {i+1}:")
    name = input("Name: ")


    def safe_int(prompt):
        while True:
            try:
                val = int(input(prompt))
                if 0 <= val <= 100:
                      return val
                else:
                    print("Enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

           
      english = safe_int("English marks: ")
      maths = safe_int("Maths marks: ")
      science = safe_int("Science marks: ")


      students.append({
        "name": name,
        "english": english,
        "maths": maths,
        "science": science
    })

    print("\nData entry complete.")



