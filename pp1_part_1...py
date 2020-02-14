count = 0
total = 0
average = 0
max_marks = 0  #if i assign 100 marks then, 100 is maximum marks
min_marks = 100 #if i assign 0 marks then, 0 is minimum marks 
grade_stu = 0
m0_29 = ""
m30_39 = ""
m40_69 = ""
m70_100 = ""

#set as marks 0
marks = 0
while marks>=0:
    try: #show error and continue the programme
        marks = int(input("Please Enter the Marks = "))
        if 0<=marks<=100: #chek the range
            total = total + marks
            count = count + 1
            if 0<=marks<=29:
                m0_29 += "*" #print the *
            elif 29<marks<=39:
                m30_39 += "*" #print the *
            elif 39<marks<=69:
                m40_69 += "*" #print the *
            elif 69<marks<=100:
                m70_100 += "*" #print the *
            if max_marks<marks:
                max_marks = marks #assign as a maximum marks
            if min_marks>marks:
                min_marks = marks   #assign as a minimum marks
            if marks>=40: 
                grade_stu = grade_stu + 1  #count the passed students
                
            
        else: #if they enter over the 100 marks
            print("Please re-enter the marks below the 100")
    #error fix
    except ValueError:
        print("Please enter the valid marks") #show the error

    

print()
print()
print()
print("________________________________________________________________")
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print()
print("Please wait........")
print("Please wait........")
print()
print("Total Marks     = ",total)
try:    
    print("Average Marks   = ",total/count) #divide
except ZeroDivisionError:
    print("No marks enterd")
print("Maximum Marks   = ",max_marks)
print("Minimum Marks   = ",min_marks)
print("Number of Marks = ",count)
print("Graded Students = ",grade_stu)

print()
print()
print()

print("________________________________________________________________")
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print()
print("Horizontal Histogram View")
print("-------------------------")
print()
print("00 - 29    -  ",m0_29)
print("30 - 39    -  ",m30_39)
print("40 - 69    -  ",m40_69)
print("70 - 100   -  ",m70_100)

print()
print()
print()
print()
print()

print("________________________________________________________________")
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print()
print()
print()
print()

print("Vertical Histogram View")
print("-----------------------")
print()
print("00-29\t30-39\t40-69\t70-100")

total_star = m0_29+m30_39+m40_69+m70_100
a = 1
b = 1
c = 1
d = 1
for x in total_star:
    print(" ",end="")
    if a<=len(m0_29):
        print(" ",x,end="\t")
    else:
        print(" ",end="\t")
    a+=1

    if b<=len(m30_39):
        print(" ",x,end="\t")
    else:
        print(" ",end="\t")
    b+=1

    if c<=len(m40_69):
        print(" ",x,end="\t")
    else:
        print(" ",end="\t")
    c+=1
    if d<=len(m70_100):
        print(" ",x,end="\t")
    else:
        print(" ",end="\t")
    d+=1
    print()

print("_______________________________________________________________")
print()
print("Thank you .........")
print()
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")

