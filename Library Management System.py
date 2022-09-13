from random import randint, randrange
import datetime
import time as T
import re
regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
regex_2= "\S*(\S*([a-zA-Z]\S*[0-9])|([0-9]\S*[a-zA-Z]))\S*"
regex_3="[@_!#$%^&*()<>?/|}{~:]"
Book_Obj={}
All_Books={}
Book_ID=[]
Bookid=[]
Admin_data={}
Borr_Obj={}
Borr_log={}
All_borr={}
tday = datetime.date.today()

class book:
    def __init__(self,Title,Author_name,Total_pages,No_of_copies,ISBN,Pub_year):
        self.Title = Title
        self.Author_name= Author_name
        self.Total_pages = Total_pages
        self.No_of_copies = No_of_copies
        self.ISBN = ISBN
        self.Pub_year = Pub_year
        bookid =randint(1000,99999)
        if bookid in Bookid is True :
            new_ID=randint(1000,99999)
            self.BookID=new_ID
        else:
            self.BookID=bookid
        Book_ID.append(self.BookID)
        self.History=[]
        All_Books[self.BookID]=[self.Title,self.Author_name,self.Total_pages,self.No_of_copies,self.ISBN,self.Pub_year]
        Book_Obj[self.BookID]=self
        print("\nYou have successfully added new book",self.Title,"with book id:",self.BookID)
        
    def update_Title(self,x):
        try:
            New_Title=input("Please enter the new title:")
            self.Title = New_Title
            All_Books[x][0]=New_Title
            print("Title is updated as",self.Title,'\n')
        except:
            print("Error occurred!!Please try again!!")
        
    def update_Auth(self,x):
        try:
            New_Auth=input("Please enter new author name:")
            self.Author_name= New_Auth
            All_Books[x][1]=New_Auth
            print ("Author name is changed as",self.Author_name,'\n')
        except:
            print("Error occurred!!Please try again!!")
    
    def update_Pages(self,x):
        try:
            New_PageC =int(input("Please enter new page numbers:"))
            self.Total_pages=New_PageC
            All_Books[x][2]=New_PageC
            print("Number of pages are updated as",self.Total_pages,'\n')
        except:
            print("Error occurred!!Please try again!!")
        
    def update_copies(self,x):
        try:
            New_Copies=int(input("Please enter new number of copies:"))
            self.No_of_copies = New_Copies
            All_Books[x][3]= New_Copies
            print("Number of copies are updated as",self.No_of_copies,'\n')
        except:
            print("Error occurred!!Please try again!!")
        
    def update_ISBN(self,x):
        try:
            while True:
                isbn=input("Enter the 13 digit ISBN number of book:")
                if len(isbn)==13:
                    self.ISBN=isbn
                    All_Books[x][4]=isbn
                    print("ISBN number is successfully updated as",self.ISBN,'\n')
                    break
                else:
                    print('Please enter 13 digit ISBN number!')
        except:
            print("Error occurred!!Please try again!!")
        
    def update_PubYr(self,x):
        try:
            New_yr=int(input("Please enter new year:"))
            self.Pub_year= New_yr
            All_Books[x][5]=New_yr
            print("Publish year has been updated as",self.Pub_year,'\n')
        except:
            print("Error occurred!!Please try again!!")
        
    def book_issued(self,x):
        try:
            if All_Books[self.BookID][3] == 0:
                print("Book is out of stock.Please try again later!!")
            else:
                All_Books[self.BookID][3]-=1
                self.History.append(x)
        except:
            print("Error occurred!!Please try again!!")

    def book_returned(self,x):
        try:
            All_Books[self.BookID][3]+=1
        except:
            print("Error occurred!!Please try again!!")

