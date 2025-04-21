Maths=int(input("Enter your Maths marks: "))
English=int(input("Enter your English marks: "))
Science=int(input("Enter your Science marks: "))

total_marks= Maths + English + Science
average_marks= total_marks/3
percentage= (total_marks/300)*100
print("Total marks are: ", total_marks)
print("Average marks are: ", percentage)
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B+")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C+")
else:
    print("Grade: C")