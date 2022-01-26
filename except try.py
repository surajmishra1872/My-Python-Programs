while True:
    try:
        age = int(input("enter your age:"))
        
    except ValueError:
        print("there is value error")
    except:
         print("other type error")
    else:
        print(f"you enter{age}")
    finally:
        print("hello")
         
         
         

if age<18:
    print("you  not eligeble")

else:
   print("you are eligble")