class admin:
    def __init__(self,Name,Password):
        self.Name = Name
        self.Password = Password
        Admin_data[Name]=Password
    def Add_Book(self): 
        try:
            title=input("\nPlease enter the new book title:")
            author=input("Please enter author name of the book:")
            PageCnt=input("Please enter number of pages:")
            copies=int(input("Enter number of copies of book:"))
            while True:
                isbn=input("Enter the 13 digit ISBN number of book:")
                if len(isbn)==13:
                    ISBN=isbn
                    print(ISBN)
                    break
                else:
                    print('Please enter 13 digit ISBN number:')
            PubYear=input("Enter the publish year of book:")
            Title=book(title,author,PageCnt,copies,ISBN,PubYear)
        except:
            print("Error occurred!!Please try again!!")
        
    def Create_admin(self):
        try:
            id=input("\nPlease enter username:")
            ID=id.lower()
            if ID in Admin_data:
                print("User already exists.")
            else:
                PW=input("Please enter password:")
                Admin_data[ID]=PW
                ID = admin(ID,PW)
                print("\nNew admin account is successfully added.")
        except:
            print("Error occurred!!Please try again!!")

    def update_book(self):
        try:
            if bool(All_Books) is True:
                while True:
                    print("Please select which file needs to be updated: \n 1.Title of book \n 2. Author name \n 3.No. of pages of book \n 4.Number of copies \n 5.ISBN \n 6. Publish year\nPress 0 to quit\n")
                    Sel= int(input())
                    if Sel ==1:
                        ID = int(input("Please enter book id:"))
                        Book = Book_Obj[ID]
                        Book.update_Title(ID)
                    elif Sel == 2:
                        ID = int(input("Please enter book id:"))
                        Book = Book_Obj[ID]
                        Book.update_Auth(ID)
                    elif Sel == 3:
                        ID=int(input("Please enter book id:"))
                        Book = Book_Obj[ID]
                        Book.update_Pages(ID)
                    elif Sel == 4:
                        ID = int(input("Please enter book id:"))
                        Book = Book_Obj[ID]
                        Book.update_copies(ID)
                    elif Sel== 5:
                        ID = int(input("Please enter book id:"))
                        Book = Book_Obj[ID]
                        Book.update_ISBN(ID)
                    elif Sel == 6:
                        ID = int(input("Please enter book id:"))
                        Book = Book_Obj[ID]
                        Book.update_PubYr(ID)
                    elif Sel==0:
                        break
                    else:
                        print("You have selected invalid operation")
            else:
                print("Currently there is no book present in storage!!")
        except:
            print("Error occurred!!Please try again!!")


    def Delete_Book(self):
        try:
            if bool(All_Books) is True:
                ID=int(input(print("\nPlease enter the Id of the book which needs to be deleted:")))
                All_Books.pop(ID)
                Book_Obj.pop(ID)
                Book_ID.pop(ID)
                print("\nBook with ID no",ID,"is deleted from repository.")
            else:
                print("\nCurrently there is no book present in storage!!")
        except:
            print("Error occurred!!Please try again!!")
        
    def create_borrower(self):
        try:
            Name=input("\nEnter borrower name:")
            DOB=input("Enter date of birth:")
            Tel=input("Enter contact number:")
            while True:
                Email=input("Please enter your new Email id:")
                if (re.search(regex,Email)):
                    email=Email.lower()
                    break
                else:
                    print("Please enter valid email ID!")
            print("Default password is user@123")
            Name= borrower(Name,DOB,Tel,Email,'user@123')
        except:
            print("Error occurred!!Please try again!!")
        
    def issue_book(self):
        try:
            UN=input("Please enter the email id of borrower:\t")
            ID=int(input("Please enter the ID of the book which needs to be issued:"))
            if UN in Borr_Obj and ID in Book_Obj:
                Book_Obj[ID].book_issued(UN)
                Borr_Obj[UN].borrow(ID)
                print("\n",Book_Obj[ID].Title,"is issued to",Borr_Obj[UN].Name)
            else:
                print("You have entered wrong email id or book id,Please try again!!")
        except:
            print("Error occurred!!Please try again!!")

    def Accept_book(self):
        try:
            ID=int(input("Please enter the ID of the book:"))
            UN=input("Please enter the email id of borrower:")
            if ID in Book_ID:
                Book_Obj[ID].book_returned(ID)
                Days=Borr_Obj[UN].return_book(ID)
                if Days<= 15:
                    print("\nThe book is returned in time!No fine will be charged!")
                else:
                    print("\nFine of 100 Rs will be charged as book is returned after 14 days.")
            else:
                print("\nYou have entered wrong book is!!Please try again!")
        except:
            print("Error occurred!!Please try again!!")
            
    def Show_details(self):
        try:
            ID=int(input("Please enter the book id:"))
            if ID in All_Books:
                print("Details of book with id",ID,'are as follows:\n')
                print("Name of book:",All_Books[ID][0],'\t\tAuthor of book:',All_Books[ID][1],'\tNumber of pages of book:',All_Books[ID][2])
                print("Copies available in library:",All_Books[ID][3],"\tISBN number:",All_Books[ID][4],'\tPublish year of book:',All_Books[ID][5])
                print("\nBorrowing history of book:")
                try:
                    for i in range(len(Book_Obj[ID].History)):
                        print(Borr_Obj[Book_Obj[ID].History[i]].Name)
                except:
                    print("No borrowing history!!")
            else:
                print("No book exist with mentioned book id!")
        except:
            print("Error occurred!!Please try again!!")
            
    def All_Borr(self):
        try:
            if bool(Borr_Obj) is True:
                print("Below is the list of all borrowers")
                for i,j in All_borr.items():
                    print('Email id of borrower:',i,"\nName of borrower:",j[0],"\t\tDOB of borrower:",j[2],"\t\tContact number of borrower:",j[1])
                    print("Borrowing history:",)
                    for k,o in Borr_Obj[i].Hist.itmes():
                        print("ID of borrowed book:",k,"Borrowed date:",o)
            else:
                print("There are no borrowers present at this moment!\n")
        except:
            print("Error occurred!!Please try again!!")
            
    def All_Books(self):
        try:
            if len(Book_ID)!=0:
                c=1
                for i in range(len(Book_ID)):
                    ID=Book_ID[i]
                    print(c,".Details of book with id:",ID,'are as follows:\n')
                    print("\tName of book:",All_Books[ID][0],'\t\tAuthor of book:',All_Books[ID][1],'\tNumber of pages of book:',All_Books[ID][2])
                    print("\tCopies available in library:",All_Books[ID][3],"\tISBN number:",All_Books[ID][4],'\tPublish year of book:',All_Books[ID][5])
                    print("\ntBorrowing history of book:")
                    for i in range(len(Book_Obj[ID].History)):
                        print('\t',Borr_Obj[Book_Obj[ID].History[i]].Name)
            else:
                print("Currently there is no book in repository!")
        except:
            print("Error occurred!!Please try again!!")

                
