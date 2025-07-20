Marks=int (input("Enter the marks: "))
if  Marks > 100:
    print("Invalid marks entered. Please enter a number between 0 and 100.")
if Marks >= 95 and Marks <= 100:
    print("grade A+")
elif Marks >= 90 and Marks < 95:
    print("grade A")
elif Marks >= 85 and Marks < 90:
    print("grade B+")
elif Marks >= 80 and Marks < 85:
    print("grade B")
elif Marks >= 75 and Marks < 80:
    print("grade C+")
elif Marks >= 70 and Marks < 75:
    print("grade C")
elif Marks >= 65 and Marks < 70:
    print("grade D+")
elif Marks >= 60 and Marks < 65:
    print("grade D")
elif Marks >= 50 and Marks < 60:
    print("grade E")
elif Marks >= 40 and Marks < 50:
    print("grade F")

