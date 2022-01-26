while True:
    try:
        age=int(input("enter your age"))
    except ValueError:
        print("please enter valid integer value")
    except:
        print("unexpected error")
    else:
      print(f"your age is:{age}")
    finally:
      print("this is finnaly block")
