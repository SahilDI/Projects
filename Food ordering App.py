from random import randint, randrange
import time as T
import re
regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
regex_2= "\S*(\S*([a-zA-Z]\S*[0-9])|([0-9]\S*[a-zA-Z]))\S*"
regex_3="[@_!#$%^&*()<>?/|}{~:]"
FOOD_ID=[]
Food_list={}
Food_Obj={}
Admin_Data={}
Admin_Obj={}
User_obj={}
Order_Hist={}
User_Data={}

class food:
    def __init__(self,Name,Quantity,Price,Discount,Stock):
        self.Name=Name
        self.Quantity=Quantity
        self.Price=Price
        self.Discount=Discount
        self.Stock=Stock
        FoodID =randint(1000,99999)
        if FoodID in FOOD_ID is True :
            New_ID=randint(1000,99999)
            self.Food_ID=New_ID
        else:
            self.Food_ID=FoodID
        FOOD_ID.append(self.Food_ID)
        Food_Obj[self.Food_ID]=self
        Food_list[self.Food_ID]=[self.Name,self.Quantity,self.Price,self.Discount,self.Stock]
        print("New food",self.Name,"is successfully added with id",self.Food_ID,'\n')
        
    def update_Name(self):
        try:
            New_name=input("Please enter the new name:\n")
            self.Name=New_name
            Food_list[self.Food_ID][0]=New_name
            print("Food name has been changed as",self.Name)
        except:
            print("Error occurred!!Please try again!!")
    
    def update_Quantity(self):
        try:
            New_Q=input("Please enter the updated quantity in gm/pcs/ltr:\n")
            self.Quantity=New_Q
            Food_list[self.Food_ID][1]=New_Q
            print("Food quantity has been changed as",self.Quantity)
        except:
            print("Error occurred!!Please try again!!")
    
    def update_Price(self):
        New_P=input("Please enter the updated price in Rs:\n")
        self.Price=New_P
        Food_list[self.Food_ID][2]=New_P
        print("Food price has been changed as",self.Price)
        
    def update_Discount(self):
        New_D=input("Please enter the updated discount in %:\n")
        self.Discount=New_D
        Food_list[self.Food_ID][3]=New_D
        print("Discount has been changed as",self.Discount)
        
    def update_Stock(self):
        try:
            New_S=input("Please enter the updated stock of item:\n")
            self.Stock=New_S
            Food_list[self.Food_ID][4]=New_S
            print("Food stock has been changed as",self.Stock)
        except:
            print("Error occurred!!Please try again!!")
        
    def food_delivered(self):
        try:
            if Food_list[self.Food_ID][4] !=0:
                Food_list[self.Food_ID][4]-=1
                print("Order of",Food_list[self.Food_ID][0],"is confirmed.")
                return True
            else:
                print("\n",Food_list[self.Food_ID][0],"is not available at this moment!!Please try again later!!")
        except:
            print("Error occurred!!Please try again!!")
            
    
class admin:
    def __init__(self,LogID,PassWord):
        loginid=LogID.lower()
        self.LoginID=loginid
        self.PassWord=PassWord
        Admin_Data[self.LoginID]=self.PassWord
        Admin_Obj[self.LoginID]=self
        
    def Update_food(self):
        while True:
            try:
                sel=int(input("\nPlease select which parameter you want to update: \n1.Food name \n2.Food quantity \n3.Food price \n4.Discount on food \n5.Stock of food \n0.Quit\n"))
                if sel == 1:
                    T.sleep(0.5)
                    ID=int(input("Please enter the ID of the food which needs to be updated:\n"))
                    Food_Obj[ID].update_Name()
                elif sel == 2:
                    T.sleep(0.5)
                    ID=int(input("Please enter the ID of the food which needs to be updated:\n"))
                    Food_Obj[ID].update_Quantity()
                elif sel == 3:
                    T.sleep(0.5)
                    ID=int(input("Please enter the ID of the food which needs to be updated:\n"))
                    Food_Obj[ID].update_Price()
                elif sel == 4:
                    T.sleep(0.5)
                    ID=int(input("Please enter the ID of the food which needs to be updated:\n"))
                    Food_Obj[ID].update_Discount()
                elif sel == 5:
                    T.sleep(0.5)
                    ID=int(input("Please enter the ID of the food which needs to be updated:\n"))
                    Food_Obj[ID].update_Stock()
                elif sel == 0:
                    T.sleep(0.5)
                    break
                else:
                    T.sleep(0.5)
                    print("Please select appropriate option!!")
            except:
                T.sleep(0.6)
                print("Error occurred.Please try again!!\n")
                    
    def Add_item(self):
        try:
            Name=input("\nPlease enter the name of dish:")
            Qaun=input("Please enter the quantity of food in gm/ltr/pcs:")
            Price=input("Please enter the price in RS.:")
            Disc=input("Please enter the discount provided on food item in %:")
            Stock=int(input("Please enter the available stock of food item:"))
            Name=food(Name,Qaun,Price,Disc,Stock)
        except:
            print("Please enter appropriate values!")
            
    def View_items(self):
        try:
            if len(Food_list) == 0:
                print("\nThere are currently no food item available. Please add some food items!!")
            else:
                for i,j in Food_list.items():
                    print('Id of dish',i,':\n\tDish name:',j[0],'\n\tquantity of food:',j[1],'\n\tPrice of food:',j[2],'\n\tDiccount on food:',j[3],'\n\tAvailable stock of food:',j[4])
        except:
            print("Error occurred!!Please try again!!")
    
    def Delete_items(self):
        try:
            if len(Food_list)!=0:
                ID=int(input("Please enter the ID of item you wish to delete:\n"))
                if ID in Food_list:
                    del Food_list[ID]
                    del Food_Obj[ID]
                    print("Food item with id",ID,"is deleted.\n")
                else:
                    print("Food with id",ID,"does not exist.Please try again.\n")
            else:
                print("\nCurrently there is no food item stored.\n")
        except:
            print("Error")
            
