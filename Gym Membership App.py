import time as T
import re
regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
Users={}
Regimen_Data={}

Regimen={1:{'Mon':'Chest','Tue':'Biceps','Wed':'abs/Rest','Thu':'Back','Fri':'Triceps','Sat':'Rest','Sun':'Rest'},
        2:{'Mon':'Chest','Tue':'Bicep','Wed':'Cardio/Abs','Thu':'Back','Fri':'Triceps','Sat':'Legs','Sun':'Rest'},
        3:{'Mon':'Chest','Tue':'Bicep','Wed':'Cardio/Abs','Thu':'Back','Fri':'Triceps','Sat':'Legs','Sun':'Cardio'},
        4:{'Mon':'Chest','Tue':'Bicep','Wed':'Cardio','Thu':'Back','Fri':'Triceps','Sat':'Cardio','Sun':'Cardio'}}

class superuser:
    def __init__(self):
        pass
    
    def Create_Member(self):
        try:
            Name=input("Please enter the name:")
            Age=input("Please enter the age:")
            Gender=input("Please enter the gender:")
            Number=input("Please enter the contact number:")
            while True:
                Email=input("Please enter the email id:")
                if (re.search(regex,Email)):
                    email=Email.lower()
                    break
                else: print("Please enter valid email ID!")
            BMI=int(input("Please enter the BMI:"))
            while True:
                try:
                    Dur=int(input("Please enter the Mebership duration from 1,3,6,12:"))
                    if Dur==1 or Dur==3 or Dur==6 or Dur==12:
                        MemDur=Dur
                        break
                    else:print("Please enter correct duration.")
                except: print("Please select the appropriate option.")
            T.sleep(0.5)
            Name=user(Name,Age,Gender,Number,email,BMI,MemDur)
        except: print("Unknown error ocurred.Please try again.")
        
    def View_Member(self):
        try:
            if len(Users)!=0:
                Num=input("Please enter the contact number of member:\n")
                if Num in Users:
                    T.sleep(0.5)
                    Users[Num].Show_Profile()
                else: print("You have entered wrong number.Please try again.")
            else: print("No member is registered yet.")
        except: print("Unknown error ocurred.Please try again.")
        
    def Delete_Member(self):
        try:
            Num=input("Please enter the contact number of member:\n")
            if Num in Users:
                T.sleep(0.5)
                print("You have succesfully deleted",users[Num].Name)
                del users[Num]
            else: print("You have entered wrong number.Please try again.")
        except: print("Unknown error ocurred.Please try again.")
        
    def Update_Member(self):
        try:
            Num=input("Please enter the contact number of member:\n")
            T.sleep(0.5)
            while True:
                try:
                    sel=int(input("Please select what needs to be updated:\n1.Name\t\t\t2.Age\t\t3.Gender\n4.Mobile Number\t\t5.Email\t\t6.BMI\n7.Membership Duration\nSelect 0 to back.\n"))
                    if sel==1:
                        Users[Num].Update_Name()
                        break
                    elif sel==2:
                        Users[Num].Update_Age()
                        break
                    elif sel==3:
                        Users[Num].Update_Gender()
                        break
                    elif sel==4:
                        Users[Num].Update_Num()
                        break
                    elif sel==5:
                        Users[Num].Update_Email()
                        break
                    elif sel==6:
                        Users[Num].Update_BMI()
                        break
                    elif sel==7:
                        Users[Num].Update_Membership()
                        break
                    elif sel==0:
                        break
                    else:
                        print("Please select the appropriate option.")
                except: print("Please select appropriate option.")
        except: print("Unknown error ocurred.Please try again.")

    def Create_Regimen(self):
        try:
            Reg_Name=input("Please enter the name of regime:\n")
            T.sleep(0.3)
            Regimen[Reg_Name]={}
            Regimen[Reg_Name]['Mon']=input("Please enter the exercise for Monday:")
            Regimen[Reg_Name]['Tue']=input("Please enter the exercise for Tuesday:")
            Regimen[Reg_Name]['Wed']=input("Please enter the exercise for Wednesday:")
            Regimen[Reg_Name]['Thu']=input("Please enter the exercise for Thursday:")
            Regimen[Reg_Name]['Fri']=input("Please enter the exercise for Friday:")
            Regimen[Reg_Name]['Sat']=input("Please enter the exercise for Saturday:")
            Regimen[Reg_Name]['Sun']=input("Please enter the exercise for Sunday:")
            T.sleep(0.5)
            print("New regimen",Reg_Name,"is created.")
        except: print("Unknown error ocurred.Please try again.")
        
    def View_Regimen(self):
        try:
            while True:
                try:
                    print("Below is the list of all regimens:")
                    c=1
                    for i in Regimen.keys():
                        if i==1:
                            print(c,":BMI<18.5")
                        elif i==2:
                            print(c,":18.5<BMI<25")
                        elif i==3:
                            print(c,":25<BMI<30")
                        elif i==4:
                            print(c,":30<BMI")
                        else: print(c,":",i)
                        c+=1
                    Sel=int(input("Please select the regime:\nSelect 1 to 4 for default\n5 for Others\nSelect 0 to go back\n"))
                    if Sel==1:
                        T.sleep(0.5)
                        print("Monday:",Regimen[1]['Mon'],"\nTuesday:",Regimen[1]['Tue'],"\nWednesday:",Regimen[1]['Wed'],"\nThursday:",Regimen[1]['Thu'])
                        print("Friday:",Regimen[1]['Fri'],"\nSaturday:",Regimen[1]['Sat'],"\nSunday:",Regimen[1]['Sun'])
                        break
                    elif Sel==2:
                        T.sleep(0.5)
                        print("Monday:",Regimen[2]['Mon'],"\nTuesday:",Regimen[2]['Tue'],"\nWednesday:",Regimen[2]['Wed'],"\nThursday:",Regimen[2]['Thu'])
                        print("Friday:",Regimen[2]['Fri'],"\nSaturday:",Regimen[2]['Sat'],"\nSunday:",Regimen[2]['Sun'])
                        break
                    elif Sel==3:
                        T.sleep(0.5)
                        print("Monday:",Regimen[3]['Mon'],"\nTuesday:",Regimen[3]['Tue'],"\nWednesday:",Regimen[3]['Wed'],"\nThursday:",Regimen[3]['Thu'])
                        print("Friday:",Regimen[3]['Fri'],"\nSaturday:",Regimen[3]['Sat'],"\nSunday:",Regimen[3]['Sun'])
                        break
                    elif Sel==4:
                        T.sleep(0.5)
                        print("Monday:",Regimen[4]['Mon'],"\nTuesday:",Regimen[4]['Tue'],"\nWednesday:",Regimen[4]['Wed'],"\nThursday:",Regimen[4]['Thu'])
                        print("Friday:",Regimen[4]['Fri'],"\nSaturday:",Regimen[4]['Sat'],"\nSunday:",Regimen[4]['Sun'])
                        break
                    elif Sel==5:
                        try:
                            T.sleep(0.5)
                            Reg_Name=input("Please enter the name of regimen:")
                            print("Monday:",Regimen[Reg_Name]['Mon'],"\nTuesday:",Regimen[Reg_Name]['Tue'],"\nWednesday:",Regimen[Reg_Name]['Wed'],"\nThursday:",Regimen[Reg_Name]['Thu'])
                            print("Friday:",Regimen[Reg_Name]['Fri'],"\nSaturday:",Regimen[Reg_Name]['Sat'],"\nSunday:",Regimen[Reg_Name]['Sun'])
                            break
                        except: print("Please enter correct regimen name.")
                    elif Sel==0:
                        T.sleep(0.5)
                        break
                    else:print("Please select the appropriate option.")
                except: print("Please select appropriate option.")
        except: print("Unknown error ocurred.Please try again.")

    def Delete_Regimen(self):
        T.sleep(0.5)
        try:
            while True:
                print("Below is the list of all regimens:")
                c=1
                for i in Regimen.keys():
                    if i==1:
                        print(c,":BMI<18.5")
                    elif i==2:
                        print(c,":18.5<BMI<25")
                    elif i==3:
                        print(c,":25<BMI<30")
                    elif i==4:
                        print(c,":30<BMI")
                    else: print(c,":",i)
                    c+=1
                Reg_name=input("You can't delete default regimens.\nPlease enter the name of regimen you want to delete or select 0 to go back:\n")
                try:
                    if Reg_name=='1' or Reg_name=='2' or Reg_name=='3' or Reg_name=='4'or Reg_name=='BMI<18.5' or Reg_name=='18.5<BMI<25' or Reg_name=='25<BMI<30' or Reg_name=='30<BMI':
                        print("As per regulations, You cant delete default regimens.")
                    elif Reg_name == '0':
                        break
                    else:
                        del Regimen[Reg_name]
                        T.sleep(0.7)
                        for i,j in Users.items():
                            try:
                                j.Regimen=Regimen[Regimen_Data[i]]
                            except:
                                if j.BMI<18.5:
                                    j.Regimen=Regimen[1]
                                    Regimen_Data[i]=1
                                elif 18.5<j.BMI<25:
                                    j.Regimen=Regimen[2]
                                    Regimen_Data[i]=2
                                elif 25<j.BMI<30:
                                    j.Regimen=Regimen[3]
                                    Regimen_Data[i]=3
                                elif 30<j.BMI:
                                    j.Regimen=Regimen[4]
                                    Regimen_Data[i]=4
                                print(j.Name,'is assignd with default regimen with respect to his BMI')
                        print(Reg_name,"is deleted successfully.")
                        break
                except: print("The regimen does not exist.Please enter correct name of regimen.")
        except: print("Unknown error ocurred.Please try again.")

    def Update_Regimen(self):
        try:
            while True:
                print("Below is the list of all regimens:")
                c=1
                for i in Regimen.keys():
                    if i==1:
                        print(c,":BMI<18.5")
                    elif i==2:
                        print(c,":18.5<BMI<25")
                    elif i==3:
                        print(c,":25<BMI<30")
                    elif i==4:
                        print(c,":30<BMI")
                    else: print(c,":",i)
                    c+=1
                try:
                    Sel=int(input("Please select the regime:\nSelect 1 to 4 for default\n5 for Others\nSelect 0 to go back\n"))
                    if Sel==1:
                        T.sleep(0.5)
                        Regimen[1]['Mon']=input("Please enter the exercise for Monday:")
                        Regimen[1]['Tue']=input("Please enter the exercise for Tuesday:")
                        Regimen[1]['Wed']=input("Please enter the exercise for Wednesday:")
                        Regimen[1]['Thu']=input("Please enter the exercise for Thursday:")
                        Regimen[1]['Fri']=input("Please enter the exercise for Friday:")
                        Regimen[1]['Sat']=input("Please enter the exercise for Saturday:")
                        Regimen[1]['Sun']=input("Please enter the exercise for Sunday:")
                        print("Regimen for BMI<18.5 is successfully updated.")
                        break
                    elif Sel==2:
                        T.sleep(0.5)
                        Regimen[2]['Mon']=input("Please enter the exercise for Monday:")
                        Regimen[2]['Tue']=input("Please enter the exercise for Tuesday:")
                        Regimen[2]['Wed']=input("Please enter the exercise for Wednesday:")
                        Regimen[2]['Thu']=input("Please enter the exercise for Thursday:")
                        Regimen[2]['Fri']=input("Please enter the exercise for Friday:")
                        Regimen[2]['Sat']=input("Please enter the exercise for Saturday:")
                        Regimen[2]['Sun']=input("Please enter the exercise for Sunday:")
                        print("Regimen for 18.5<BMI<25 is successfully updated.")
                        break
                    elif Sel==3:
                        T.sleep(0.5)
                        Regimen[3]['Mon']=input("Please enter the exercise for Monday:")
                        Regimen[3]['Tue']=input("Please enter the exercise for Tuesday:")
                        Regimen[3]['Wed']=input("Please enter the exercise for Wednesday:")
                        Regimen[3]['Thu']=input("Please enter the exercise for Thursday:")
                        Regimen[3]['Fri']=input("Please enter the exercise for Friday:")
                        Regimen[3]['Sat']=input("Please enter the exercise for Saturday:")
                        Regimen[3]['Sun']=input("Please enter the exercise for Sunday:")
                        print("Regimen for 25<BMI<30 is successfully updated.")
                        break
                    elif Sel==4:
                        T.sleep(0.5)
                        Regimen[4]['Mon']=input("Please enter the exercise for Monday:")
                        Regimen[4]['Tue']=input("Please enter the exercise for Tuesday:")
                        Regimen[4]['Wed']=input("Please enter the exercise for Wednesday:")
                        Regimen[4]['Thu']=input("Please enter the exercise for Thursday:")
                        Regimen[4]['Fri']=input("Please enter the exercise for Friday:")
                        Regimen[4]['Sat']=input("Please enter the exercise for Saturday:")
                        Regimen[4]['Sun']=input("Please enter the exercise for Sunday:")
                        print("Regimen for 30<BMI is successfully updated.")
                        break
                    elif Sel==5:
                        try:
                            T.sleep(0.5)
                            Reg_Name=input("Please enter the name of regimen:")
                            T.sleep(0.2)
                            Regimen[Reg_Name]['Mon']=input("Please enter the exercise for Monday:")
                            Regimen[Reg_Name]['Tue']=input("Please enter the exercise for Tuesday:")
                            Regimen[Reg_Name]['Wed']=input("Please enter the exercise for Wednesday:")
                            Regimen[Reg_Name]['Thu']=input("Please enter the exercise for Thursday:")
                            Regimen[Reg_Name]['Fri']=input("Please enter the exercise for Friday:")
                            Regimen[Reg_Name]['Sat']=input("Please enter the exercise for Saturday:")
                            Regimen[Reg_Name]['Sun']=input("Please enter the exercise for Sunday:")
                            T.sleep(0.6)
                            print("Regimen for",Reg_Name,"is successfully updated.")
                            break
                        except: print("Please enter correct regimen name.")
                    elif Sel==0:
                        T.sleep(0.7)
                        break
                    else:print("Please select the appropriate option.")
                    for i,j in Users.items():
                        j.Regimen=Regimen[Regimen_Data[i]]
                except: print("Please select appropriate option.")
        except: print("Unknown error ocurred.Please try again.")

    def Assign_Regimen(self):
        try:
            Num=input("Please enter the number of member:")
            T.sleep(0.5)
            if Num in Users:
                print("Below is the list of all regimens:")
                c=1
                for i in Regimen.keys():
                    if i==1:
                        print(c,":BMI<18.5")
                    elif i==2:
                        print(c,":18.5<BMI<25")
                    elif i==3:
                        print(c,":25<BMI<30")
                    elif i==4:
                        print(c,":30<BMI")
                    else: print(c,":",i)
                    c+=1
                Reg=input("Please enter the name of regime:")
                if Reg=='BMI<18.5':
                    Users[Num].Regimen=Regimen[1]
                    Regimen_Data[Users[Num].Num]=1
                    T.sleep(0.5)
                    print(Reg,"is successfully assigned to",Users[Num].Name)
                elif Reg == '18.5<BMI<25':
                    Users[Num].Regimen=Regimen[2]
                    Regimen_Data[Users[Num].Num]=2
                    T.sleep(0.5)
                    print(Reg,"is successfully assigned to",Users[Num].Name)
                elif Reg == '25<BMI<30':
                    Users[Num].Regimen=Regimen[3]
                    Regimen_Data[Users[Num].Num]=3
                    T.sleep(0.5)
                    print(Reg,"is successfully assigned to",Users[Num].Name)
                elif Reg == '30<BMI':
                    Users[Num].Regimen=Regimen[4]
                    Regimen_Data[Users[Num].Num]=4
                    T.sleep(0.5)
                    print(Reg,"is successfully assigned to",Users[Num].Name)
                else:
                    try:
                        Users[Num].Regimen=Regimen[Reg]
                        Regimen_Data[Users[Num].Num] =Reg
                        T.sleep(0.7)
                        print(Reg,"is successfully assigned to",Users[Num].Name)
                    except: print(" You might have entered wrong regimen name.Please try again.")
            else: print("You have entered wrong number.Please try again.")
        except: print("Unknown error ocurred.Please try again.")
            

