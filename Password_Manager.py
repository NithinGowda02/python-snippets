
def add():
    name = input("Name : ")
    pwd = input("Password : ")
    with open("passwords.txt","a") as f:
        f.write(f"{name}|{pwd}\n")

def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, paswd = data.split("|")
            print(f"USER NAME >> {user} \nPASSWORD >> {paswd} ")
                   
while True:
    mode = input("would you like to Add a new password or view the existing passwords (Type:view/add).Press q to quit >>").lower()

    if mode == "q":
        break    
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Mode!, Try Again...")
        continue     