Admin=admin('Admin','Admin')
        

class user:
    def __init__(self,Name,ConNum,Email,Add,Pass):
        self.Name=Name
        self.ConNum=ConNum
        email=Email.lower()
        self.Email=email
        self.Add=Add
        self.Pass=Pass
        self.History=[]
        User_obj[self.Email]=self
        User_Data[self.Email]=self.Pass
        print("\nCongatulations!!\nYou have succesfully registered yourself!!\nPlease visit login page!!")
        
    def Update_profile(self):
        while True:
            try:
                sel=int(input("\nPlease select the option which needs to be updated:\n1.Name\t2.Contact number\t3.Email address\n4.Residential address\t5.Password\t0.quit\n"))
                if sel == 1:
                    T.sleep(0.5)
                    Name=input("Please enter new name:")
                    self.Name=Name
                    print("Name is succesfully updated!!")
                elif sel == 2:
                    T.sleep(0.5)
                    ConNum=input("Please enter new contact number:")
                    self.ConNum=ConNum
                    print("Contact number is succesfully updated!!")
                elif sel == 3:
                    T.sleep(0.5)
                    while True:
                        Email=input("Please enter your new Email id:")
                        if (re.search(regex,Email)):
                            email=Email.lower()
                            break
                        else:
                            print("Please enter valid email ID!")
                    self.Email=email
                    User_obj[self.Email]=self
                    User_Data[self.Email]=self.Pass     
                    print("Email address is succesfully updated!!")
                elif sel == 4:
                    T.sleep(0.5)
                    Add=input("Please enter new address:")
                    self.Add=Add
                    print("Residential address is succesfully updated!!")
                elif sel == 5:
                    T.sleep(0.5)
                    while True:
                        Pass=input("Please enter new password(password must contains number,letters and speacial character eg.@,# etc):")
                        if (re.search(regex_2,Pass)) and (re.search(regex_3,Pass)):  
                            self.Pass=Pass
                            User_Data[self.Email]=self.Pass 
                            print("Password is succesfully updated!!")
                            break
                        else:
                            print("Please enter valid alpha-neumaric password")
                elif sel == 0:
                    T.sleep(0.5)
                    break
                else:
                    T.sleep(0.5)
                    print("Please select appropriate option!")
            except:
                print("Error occurred.Please try again!!\n")
    def Show_list(self):
        try:
            if len(Food_list) == 0:
                print("\nThere are currently no food item available.")
            else:
                count=1
                for i,j in Food_list.items():
                    print(count,'.',j[0],'(',j[1],')[',j[2],']')
        except:
            print("Error occurred!!Please try again!!")

    def order_food(self):
        order={}
        delivery={}
        try:
            if len(Food_list) == 0:
                print("\nThere are currently no food item available.")
            else:
                count=1
                for i,j in Food_list.items():
                    order[count]=j
                    delivery[count]=i
                    print(count,'.',j[0],'(',j[1],')[',j[2],']')
                    count+=1
                try:
                    my_list = []
         
                    while True:
                        my_list.append(int(input('Please selct the number of items you choose one by one and press 0 to complete the order:\n')))
                        if 0 in my_list:
                            break
                        print("Your order is:")
                        for i in range(len(my_list)):
                            print(order[my_list[i]][0],',',order[my_list[i]][1])
                    print("\nYour Final order is:")
                    for i in range(len(my_list)):
                        print(order[my_list[i]][0],'',order[my_list[i]][1])
                except:
                    pass
                try:
                    while True:
                        Sel= int(input("Please press 1 to confirm your order or press 0 to quit:\n"))
                        if Sel == 1:
                            for i in range(len(my_list)-1):
                                x=Food_Obj[delivery[my_list[i]]].food_delivered()
                                if x is True:
                                    self.History.append(order[my_list[i]])
                            print("\nYour order of confirmed items will be delivered shorly!!\nThank for using our service...See you soon!! ")
                            break
                        elif Sel == 0:
                            break
                        else:
                            print("Please select the appropriate option!!")
                except:
                    print("Error occurred.Please try again!!\n")
        except:
            print("Error occurred!!Please try again!!")
            
    def Show_History(self):
        try:
            if len(self.History)!=0:
                c=1
                for i in range(len(self.History)):
                    print(c,'.',self.History[i][0],',',self.History[i][1],',',self.History[i][2])
            else:
                print("\nYou have no previous history of orders!!Please order some food!")
        except:
            print("Error occurred!!Please try again!!")


