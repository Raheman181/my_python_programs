#database required is logindata.txt here:

class login():
    def __init__(self, usrname, passwd):
        self.usrname = usrname
        self.passwd = passwd
       

    def add(self):#signup
        with open("logindata.txt", "a") as ld:
            ld.write(self.usrname + " : " + self.passwd +"\n")
            print("\n Data added successfully!! \n       Thank You!!")
            print("   Username: ",self.usrname + "\n" + "   Password: ",self.passwd,"\n")
            ld.close()
            
    def valid(self):#to check if the username and pass. provided matches with the one stored in the database(logindata.txt here):
        with open("logindata.txt", 'r') as ld:#this will close file after execution of indented algorithm anyway even if we didn't close it.
            read = ld.readlines()
            for i in read:
                wordlist = []
                wordlist.append(i.split(" " or "\n"))
                if wordlist[0][0] == self.usrname:
                    if wordlist[0][2] == str(self.passwd+"\n"):#in file database, i've reserved the position [2] for password
                        return True
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           

def log_in():
    sign_in = input("  !!Do you want to login to your account (enter l or login for login)!! \n  !!OR press s for signup!! \n  !!OR enter e or exit to exit!! \n >>>>>>>>>>>>>>>>>>>>>>:")
    si = sign_in.lower()
    global uname, passsw
    if si == "l" or si == "login":
        ret = enterfield_login()#uses return value of enterfield() and assigns li to ret
        if (ret.valid()):
            print("  **Congrats!! \n  **Access Granted!! ")
            
        else:
            print("!!Access Denied!!")
            run2 = input("<<want to run again!!(press y or n)>>: ")
            r2 = run2.lower()
            if r2 == "y" or r2 == "yes":
                log_in()
            else:
                quit()
    
    elif si == "s" or si == "S":
        sign_up()

    elif si == "e" or si == "exit":
        quit()
        
    else:
        print("wrong input!! ")
        log_in()
#----------------------------------------------------------------------------------------------------------

def enterfield_login():#This will be used while the time of login
    uname1 = input("Enter your username: ")
    passw1= input("Enter your password: ")
    loginn = login(uname1, passw1)
    return loginn
#----------------------------------------------------------------------------------------------------------

def sign_up():#this will only be called for signup cuz we need to check if username & password are valid.
    uname = input("Enter your username: ")
    if check_avail_un(uname):
        passw = input("Enter your password: ")
        if check_avail_ps(passw):
            li = login(uname, passw)
            li.add()
#---------------------------------------------------------------------------------------------------------- 
  
def check_avail_un(un):#Check this function tommorow as this func is not returning true value:
    if len(un)==0:
        print("Username can't be empty!!")
        return sign_up()#we're returning sign_up() cuz if the if condition evaluates to-
                        #-true we'll return the value of function as sign_up instead of true
    
    elif len(un)<3:
        print("!!Length of username should not be less than three!!")
        return sign_up()

    elif " " in un:#check for spaces in username
        print("spaces not allowed")
        return sign_up()
    
    #Check if username is available
    elif un != ' ':#just ensuring username isn't blank
        file= open("logindata.txt", "r")
        read = file.readlines()
        for i in read:
            wordlist = []
            wordlist.append(i.split(" " or "\n"))
            if wordlist[0][0] == un:#in the database file, i've reserved [0] as the position for username.
                print("Username already taken!!: \n choose another one!!")
                return sign_up()

    return True

#----------------------------------------------------------------------------------------------------------

def check_avail_ps(ps):
    if " " in ps:#check for spaces in password
            print("spaces not allowed")
            return sign_up()
    elif len(ps)<5 or len(ps)==0:#check password length
            print ("Minimum length is 5 charecters..")
            return sign_up()

    else:
        return True
#----------------------------------------------------------------------------------------------------------

def quit():
    return None


if __name__ == '__main__':
    log_in()