Admin=admin('admin','Admin')

class borrower:
    def __init__(self,Name,DOB,Number,Email,Password):
        self.Name=Name
        self.DOB=DOB
        self.Number=Number
        email=Email.lower()
        self.Email=email
        self.Password=Password
        self.Borrowed={}
        self.Hist={}
        self.History=[]
        Borr_log[self.Email]=self.Password
        All_borr[self.Email]=[self.Name,self.Number,self.DOB,self.Password]
        Borr_Obj[self.Email]=self
        print("New user is successfully registered!!")
        
        
    def borrow(self,ID):
        try:
            borrow_date=tday
            self.Borrowed[ID]=borrow_date
            self.Hist[ID]=borrow_date
            
            self.History.append([ID,borrow_date])
        except:
            print("Error occurred!!Please try again!!")

    def return_book(self,ID):
        try:
            if ID in self.Borrowed:
                delta=tday-self.Borrowed[ID]
                self.Hist.pop(ID)
                D=delta.days
                return D
                print(delta.days)
            else:
                print("Nothing borrowed yet!")
        except:
            print("Error occurred!!Please try again!!")

    def time(self):
        try:
            if len(self.Hist) != 0:
                for i,j in self.Hist.items():
                    T=14-(j-tday).days
                    print("Remaining time for book ",Book_Obj[i].Title ,":", T)
            else:
                print("You have not borrowed any book currently!!")
        except:
            print("Error occurred!!Please try again!!")
            
    def hist(self):
        try:
            for i in range(len(self.History)):
                print("Book name",Book_Obj[self.History[i][0]].Title ,":Issue date",self.History[i][1])
        except:
            print("Error occurred!!Please try again!!")
            
    def book_det(self):
        try:
            if len(self.History)!=0:
                print("History of previously borrowed books:")
                for i in range(len(self.History)):
                    ID=self.History[i][0]
                    print("Details of book with id:",ID,'are as follows:\n')
                    print("Name of book:",All_Books[ID][0],'\t\t\tAuthor of book:',All_Books[ID][1],'\tNumber of pages of book:',All_Books[ID][2])
                    print("\tISBN number:",All_Books[ID][4],'\tPublish year of book:',All_Books[ID][5])
            else:print("\nYou have borrowed zero books in past.\nPlease borrow some books!\n")
        except:
            print("Error occurred!!Please try again!!")

