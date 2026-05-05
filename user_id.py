import os
print("-------------------------------")
print("| WELCOME TO LOGIN AND SIGN UP |")
print("--------------------------------\n")

def this():
    x = input("SIGN UP(A) OR LOGIN USER(B):- ")
    if "A" == x or "a" == x:
        print("-----------------LOGIN YOUR ID------------------\n")
        
        call()
    if "B" == x or "b" == x:
        check()
        
    else:
        print("CHOICE ONLY A OR B")
        print("____________________\n")
        
    this()
    
def call():
    a = input("SET YOUR ID :- ")
    f = input("SET YOUR PASSWORD :- ")
    r = f"{a},{f}"
    os.popen(f"echo {r}>> example.txt")
    print("SIGN UP SUCCESSFUL ")
    print("-------------------\n")
    this()
    
e = []    
def check():
    global e
    user = input("ENTER YOUR USER ID TO LOGIN OR CLS TO SET ID :- ")
    if user.lower() == "cls":
        call()
        return
    if user in e:
        print("YOURE BLOCKED")
        this()
        
    lines = os.popen("type example.txt").read()
    lines = lines.splitlines()
    for line in lines:
        if user in line:
            print("\n----------------------")
            print("|   USER AVAILABLE ! |")
            print("----------------------\n")
            y,x = line.split(",")
            for i in range(3):
                password = input("ENTER YOUR PASSWORD :- ")
                if password == x:
                    print("LOGIN SUCCESSFUL\n")
                    this()
                else:
                    print("WRONG PASSWORD\n")
                    print("YOU ARE BLOCKED AFTER 3 FAILED ATTEMPTS\n")
                
                if i==2:
                    e.append(user)
                    print(f"YOURE BLOCKED {user} !")
                    this()
    else:
        print("\n-------------------------------")
        print("|   THIS USER NOT AVAILABLE   |")
        print("|    PLEASE TRY AGAIN         |")
        print("------------------------------|\n")
        check()

this()