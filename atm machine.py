print('welcome to sbi atm \n bherpur shakha \n pincode 212307')
print("enter your card within few second")
enterpin = int(input("please enter your pin"))
if enterpin == 212307:
   accounttype = input("choese your account type: (account type)")
   if accounttype == 'saving':
    entermony = int(input("enter your mony"))
    if entermony <=10000:
     print('please wait work under proccesing')
     print('mony hanve withdrawled \n thanks for visit')
    else:
     print("your enter mony is high")
     print('mony hanve withdrawled \n thanks for visit')
   else:
     print('error')  
        

