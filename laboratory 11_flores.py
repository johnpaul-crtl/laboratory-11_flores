counter = 0
passed = 0
numlist = []

for x in range(5) :
    num = int(input("Enter you Grade: "))
    
    if num <= 39 or num >= 101:
        print("Invalid. number must be between 40 and 100 only")
        break
    else:
        numlist.append(num)
        
    if num >= 75:
        passed += 1
        counter += 1
    else:
        counter += 1
        
    if counter == 5:
        print()
        sumNums = sum(numlist)
        averageGrade = sumNums / 5
        averageGrade = round(averageGrade, 2)
        
        passPercent = (passed / len(numlist)) * 100
        passPercent = round(passPercent, 2) 
        
        print("Grade Inputted : " + str(numlist))
        print("Average grade: " + str(averageGrade)) 
        print("Number of people who passed: " + str(passed)) 
        print("Average of people who passed: " + str(passPercent) + "%" )     