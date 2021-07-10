#!/usr/bin/env python
# coding: utf-8

# # Hotel room booking service 
# # This is a simple yet basic python programme to book a room in a hotel 
# # There are some limitations  in the prrogrramme 
# # 1)did not use the data base for the programme 
# 
#       
#   
# 

# # Here mostly we used functions with all afforts tried to put it as simple and clear 

# In[ ]:


#  project : hotel room booking services
import random #which is used for functions :
import datetime # used to import the time
from functools import reduce

#declarations using global keyword to use the list completely.
name=[]
phonenumber=[]
address=[]
check_in=[]
check_out=[]
room=[]
price=[]
room_no=[]
customer_id=[]
day=[]
bill=[]
rm_no=[]
c_id=[]
m=0
i=0
#global varaibles for using with all functions
a=0
Totatrooms=20



#printing the basic information of the basic before booking the hotel

print("************ WELCOME***********")
print("Thank you Choosing Us","*Its Pleasure to Serve you*")
print("We Promice you that ,The Stay in our Hotel gives You u memorable day")

def Hotel():
    print("\t****Welcome to ***Tree House Stay****\n")
    print("\t\t\tFor Rooms Info give 1 \n")
    print("\t\t\tFor Amminities info give 2\n")
    print("\t\t\tFor Bookings give 3\n")
    print("\t\t\tFor Restaurant Info give 4 \n")
    print("\t\t\tFor  payment 5\n")

    info=int(input(">>>>>>>>>---------"))
    if info==1:
        print("Basic Details of Hotel")
        Room_info()

    elif info==2:
        print("Room Info")
        amminities_info()
    elif info==3:
        print("Room Booking")
        Booking_room()
    elif  info==4:
        print("Restaurant information")
        restaurant()
    elif  info==5:
        print("Payment")
        payment()
    else:
        exit()
def Room_info():
    print(">>>>>>>>>Hotel information<<<<<<<<<")
    print("We provide free wifi,24/7 security")
    print("----SELECT ROOM TYPE----")
    print(" 1. Standard Non-AC")
    print(" 2. Standard AC")
    print(" 3. 3-Bed Non-AC")
    print(" 4. 3-Bed AC")
    print(("\t\tPress 0 for Room Prices"))
          
    ch=int(input("->"))          
        # if-conditions to display alloted room
        # type and it's price
    if ch==0:
            print(" 1. Standard Non-AC - Rs. 3500")
            print(" 2. Standard AC - Rs. 4000")
            print(" 3. 3-Bed Non-AC - Rs. 4500")
            print(" 4. 3-Bed AC - Rs. 5000")
            ch=int(input("->"))
    if ch==1:
            room.append('Standard Non-AC')
            print("Room Type- Standard Non-AC")  
            price.append(3500)
            print("Price- 3500")
    elif ch==2:
            room.append('Standard AC')
            print("Room Type- Standard AC")
            price.append(4000)
            print("Price- 4000")
    elif ch==3:
            room.append('3-Bed Non-AC')
            print("Room Type- 3-Bed Non-AC")
            price.append(4500)
            print("Price- 4500")
    elif ch==4:
            room.append('3-Bed AC')
            print("Room Type- 3-Bed AC")
            price.append(5000)
            print("Price- 5000")
    else:
            print(" Wrong choice..!!")
            
    
    print("to contiinue for bookings ")
    m=int(input("give *** 1 for future proceddings **0 for exit"))
    if m==1:
        amminities_info()
    elif m==0:
        exit()
    else:
        print("wrong input")
        
  
def amminities_info():#amminities of room check it before we book room 
    print("         ------ HOTEL ROOMS INFO ------")
    print("")
    print(">>>>>>>>>Hotel information<<<<<<<<<")
    print("We provide free wifi,24/7 security")
    print(" Press . 1) STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print(" Press . 2)STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print(" Press . 3) 3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("Press . 4) 3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print("To continue bookings give  **1")
    n=int(input("0-BACK\n -> ** 1 for bookings"))
   
    if n==0:
         Hotel()
    elif n==1:
        Booking_room()
        exit()