print("!!!!Welcome to Library Management System!!")
T.sleep(0.7)
try:
    while True:
        Role=int(input("Please select you role sir:\n1.Admin\t\t2.User\nSelect 0 to quit!\n"))
        if Role == 1:
            try:
                T.sleep(0.5)
                print("Now you are in Admin interface!!")
                while True:
                    ID=input("Hii!!\nPlease enter your user id to login or type 'quit' to quit:")
                    PW=input("Please your password or type 'quit' to quit:")
                    id=ID.lower()
                    if id in Admin_data and Admin_data[id]== PW:
                        T.sleep(0.5)
                        print("\nYou have successfully logged in to the admin system!\n")
                        try:
                            while True:
                                print("\nPlease select the operation you want perform from following list\n")
                                Sel=int(input('1.Add new admin\t\t\t\t2.Add new book\n3.Add new borrower\t\t\t4.View book details and borrowing history\n5.Update existing book\t\t\t6.Delete book\n7.List of borrowers and there history\t8.Issue book to borrower\n9.Accept the returned book\t\t10.Show all books\nPlease select 0 to quit!\n'))
                                if Sel == 1:
                                    T.sleep(0.5)
                                    Admin.Create_admin()

                                elif Sel == 2:
                                    T.sleep(0.5)
                                    Admin.Add_Book()

                                elif Sel==3:
                                    T.sleep(0.5)
                                    Admin.create_borrower()

                                elif Sel==4:
                                    T.sleep(0.5)
                                    Admin.Show_details()

                                elif Sel ==5:
                                    T.sleep(0.5)
                                    Admin.update_book()

                                elif Sel == 6:
                                    T.sleep(0.5)
                                    Admin.Delete_Book()

                                elif Sel == 7:
                                    T.sleep(0.5)
                                    Admin.All_Borr()

                                elif Sel == 8:
                                    T.sleep(0.5)
                                    Admin.issue_book()

                                elif Sel == 9:
                                    T.sleep(0.5)
                                    Admin.Accept_book()

                                elif Sel == 10:
                                    T.sleep(0.5)
                                    Admin.All_Books()

                                elif Sel == 0:
                                    T.sleep(0.5)
                                    break
                                else:
                                    T.sleep(0.5)
                                    print("Please select appropriate option!!")
                            break
                        except:
                            print("Error occurred.Please try again!!\n")
                    elif id in Admin_data and Admin_data[id]!= PW:
                        T.sleep(0.7)
                        print("You have entered wrong password")
                    elif id == 'quit' or PW == 'quit':
                        T.sleep(0.7)
                        break
                    else:
                        T.sleep(0.7)
                        print("You have entered wrong id username!!")
            except:
                print("Error occurred.Please try again!!\n")
        elif Role == 2:
            T.sleep(0.5)
            print("Now you are in user interface!")
            while True:
                Log=int(input("\nPlease select 1 to log in if you are registered or select 2 to register yourself.\nSelect 0 to quit!\n"))
                if Log == 2:
                    T.sleep(0.5)
                    Name=input("Please enter your name:")
                    Num=input("Please enter your contact number:")
                    while True:
                        Email=input("Please enter your Email id:")
                        if (re.search(regex,Email)):
                            email=Email.lower()
                            break
                        else:
                            print("Please enter valid email ID!")
                    DOB=input("Please enter your Date of birth:")
                    while True:
                        Pass=input("Please enter password(password must contains number,letters and speacial character eg.@,# etc:\n")
                        if (re.search(regex_2,Pass)) and (re.search(regex_3,Pass)):  
                            Pass_2=Pass
                            break
                        else:
                            print("Please enter valid alpha-numeric password")
                    Name=borrower(Name,DOB,Num,email,Pass_2)
                elif Log == 1:
                    T.sleep(0.5)
                    while True:
                        ID=input("Please enter your email id or enter 'quit' to quit:")
                        ID_2 = ID.lower()
                        Pass = input("\nPlease enter your password:")
                        if ID_2 in Borr_log and Borr_log[ID_2] == Pass:
                            print("\nYou have successfully logged in!!\n")
                            try:
                                while True:
                                    Sel=int(input("\nPlease select the desired operations:\n1.View the list of currently borrowed books\t2.View the details of each borrowed book\n3.View the list of books borrowed in past\nPress 0 to quit!!\n"))
                                    if Sel == 1:
                                        T.sleep(0.5)
                                        Borr_Obj[ID_2].time()
                                    elif Sel == 2:
                                        T.sleep(0.5)
                                        Borr_Obj[ID_2].book_det()
                                    elif Sel == 3:
                                        T.sleep(0.5)
                                        Borr_Obj[ID_2].hist()
                                    elif Sel == 0:
                                        T.sleep(0.5)
                                        break
                                    else:
                                        T.sleep(0.5)
                                        print("Please select the appropriate option!!")
                                break
                            except:
                                print("Error occurred.Please try again!!\n")

                        elif ID_2 in Borr_log and Borr_log[ID_2]!= Pass:
                            T.sleep(0.7)
                            print("You have entered wrong password.Please try again!")
                        elif ID_2 == 'quit' or Pass == 'quit':
                            break
                        else:
                            T.sleep(0.7)
                            print("You have entered wrong email id or password or you are not a registered user. Please try again!")
                elif Log == 0:
                    T.sleep(0.5)
                    break
                else:
                    print("Please select appropriate option!!")

        elif Role == 0:
            T.sleep(0.5)
            break
        else:
            T.sleep(0.6)
            print("Please select appropriate option!!\n")
except:
    print("Error occurred.Please try again!!\n")