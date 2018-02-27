#Nikhil Amin -:- https://github.com/nikhilamin073
#Python Script to calculate SGPA of VTU CSE students


print("\n**************************************************************************")
print("************* SGPA CALCULATOR FOR VTU CSE STUDENTS (5th SEM) *************")
print("**************************************************************************\n")
print("Enter your Marks of 6 Subjects and 2 Labs in Order as Shown below: ")
print("|| ME | CN | DBMS | ATC | A.JAVA & J2EE | ECS | CN Lab | DBMS Lab ||\n")

marks = []
grade = []
credits = []
marks = list(map(int, input().split()))

for x in range(8):
#	print("x is ",x,"and value is", marks[x])
	if marks[x] < 40 :
		grade.append(0)
	elif marks[x] >=40 and marks[x] < 45:
		grade.append(4)
	elif marks[x] >=45 and marks[x] < 50:
		grade.append(5)
	elif marks[x] >=50 and marks[x] < 60:
		grade.append(6)
	elif marks[x] >=60 and marks[x] < 70:
		grade.append(7)
	elif marks[x] >=70 and marks[x] < 80:
		grade.append(8)
	elif marks[x] >=80 and marks[x] < 90:
		grade.append(9)
	elif marks[x] >=90 and marks[x] <= 100:
		grade.append(10)
	else:
		print("Invalid Input!")				
	
print("\nMarks:               ",marks)
print("Grade:               ",grade)

for x in range(8):
	if x < 4:
		cp = grade[x]*4
		credits.append(cp)
	elif x < 6:
		cp = grade[x]*3
		credits.append(cp)
	else:
		cp = grade[x]*2
		credits.append(cp)
print("Credits:             ",credits)
print("Total Credit Points: ", sum(credits))

print("SGPA:                ",round((sum(credits) / 26),2))