def Booking_room():
      
        # used global keyword to 
        # use global variable 'i'
        global i
        print(" BOOKING ROOMS")
        print(" ")
          
        while 1:
            n = str(input("Name: "))
            p1 = str(input("Phone No.: "))
            a = str(input("Address: "))
             
            # checks if any field is not empty
            if n!="" and p1!="" and a!="":
                name.append(n)
                address.append(a)
                break
                  
            else:
                 print("\tName, Phone no. & Address cannot be empty..!!")
               
        cii=str(input("Check-In:   date must be in  date/month/year"))
        check_in.append(cii)
        cii=cii.split('/')
        ci=cii
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        date(ci)
           
        coo=str(input("Check-Out: "))
        check_out.append(coo)
        coo=coo.split('/')
        co=coo
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])
      
           
       
        # randomly generating room no. and customer 
        # id for customer
        rn = random.randrange(40)+300
        cid = random.randrange(40)+10
          
          
        # checks if alloted room no. & customer 
        # id already not alloted
        while rn in room_no or cid in customer_id:
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
              
       
      
        print("")
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
        print("Room No. - ",rn)
        print("Customer Id - ",cid)
        room_no.append(rn)
        customer_id.append(cid)
        i=i+1
        #for every room booked the total rooms  should decrease
        #Total_no_of_rooms=20
        
        n=int(input("0-BACK\n -"))
        if n==0:
            Hotel() 
        else:
            exit()

  
def restaurant():
            print("-------------------------------------------------------------------------")
            print("                           Hotel AnCasa")
            print("-------------------------------------------------------------------------")
            print("                            Menu Card")
            print("-------------------------------------------------------------------------")
            print("\n BEVARAGES                              26 Dal Fry................ 140.00")
            print("----------------------------------      27 Dal Makhani............ 150.00")
            print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00")
            print(" 2  Masala Tea.............. 25.00")
            print(" 3  Coffee.................. 25.00      ROTI")
            print(" 4  Cold Drink.............. 25.00     ----------------------------------")
            print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00")
            print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00")
            print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00")
            print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00")
            print(" 9  Cheese Toast Sandwich... 70.00")
            print(" 10 Grilled Sandwich........ 70.00      RICE") 
            print("                                       ----------------------------------")
            print(" SOUPS                                  33 Plain Rice.............. 90.00")
            print("----------------------------------      34 Jeera Rice.............. 90.00")
            print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00")
            print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00")
            print(" 13 Veg. Noodle Soup....... 110.00")
            print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN")
            print(" 15 Veg. Munchow........... 110.00     ----------------------------------")
            print("                                        37 Plain Dosa............. 100.00")
            print(" MAIN COURSE                            38 Onion Dosa............. 110.00")
            print("----------------------------------      39 Masala Dosa............ 130.00")
            print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00")
            print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00")
            print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00")
            print(" 19 Palak Paneer........... 120.00")
            print(" 20 Chilli Paneer.......... 140.00      ICE CREAM")
            print(" 21 Matar Mushroom......... 140.00     ----------------------------------")
            print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00")
            print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00")
            print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00")
            print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")
            
            #print("enter the number which u want to order")
        
            #list =int(input("enter the number which you want to order: "))
            def menu_final():
            
             list =int(input("enter the number which you want to order: "))
             if list==1:
                 bill.append(20)
             elif list==2:
                bill.append(25)
             elif list==3:
                #a3=25
                bill.append(25)
             elif list==4:
                #a4=25
                bill.append(25)
             elif list==5:
                #a5=25
                bill.append(25)
             elif list==6:
                #a6=30
                bill.append(30)
             elif list==7:
                #a7=30
                bill.append(30)
             elif list==8:
                #a8=50
                bill.append(50)
             elif list==9:
                #a9=50
                bill.append(50)
             elif list==10:
                #a10=70
                bill.append(70)
             elif list==11:
                 bill.append(80)
             elif list==12:
                #a12=70
                bill.append(70)
             elif list==13:
                #a13=110
                bill.append(110)
             elif list==14:
                #a14=125
                bill.append(125)
             elif list==15:
                #a15=130
                bill.append(130)
             elif list==16:
                #a16=130
                bill.append(130)
             elif list==17:
                #a17=50
                bill.append(50)
             elif list==18:
                #a18=170
                bill.append(170)
             elif list==19:
                #a19=125
                bill.append(125)
             elif list==20:
                #a20=250
                bill.append(250)
             elif list==21:
                #a21=250
                bill.append(250)
             elif list==22:
                #a22=250
                bill.append(250)
             elif list==23:
                #a23=130
                bill.append(130)
             elif list==24:
                #a24=130
                bill.append(130)
             elif list==25:
                #a25=150
                bill.append(150)
             elif list==26:
                #a26=120
                bill.append(120)
             elif list==27:
                #a27=125
                bill.append(125)
             elif list==28:
                #a28=125
                bill.append(125)
             elif list==29:
                #a29=125
                bill.append(125)
             elif list==30:
                #a30=125
                bill.append(125)
             elif list==31:
                #a31=130
                bill.append(130)
             elif list==32:
                #a32=130
                bill.append(130)
             elif list==33:
                #a33=150
                bill.append(150)
             elif list==34:
                #a34=100
                bill.append(100)
             elif list==35:
                #a35=125
                bill.append(125)
             elif list==36:
                #a36=100
                bill.append(100)
             elif list==37:
                #a37=150
                bill.append(150)
             elif list==38:
                #a38=110
                bill.append(110)
             elif list==39:
                #a34=130
                bill.append(130)
             elif list==40:
                #a40=130
                bill.append(130)
             elif list==41:
                #a41=130
                bill.append(130)
             elif list==42:
                #a42=140
                bill.append(140)
             elif list==43:
                #a43=60
                bill.append(60)
             elif list==44:
                #a44=60
                bill.append(60)
             elif list==45:
                #a45=60
                bill.append(60)
             elif list==46:
                #a46=60
                bill.append(60)
          
             else:
                print("wrong number")
             print(bill)    
             n=int(input("if u still want to continue to order * press 1**"))
             if n==1:
                 menu_final()
             else:
                 print(" thank you ")
                
            
           
            n=int(input("if you want to order food press ***1"))
            if n==1:
                menu_final()
            else:
                print(" thank you ")
                
            print(bill)  
            amount =reduce(lambda x,y:x+y,bill)
            print(amount)
            m=int(input("enter **0 to go Home "))
            if m==0:
             Hotel()
            else:
             exit()
