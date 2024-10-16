name = str(input("Enter ypur name: "))
sec = str(input("Enter your section: "))
prelim = float(input("Enter you Preliminary Grade: "))
midterm = float(input("Enter you Midterm Grade: "))
final = float(input("Enter you final grade: "))


if prelim < 40.0 or prelim > 100.0:
    print("Error: your grade must stay between 40 and 100.")
elif midterm <40.0 or midterm > 100.0:
    print("Error: your grade must stay between 40 and 100.")
elif final < 40.0 or final > 100.0:
    print("Error: your grade must stay between 40 or 100.")
else:
    final_grade = (prelim * 0.3333) +  (midterm * 0.3333) + (final * 0.3333)


if final_grade>= 99.0  and final_grade<= 100.0:
    grade = 1.00
    status = "exellent"
elif final_grade>= 96.0 and final_grade<= 99.0:
    grade = 1.25
    status = "outstanding"
elif final_grade>= 93.0 and final_grade<= 96.0:
    grade = 1.50
    status = "Superior"
elif final_grade>= 90.0 and final_grade<= 93.0:
    grade = 1.75
    status = "Very good"
elif final_grade>= 87.0 and final_grade<= 90.0:
    grade = 2.00
    status = "Good"
elif final_grade>= 84.0 and final_grade<= 87.0:
    grade = 2.25
    status = "Satisfaciory"
elif final_grade>= 81.0 and final_grade<= 84.0:
    grade = 2.50 
    statuts = "Fairly Satisfactory"
elif final_grade>= 78.0 and final_grade<= 81.0:
    grade = 2.75
    status = "Fair"
    
elif final_grade>= 75.0 and final_grade<= 75.0:
    grade = 3.00
    status = "Passed"
else:
    grade = 5.00
    status = "Failed"
    
print(f"Final Grade: {final_grade:.2f}")
print(f"Your grade: {grade}")
print(f"Status: {status}")