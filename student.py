student=input ("enter how many student you want to add")
student=(int(student))                                              #completeted
x=1
x=(int(x))


while x<=student:
    print ("========student result=======")
    student_name = input("enter student name")
    student_name=(str(student_name))
    english = input("enter marks in english")
    english=(int(english))
    nepali = input("enter marks in nepali")
    nepali=(int(nepali))
    math = input("enter marks in math")
    math=(int(math))
    science = input("enter marks in science")
    science=(int(science))
    population = input("enter marks in population")
    population=(int(population))

    print ("student_name"),student_name
    print ("marks in english"),english
    print ("marks in nepali"),nepali
    print ("marks in math"),math
    print ("marks in science"),science
    print ("marks in population",population)
    total=english+nepali+math+science+population
    total=(int(total))
    print ("your total marks is",(total))
    percent=(total/5)
    percent=(int(percent))
    print ("your percent is",(percent))
    if percent>=60 and percent<=70:
        devision=("third devision")
    elif percent>=70 and percent<=80:
        devision=("second devision")
    elif percent>=80 and percent<=90:
        devision=("first devision")
    else:
        devision=("fail")

    devision=(str(devision))
    print ("your devision is ",(devision))
    x+=1