class user:
    def __init__(self,Name,Age,Gen,Num,Email,BMI,MemDur):
        self.Name=Name
        self.Age=Age
        self.Gen=Gen
        self.Num=Num
        self.Email=Email
        self.BMI=BMI
        self.MemDur=MemDur
        Users[self.Num]=self
        if self.BMI<18.5:
            self.Regimen=Regimen[1]
            Regimen_Data[self.Num]=1
        elif 18.5<self.BMI<25:
            self.Regimen=Regimen[2]
            Regimen_Data[self.Num]=2
        elif 25<self.BMI<30:
            self.Regimen=Regimen[3]
            Regimen_Data[self.Num]=3
        else:
            self.Regimen=Regimen[4]
            Regimen_Data[self.Num]=4
        print("New GYM member",self.Name,'is successfully enrolled for',self.MemDur,'months.')
        if self.BMI<18.5:
              print("Regimen is assigned for 'BMI<18.5'.")
        elif 18.5<self.BMI<25:
              print("Regimen is assigned for '18.5<BMI<25'.")
        elif 25<self.BMI<30:
              print("Regimen is assigned for '25<BMI<30'.")
        else: print("Regimen is assigned for '30<BMI'.")
        
    def Print_Regimen(self):
        print("Monday:",self.Regimen['Mon'],"\nTuesday:",self.Regimen['Tue'],"\nWednesday:",self.Regimen['Wed'],"\nThursday:",self.Regimen['Thu'])
        print("Friday:",self.Regimen['Fri'],"\nSaturday:",self.Regimen['Sat'],"\nSunday:",self.Regimen['Sun'])
        
    def Update_Membership(self):
        try:
            Sel=int(input("Please select the operation:\n1.Update the Membership\n2.Revoke membership\nSelect 0 to quit\n"))
            try: 
                while True:
                    if Sel == 1:
                        try:
                            while True:
                                Dur=int(input("Please select the extended duration from(1,3,6,12).\n"))
                                if Dur==1 or Dur==3 or Dur==6 or Dur==12:
                                    self.MemDur=Dur
                                    print("Updated duration is",self.MemDur,".")
                                    break
                                else: print("Please select the appropriate duration.")
                        except: print("Please enter appropriate duration.")              
                        break
                    elif Sel==2:
                        self.MemDur=0
                        print("Mebership of",self.Name,"is revoked.")
                        break
                    elif Sel == 0:
                        break
                    else:print("Please select appropriate operation.")
            except: print("Please select appropriate operation.")
        except: print("Unknown error ocurred.Please try again.")

    def Show_Profile(self):
        T.sleep(0.6)
        print("\nName:",self.Name,"\nAge:",self.Age,"\t\t\tGender:",self.Gen,"\tMobile Number:",self.Num,"\nEmail:",self.Email,"\tBMI:",self.BMI)
        if Regimen_Data[self.Num] == 1:
            print("Assigned regimen:18.5<BMI")
        elif Regimen_Data[self.Num] == 2:
            print("Assigned regimen:18.5<BMI<25")
        elif Regimen_Data[self.Num] == 3:
            print("Assigned regimen:25<BMI<30")
        elif Regimen_Data[self.Num] == 4:
            print("Assigned regimen:30<BMI")
        else:
            print("Assigned regimen:",Regimen_Data[self.Num])
        if self.MemDur == 0:
            print("Your membership is revoked.Please contact Gym authority.")
        else:
            print("Membership duration:",self.MemDur)
            
    def Update_Name(self):
        T.sleep(0.3)
        Name=input("Please enter new name:\n")
        self.Name=Name
        T.sleep(0.5)
        print("Name is updated.")
        
    def Update_Age(self):
        T.sleep(0.3)
        Age=input("Please enter new age:\n")
        self.Age=Age
        T.sleep(0.5)
        print("Age is updated.")
        
    def Update_Gender(self):
        T.sleep(0.3)
        Gen=input("Please enter the gender:\n")
        self.Gen=Gen
        T.sleep(0.5)
        print("Name is updated.")    
        
    def Update_Num(self):
        T.sleep(0.3)
        Num=input("Please enter new number:\n")
        self.Num=Num
        Users[self.Num]=self
        T.sleep(0.5)
        print("Contact number is updated.")
        
    def Update_Email(self):
        T.sleep(0.3)
        while True:
            Email=input("Please enter new email:\n")
            if (re.search(regex,Email)):
                email=Email.lower()
                break
            else: print("Please enter valid email ID!")
            self.Email=email
            T.sleep(0.5)
            print("Email is updated.")
        
    def Update_BMI(self):
        T.sleep(0.3)
        BMI=int(input("Please enter new BMI:\n"))
        self.BMI=BMI
        if self.BMI<18.5:
            self.Regimen=Regimen[1]
            Regimen_Data[self.Num]=1
        elif 18.5<self.BMI<25:
            self.Regimen=Regimen[2]
            Regimen_Data[self.Num]=2
        elif 25<self.BMI<30:
            self.Regimen=Regimen[3]
            Regimen_Data[self.Num]=3
        else:
            self.Regimen=Regimen[4]
            Regimen_Data[self.Num]=4
        T.sleep(0.5)
        print("BMI is updated.")
        
        
