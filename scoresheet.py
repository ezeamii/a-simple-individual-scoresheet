# THIS PROGRAM IS TO FIND THE NUMBER OF SUBJECT A STUDENT DOES, AND THE STUDENTS SUM, AVERAGE AND GRADE FROM THE
# SUBJECTS

print("---------Welcome to Shelby School's subject score sheet----------")
print("Please input your 10 subjects below.")

subjects = []

no_of_subjects = 10


def insert():
    for i in range(1, no_of_subjects + 1):
        subject = str(input("Enter subject: "))
        subjects.append(subject)
    print(subjects)


insert()


a = int(input("what is your score in " + subjects[0] + " : "))
b = int(input("what is your score in " + subjects[1] + " : "))
c = int(input("what is your score in " + subjects[2] + " : "))
d = int(input("what is your score in " + subjects[3] + " : "))
e = int(input("what is your score in " + subjects[4] + " : "))
f = int(input("what is your score in " + subjects[5] + " : "))
g = int(input("what is your score in " + subjects[6] + " : "))
h = int(input("what is your score in " + subjects[7] + " : "))
i = int(input("what is your score in " + subjects[8] + " : "))
j = int(input("what is your score in " + subjects[9] + " : "))


sum_of_scores = (a + b + c + d + e + f + g + h + i + j)
print("The sum of your scores is", sum_of_scores)

average_of_scores = (sum_of_scores/no_of_subjects)
print("The average of your subjects is ", average_of_scores)

if average_of_scores >= 80:
    print("Your overall grade is A")
elif average_of_scores >= 70:
    print("Your overall grade is B")
elif average_of_scores >= 60:
    print("Your overall grade is C")
elif average_of_scores >= 50:
    print("Your overall grade is D")
else:
    print("Your overall grade is F")

if average_of_scores >= 80:
    print("Congratulations. You have been granted a full tuition scholarship")
elif average_of_scores >= 70:
    print("Congratulations. You have been granted an 80% tuition scholarship")
elif average_of_scores >= 60:
    print("Congratulations. You have been granted a 60% tuition scholarship")
else:
    print("Sorry. You could not get the scholarship")