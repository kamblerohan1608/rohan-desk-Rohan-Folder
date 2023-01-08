#chapter 3 practise set


#question 2

'''
#Template my method

a=input("Enter your name : ")
date=input("Enter the date : ")
print(" Dear ",a,",\n We are happy to announce your status of selection.\n congratulations! You are selected!!!\n Thanks and regards, \n Dream Company","\n","Date : ",date )
'''

#Template right method


a=input("Enter your name : ")
date=input("Enter the date : ")
c='''
Dear |<a>|,

Greetings from the Dream company,
We are happy to tell you your selection status.
congratulation!!! You are selected!!!
Wishing you a great future ahead.

Thanks and regards,
Dream Company
date : |<date>|.'''
c=c.replace("|<a>|",a)
c=c.replace("|<date>|",date)

print(c)