def payment():
            phonenumber=str(input("Phone Number: "))
            global i
            f=0
            for n in range(0,i):
                if ph==phonenumber[n]:
                    if p[n]==0:
                        f=1
                        print(" Payment")
                        print(" --------------------------------")
                        print("  MODE OF PAYMENT")
                   
                        print("  1- Credit/Debit Card")
                        print("  2- Paytm/PhonePe")
                        print("  3- Using UPI")
                        print("  4- Cash")
                        x=int(input("-> "))
                        print("\n  Amount: ",(price[n]*d[n])+amount[n])
                        print("\n            Pay For The tree house")
                        print("  (y/n)")
                        ch=str(input("->"))
                  
                        if ch=='y' or ch=='n':
                            print("\n\n --------------------------------")
                            print("           Hotel The tree house")
                            print(" --------------------------------")
                            print("              Bill")
                            print(" --------------------------------")
                            print(" Name: ",name[n],"\t\n Phone No.: ",phonenumber[n],"\t\n Address: ",address[n],"\t")
                            print("\n Check-In: ",check_in[n],"\t\n Check-Out: ",check_out[n],"\t")
                            print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*d[n],"\t") 
                            print(" Restaurant Charges: \t",amount[n])
                            print(" --------------------------------")
                            print("\n Total Amount: ",(price[n]*d[n])+amount[n],"\t")
                            print(" --------------------------------")
                            print("          Thank You")
                            print("          Visit Again :)")
                            print(" --------------------------------\n")
                            p.pop(n)
                            p.insert(n,1)
                      
                    # pops room no. and customer id from list and 
                    # later assigns zero at same position
                            roomno.pop(n)
                            custid.pop(n)
                            roomno.insert(n,0)
                            custid.insert(n,0)
                      
                        else:
                            for j in range(n+1,i):
                              if ph==phonenumber[j] :
                                if p[j]==0:
                                    pass
                          
                                else:
                                    f=1
                                    print("\n\tPayment has been Made :)\n\n")
           
            #for every room booking the total rooms number should decrease 
            Total_no_of_rooms=20-1
            Totalrooms.append(T0tal_no_of_rooms)
            print(Totalrooms)
            if Totalrooms==0:
                print("rooms finished")
            else:
                pass
            if f==0: 
                 print("Invalid Customer Id")
            n = int(input("0-BACK\n ->"))
            if n == 0:
              Hotel()
            else:
              exit()
  

        
         
          
                
                
                
           
   

         


        
         
         ###def date ():
           
def date(c):
     if c[2] >=2021  and c[2] <= 2022:
         if c[1] != 0 and c[1] <= 12:
              
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                  
                if c[2]%4 == 0 and c[0] <= 29:
                    pass
                  
                elif c[0]<29:
                    pass
                  
                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phno.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()
              
              
            # if month is odd & less than equal 
            # to 7th  month 
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                pass
              
            # if month is even & less than equal to 7th
            # month and not 2nd month
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                pass
              
            # if month is even & greater than equal 
            # to 8th  month
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                pass
              
            # if month is odd & greater than equal
            # to 8th  month
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:  
                pass
              
            else: 
                print("Invalid date\n")
                name.pop(i)
                phno.pop(i)
                add.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                Booking()
                  
         else:
               print("Invalid date\n")
               name.pop(i)
               phno.pop(i)
               add.pop(i)
               checkin.pop(i)
               checkout.pop(i)
               Booking()
              
     else:
         print("Invalid date\n")
         name.pop(i)
         phno.pop(i)
         add.pop(i)
         checkin.pop(i)
         checkout.pop(i)
         Booking()

Hotel()