print("Hii..Welcome to our online food ordering platform!!")
T.sleep(0.7)
try:
    while True:
        Role=int(input("Please select you role sir:\n1.Admin\t\t2.User\nSelect 0 to quit!\n"))
        if Role == 1:
            T.sleep(0.5)
            print("Now you are in Admin interface!!")
            while True:
                ID=input("\nHii!!Please enter your user id to login or type quit to quit:")
                PW=input("Please enter your password or type quit to quit:")
                id=ID.lower()
                if id in Admin_Data and Admin_Data[id]== PW:
                    T.sleep(0.5)
                    print("\nYou are successfully logged in into the admin system!\n")
                    try:
                        while True:
                            print("\nPlease select the operation you want perform from following list\n")
                            Sel=int(input('1.Add new food item\t\t2.Update existing food item\n3.View the list of food items\t4.Remove food item\nPlease select 0 to quit!\n'))
                            if Sel==1:
                                T.sleep(0.5)
                                Admin.Add_item()

                            elif Sel==2:
                                T.sleep(0.5)
                                Admin.Update_food()

                            elif Sel==3:
                                T.sleep(0.5)
                                Admin.View_items()

                            elif Sel==4:
                                T.sleep(0.6)
                                Admin.Delete_items()

                            elif Sel==0:
                                T.sleep(0.5)
                                break
                            else:
                                T.sleep(0.6)
                                print("Error occurred.Please try again. Sorry for inconvenience!")
                        break
                    except:
                        print("Error occurred.Please try again. Sorry for inconvenience!")
                elif id in Admin_Data and Admin_Data[id]!= PW:
                    T.sleep(0.7)
                    print("You have entered wrong password")
                elif id == 'quit' or PW == 'quit':
                    T.sleep(0.5)
                    break
                else:
                    T.sleep(0.7)
                    print("You have entered wrong id username!!")
        elif Role == 2:
            try:
                print("Now you are in user interface!")
                while True:
                    Log=int(input("\nPlease select 1 to log in if you are registered or select 2 to register yourself.\nSelect 0 to quit!\n"))
                    if Log == 2:
                        T.sleep(0.5)
                        Name=input("\nPlease enter your name:")
                        Num=input("Please enter your contact number:")
                        Add=input("Please enter your residential address:") 
                        while True:
                            Email=input("Please enter your Email id:")
                            if (re.search(regex,Email)):
                                email=Email.lower()
                                break
                            else:
                                print("Please enter valid email ID!")
                        while True:
                            Pass=input("Please enter password(password must contains number,letters and speacial character eg.@,# etc:\n")
                            if (re.search(regex_2,Pass)) and (re.search(regex_3,Pass)):  
                                Pass_2=Pass
                                break
                            else:
                                print("Please enter valid alpha-neumaric password")
                        Name=user(Name,Num,email,Add,Pass_2)
                    elif Log==1:
                        T.sleep(0.5)
                        while True:
                            Email=input("Please enter your Email id:")
                            if (re.search(regex,Email)):
                                email=Email.lower()
                                break
                            else:
                                print("\nPlease enter valid email ID!")
                        PW=input("Please enter your password:")
                        ID_2=Email.lower()
                        if ID_2 in User_Data and User_Data[ID_2]== PW:
                            T.sleep(0.5)
                            print("\nYou have successfully logged in Mr.",User_obj[ID_2].Name,"\n")
                            try:
                                while True:
                                    Sel=int(input("\nPlease select the desired operations:\n1.Place new order\t2.View the order history\n3.Update your profile\nPress 0 to quit!!\n"))
                                    if Sel == 1:
                                        T.sleep(0.5)
                                        User_obj[ID_2].order_food()
                                    elif Sel == 2:
                                        T.sleep(0.5)
                                        User_obj[ID_2].Show_History()
                                    elif Sel==3:
                                        T.sleep(0.5)
                                        User_obj[ID_2].Update_profile()
                                    elif Sel == 0:
                                        T.sleep(0.5)
                                        break
                                    else:
                                        T.sleep(0.6)
                                        print("\nPlease select the appropriate option!!\n")
                            except:
                                T.sleep(0.6)
                                print("\nError occurred.Please try again!!\n")

                        elif ID_2 in User_Data and User_Data[ID_2]!= PW:
                            T.sleep(0.6)
                            print("\nYou have entered wrong password.Please try again!")
                        else:
                            T.sleep(0.6)
                            print("\nYou have entered wrong email id or password or you are not a registered user. Please try again!")
                    elif Log == 0:
                        T.sleep(0.5)
                        break
                    else:
                        T.sleep(0.6)
                        print("\nPlease select appropriate option!!")
            except:
                print("\nError occurred.Please try again!!\n")

        elif Role == 0:
            T.sleep(0.5)
            break
        else:
            T.sleep(0.6)
            print("\nPlease select appropriate option!!\n")
except:
    T.sleep(0.7)
    print("\nError occurred.Please try again!!\n")