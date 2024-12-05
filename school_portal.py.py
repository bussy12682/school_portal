#Create a school portal for checking students grades which takes the input
# to determine 5 subjects grades (english, maths, chem, physics, ict)
# student score in each subject
# ask of student first name, student last name, school name, student seat number, student exam number, student gender.
# which returns the output 
# portal loading!, portal loading!!, portal loading!!!
# cumulative grade, average grade, status (pass or fail).
# and make it user friendly.

Is_user_a_student_of_this_school = str(input("Are you a student of this school input 'yes' or 'no' : "))
if Is_user_a_student_of_this_school.upper() == "YES":
    print("PORTAL LOADING !!! " * 3)
elif Is_user_a_student_of_this_school.upper() == "NO":
    print("Exiting...")
    exit()



def student_details():
    global student_first_name, student_last_name, student_school, student_exam_number, student_seat_number
    student_first_name = input('Input your first name : ')
    student_last_name = input('Input your last name : ')
    student_full_name = student_first_name.title() + " " + student_last_name.title()
    student_school = input("Enter school name : ")
    student_gender = input("Enter your gender (Male or Female) : ")
    student_exam_number = input(f"{student_full_name}, Please enter your registration/exam number : ")
    student_seat_number = input("Enter your seat number : ")
    print()
    print()
    print()
    print(f'Fullname : {student_full_name.title()}')
    print(f'SCHOOL NAME : {student_school.title()}')
    print(f'Gender : {student_gender.title()}')
    print(f'Exam/registration number : {student_exam_number}')
    print(f"Seat number : seat number {student_seat_number}")

def grade_calculation():
    global subject_and_grade
    
    print("The score inputed is from a scale of 1 - 100 , !!!")
    English = int(input("Input your english score : "))
    Mathematics = int(input("Input your Mathematics score : "))
    Physics = int(input("Input your Physics score : "))
    Chemistry = int(input("Input your Chemistry score : "))
    ICT = int(input("Input your ICT score : "))
    subject_and_grade = {"English":English , "Mathematics":Mathematics, "Physics":Physics,"Chemistry":Chemistry,"ICT":ICT}
    print()
    print()
    print()
    print(f"Subjects: \n {subject_and_grade}")
    pass_mark = 50
    import math
    
    Cummulative_score = sum(subject_and_grade.values())
    number_of_subjects = len(subject_and_grade)
    Average_score = Cummulative_score/number_of_subjects
    print(f'your cummulative average grade score is {Average_score}')


    if Average_score>= 50 :
        print(f'Status : Pass !!!')
    elif Average_score< 50 :
        print(f'Status : Fail ')
    
    for grade in subject_and_grade.values():
     if grade in range(70, 101):
        print("A  excellent")
     elif grade in range(60, 70):
        print("B  very good")
     elif grade in range(50, 60):
        print("C  good")
     elif grade in range(40, 50):
        print("D  fair")
     elif grade in range(30, 40):
        print("E  poor")
     elif grade in range(20, 30):
        print("F9  fail")


def user_choice():
     print()
     print()
     print("YOUR STATEMENT OF RESULT")
     print("To whom it may concern")
     print(f"This is to inform you that {student_first_name.title()}  {student_last_name.title()} of {student_school.title().title()} school, with exam number {student_exam_number}  seat number {student_seat_number} successfully pass his examination at  {student_school.title()}.")

     print("Below is the result summary")
     print(f"Subjects: \n {subject_and_grade}")
    
     for grade in subject_and_grade.values():
      if grade in range(70, 101):
        print("A  excellent")
      elif grade in range(60, 70):
        print("B  very good")
      elif grade in range(50, 60):
        print("C  good")
      elif grade in range(40, 50):
        print("D  fair")
      elif grade in range(30, 40):
        print("E  poor")
      elif grade in range(20, 30):
        print("F9  fail")
  
    
student_details()
grade_calculation()  
user_choice()

def tryagain():
    student_details()
    grade_calculation()

user_try_again = str(input("Do you want to check your score again (yes or no) ? "))
user_trial = 0
max_trial = 5
while user_trial<max_trial:
    if user_try_again.title() == "Yes":
        tryagain()
    user_trial+=1
    print(f'You have {max_trial - user_trial} trials left !!!')
    
    if user_try_again.title() == "No":
        print("Thank you!.")
        print("Below is the result summary")
        user_choice()
        exit()



if user_trial == max_trial:
    print("You've exceeded your maximum trial\n rerun to use portal !!")
    print("LOGGING OUT !!!")
    exit()
    
