i=1
passes=0
fails=0
total=0
highest=0
lowest=0
while i <=15:
    marks = int(input("enter student marks {}:". format(i)))
    i+=1
if marks >= 90:
   grade = "outstanding"
elif 89 > marks >= 75:
    grade="distinction"
elif 74> marks >=40:
    grade= "pass"
else:
    print("fail")
if marks<lowest:
    highest=marks
if marks>highest:
    lowert=marks

total +=marks
i +=1
print("Number of student pass: ",passes)
print("number of student fall: ",fails)
print("highest number: ",highest)
print("lowert number: ",lowest)
print ("Averaage marks:", total/15)