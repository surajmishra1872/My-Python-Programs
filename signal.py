import time
def red():
    for i in range(30,0,-1):
        print(i)
        time.sleep(1)
        print("GO","\U0001F7E2")
        time.sleep(1)
    print("STOP")
    time.sleep(2)
    green()
        
def green():
    for i in range(30,0,-1):
        print(i,"STOP")
        time.sleep(1)
        print("STOP","\U0001F534")
        time.sleep(1)
    print("GO")
    time.sleep(2)
    red()

red()
    
    