SuperUser=superuser()


print("***Helloo!!!Weclome to GYM membership application***")
T.sleep(0.7)
try:
    while True:
        T.sleep(0.5)
        Role=int(input("\nPlease select the role:\n1.SuperUser\t\t2.Gym Member\nPress 0 to quit.\n"))
        if Role==1:
            while True:
                T.sleep(0.6)
                Sel=int(input("\nPlease select the operation:\n1.Create Member\t\t2.View Member\n3.Delete Member\t\t4.Update Member\n5.Create Regimen\t6.View Regimen\n7.Delete Regimen\t8.Update Regimen\n9.Assign regimen\nSelect 0 to quit.\n"))
                if Sel == 1:
                    T.sleep(0.5)
                    SuperUser.Create_Member()
                elif Sel == 2:
                    T.sleep(0.5)
                    SuperUser.View_Member()
                elif Sel == 3:
                    T.sleep(0.5)
                    SuperUser.Delete_Member()
                elif Sel == 4:
                    T.sleep(0.5)
                    SuperUser.Update_Member()
                elif Sel == 5:
                    T.sleep(0.5)
                    SuperUser.Create_Regimen()
                elif Sel == 6:
                    T.sleep(0.5)
                    SuperUser.View_Regimen()
                elif Sel == 7:
                    T.sleep(0.5)
                    SuperUser.Delete_Regimen()
                elif Sel == 8:
                    T.sleep(0.5)
                    SuperUser.Update_Regimen()
                elif Sel == 9:
                    T.sleep(0.5)
                    SuperUser.Assign_Regimen()
                elif Sel == 0:
                    T.sleep(0.5)
                    break
                else:
                    T.sleep(0.6)
                    print("Please select the appropriate option.")
        elif Role == 2:
            while True:
                T.sleep(0.5)
                Number=input("\nPlease enter your contact number to login or enter 0 to go back:\n")
                if Number in Users:
                    T.sleep(0.5)
                    while True:
                        Sel=int(input("\nPlease select the operation:\n1.My Regimen\t\t2.My Profile\nSelect 0 to go back\n"))
                        if Sel == 1:
                            T.sleep(0.5)
                            Users[Number].Print_Regimen()
                        elif Sel == 2:
                            T.sleep(0.6)
                            Users[Number].Show_Profile()
                        elif Sel == 0:
                            break
                        else:
                            T.sleep(0.5)
                            print("Please select appropriate option.")
                elif Number == '0':
                    T.sleep(0.6)
                    break
                else: print("Please enter correct number.")
        elif Role ==0:
            T.sleep(0.5)
            break
        else:
            T.sleep(0.3)
            print("Please select appropriate option!!")
except: print("Unknown error ocurred.Please try again.")