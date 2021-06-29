 #contactbook
class contactbook():
    def __init__(self, name, phnum):
        self.name = name
        self.phnum = phnum
        self.nprint = str()
        self.numprint = 0
        self.listnum = []
        self.listname = []
    
    def addmember(self):
        for i in range(len(self.listname)):
            if self.name == self.listname[i]:
                print("!!similar name exists!!")
        for i in range(len(self.listnum)):
            if self.phnum == self.listnum[i]:
                print("!!number you entered already exists with a name!!")
            else:#adding member and their number to the lists.
                    self.listnum.append(self.phnum)
                    self.listname.append(self.name)
                    print("contacts updated successfully!!")
            
        for i in range(len(self.listname)):#storing the added values in a variable in 
            self.nprint = (self.listname[i])#order to print it later
            
        for j in range(len(self.listnum)):
            self.numprint = (self.listnum[j])
            
        with open("database.txt", "a") as db:
            db.write(str(self.nprint).rstrip("")+"  :  ")#adding values to our created database
            db.writelines(str(self.numprint).rstrip("")+"\n")#with our created variables i.e, self.nprint etc.
            db.close()
        rd = open("database.txt", "r")
        pri = rd.readlines()#read each line and store it in pri
        v = list(map(lambda u: u.rstrip(), pri))#this will remove \n from the printed list
        print(v)
        rd.close()
            
        while True:
            inp = input("do you want to add more:(y/n) or do you want to search someone in the list(press 's')")
            if inp == "s":
                search = input("enter the exact name of the contact: \n ")
                flag = 0
                global file
                file = open("database.txt", "r")
                rdl = file.readlines()
                for rdl in file:#for line in file
                    if search == rdl:#if search matches the line
                        flag = 1
                        print("results found:)")
                        print("\n")
                        print(rdl)#prints line
                    
                    if flag == 0:
                        print("!!no such contacts found!!:(")
            elif inp == "n":
                file.close()
                break
            elif inp == "y":
                snum = int(input("enter the number:\n"))
                sname = str(input("enter the name:\n"))
                ls = contactbook(sname, snum)
                ls.addmember()
            else:
                print("O, o !!wrong input!!\n!!Enter either y or n or s!!")
            
            

def main():           
    number = input("enter you number: \n")
    ename = input("enter your name: \n")
    cd = contactbook(ename, number)
    cd.addmember()


if __name__ == '__main__':#run code
    main()









        