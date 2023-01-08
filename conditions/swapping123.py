'''
#Example 1 : Percentage - Even if user enter gives opposite inputs like total makes in obtained and obtained in total marks still should get appropriate output. 

total=int(input("Enter the total marks : "))
marks = int(input("Enter the marks obtained : "))

if (total > marks):
    print("Your percentages are : ",marks/total*100,"%")
elif(marks > total):
    print("Your percentages are : ",total/marks*100,"%")
print("Program Finished.")

'''

#Example 2 : Percentage (with swap) - Even if user enter gives opposite inputs like total makes in obtained and obtained in total still should get appropriate output. 

total=int(input("Enter the total marks : "))
marks = int(input("Enter the marks obtained : "))

if (marks > total):
    total,marks = marks,total
    
print("Your percentages are : ",marks/total*100,"%")
print("Program Finished.")
