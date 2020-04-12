"""
Subject : Ticket Reservation system
@author: 
    18bce116 - Nihar Markana
    18bce119 - Vasu Mavani
"""

import random
import string
import datetime
from random import randint
from os import path
import smtplib

import sys

user={}
status = ""



def send_email(SUBJECT, MESSAGE,s_e,s_p,r_e):
    try: 
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(s_e,s_p)
        message = 'Subject: {}\n\n{}'.format(SUBJECT, MESSAGE)
        server.sendmail(s_e, r_e, message)
        server.quit()
        print("E-Mail sent Successfully !")
    except:
        print("Error","Cannot send Email.")


def send_email_new(subject,message,s_e,s_p,r_e):
    send_email(subject,message,s_e,s_p,r_e)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def displayMenu():
     while True:
        status = input("Press l for login/ r for register and q for quit: ")
        if(status == 'q'):
            sys.exit("Logout from session ")
        elif(status=='r'):
            newUser()
        elif(status == 'l'):
            oldUser()
        else:
            print("Enter valid input: ")
            continue
                

def newUser():
    createLogin = input("create UserName : ")
    f2=open("Login.txt","r")
    f1=open("Login.txt","a")
    if(createLogin in f2):
        print("\n User already Exist \n")
    else:
        createPassw = input("Create Password:")
        f1.write("\n")
        f1.write(createLogin)
        f1.write("\n")
        f1.write(createPassw)
        f1.write("\n")
        f1.close()
        user[createLogin] = createPassw
        print("\nUser created\n")

def oldUser():
    file1 = open("Login.txt", 'r') 
    Lines = file1.readlines() 
    login = []
    for line in Lines: 
        temp=line.strip()
        login.append(temp)
    
    length=len(login)
    username=input("Enter the username: ")
    flag=0
    for i in range(0,length):
        if username==login[i]:
            index=i
            flag=1
            break
    if flag==0:
        print("user doesn't exists, please register first: ")
        password=input("Enter the password to complete register: ")
        file1.close()
        file = open("Login.txt", 'a+')
        file.write("\n")
        file.write(username + "\n")
        file.write(password)
        file.close()
    else:
        password=input("Enter the password: ")
        while True:
            if password==login[index+1]:
                break
            else:
                password=input("Enter the correct password again: ")
        file1.close() 
    
        print("\n Login Succesfully\n")
        print("\n\nWelcome! To Ticket Booking System\n ")
        print("Press : \n1.Ticket Reservation \n2.PNR Status\n3.E-mail\n4.exit");
        g=1
        while(g):
            while True:
                temp=input("Enter you choice :")
                temp2=temp.isdigit()
                if temp2==True:
                    num=int(temp)
                    if num==1 or num==2 or num==3 or num==4:
                        c=num
                        break
                    else:
                        print("Enter the valid choice: ")
                        continue
                else:
                    print("Enter the valid choice: ")
                    continue
            
            if(c==2):
                print("Enter your CID number : ");
                while True:
                    temp=input()
                    temp2=temp.isdigit()
                    if temp2==True:
                        num=int(temp)
                        cid1=num
                        break
                    else:
                        print("Enter the valid CID number: ")
                        continue
                
                if(str(path.exists(str(cid1)+".txt"))=="True"):
                    f1=open(str(cid1)+".txt","r")
                    print(f1.read())
                    print("press c for continue , n for exit");
                    cs=input();
                    if(cs=='c'):
                        g=1;
                    else:
                        g=0;
                    
                else:
                    print("CID doesn't exist !");
                    print("press c for continue , n for exit");
                    cs=input();
                    if(cs=='c'):
                        g=1;
                    else:
                        g=0;
                
                
            elif(c==1):
                
                g1=1
                while(g1):
                    
                    print("Enter your CID : ")
                    while True:
                        temp=input()
                        temp2=temp.isdigit()
                        if temp2==True:
                            num=int(temp)
                            cid=num
                            break
                        else:
                            print("Enter the valid CID number: ")
                            continue
                   
                    if(str(path.exists(str(cid)+".txt"))=="True"):
                        print("It's already exist !")
                        g1=1
                    else:
                        
                        sd = {1:'Rajkot',2:'Ahmedabad',3:'surat',4:'Gandhinager'};
                        print("select your source place(key) : \n")
                        print(sd)
                        while True:
                            temp2=input()
                            temp=temp2.isdigit()
                            if temp==True:
                                num=int(temp2)
                                if num>0 and num<5:
                                    s=num
                                    break
                                else:
                                    print("Enter the valid source: ")
                                    continue
                            else:
                                print("Enter the valid source: ")
                                continue
                        
                        print("select your destination place(key) : \n")
                        print(sd)
                        while True:
                            temp2=input()
                            temp=temp2.isdigit()
                            if temp==True:
                                num=int(temp2)
                                if num>0 and num<5 and num!=s:
                                    s1=num
                                    break
                                else:
                                    print("Enter the valid destination: ")
                                    continue
                            else:
                                print("Enter the valid destination: ")
                                continue
                            
                        
                        while True:
                            temp = input("how many ticket you want : ")
                            temp2=temp.isdigit()
                            if temp2==True:
                                people=int(temp)
                                break
                            else:
                                print("Enter valid number: ")
                                continue
                            
                        
                        name_l=[]
                        age_l=[]
                        sex_l=[]
                        for i in range(people):
                            while True:
                                temp2=input("Name : ")
                                temp=temp2.isalpha()
                                if temp==True:
                                    name=temp2
                                    break
                                else:
                                    continue
                            name_l.append(name);
                           
                            print("Age: ")
                            while True:
                                temp = input()
                                temp2=temp.isdigit()
                                if temp2==True:
                                    num=int(temp)
                                    if num>0:
                                        age=num
                                        break
                                    else:
                                        print("Enter the valid age: ",end=" ")
                                        continue
                                else:
                                    print("Enter the valid age: ",end="")
                                    continue
                            age_l.append(age)
                            
                            while True:
                                sex = input("Sex : ")
                                if sex=="Male" or sex=="Female" or sex=="male" or sex=="female":
                                    break
                                else:
                                    print("Enter valid things: ",end=" ")
                                    continue
                        
                            sex_l.append(sex)
                            
                        print("Source : ",sd[s])
                        print("Dest   : ",sd[s1])
                        p=random.randint(100,300)
                        print("Price per ticket : ",p)
                        tp=people * p;
                        print("Total fare : ",tp);
                        
                        f=open(str(cid)+".txt","w")
                        
                        f.write("PNR : ")
                        p12 = "G"+str(random_with_N_digits(6))
                        f.write(p12)
                        f.write("\n")
                        
                        f.write("TICKET ID : ")
                        upper_alphabet = string.ascii_uppercase
                        f.write(str(random.randint(1,1000))+str(random.choice(upper_alphabet))) 
                        f.write("\n")
                        
                        f.write("ORDER ID : ")
                        f.write(str(random.randint(1,10000)))
                        f.write("\n")
                        
                        x = datetime.datetime.now()
                        f.write("BOOKING TIME :")
                        f.write(str(x))
                        f.write("\n")
                        
                        f.write("From "+sd[s]+" To "+sd[s1])
                        f.write("\n")
                        
                        f.write("\n")
                        for i in range(people):
                            f.write("\n")
                            
                            f.write("Ticket : ")
                            f.write(str(i+1))
                            f.write("\n")
                            
                            f.write("Name : ")
                            f.write(name_l[i])
                            f.write("\n")
                            
                            f.write("Age : ")
                            f.write(str(age_l[i]))
                            f.write("\n")
                            
                            f.write("sex : ")
                            f.write(sex_l[i])
                            f.write("\n")
                        
                        f.write("Price per ticket : ")
                        f.write(str(p))
                        f.write("\n")
                        
                        f.write("Total Fare : ")
                        f.write(str(tp))
                        f.write("\n")
                        
                        f.close();
                                
                        print("Your bus ticket booking has been confirmed\n");
                        print("press c for continue , n for exit");
                        cs=input();
                        if(cs=='c'):
                            g=1;
                            print("Enter your choice: ")
                            print("Press : \n1.Ticket Reservation \n2.PNR Status\n3.E-mail\n4.exit");
                        else:
                            g=0;
                        g1=0;
            elif(c==3):
                print(" Email Sending Using Python")
                reciever_email = input("enter a receiver_email : ")
                print("Enter your CID : ")
                while True:
                        temp=input()
                        temp2=temp.isdigit()
                        if temp2==True:
                            num=int(temp)
                            cid1=num
                            break
                        else:
                            print("Enter the valid CID number: ")
                            continue
                if(str(path.exists(str(cid1)+".txt"))=="True"):
                    f=open(str(cid1)+".txt","r")
                    hl=f.readlines()
                    m="Hello ,  "+username+"\n\nYour Ticket Booking Confirmed from "+hl[4]+"\n" +hl[0]+"\n"+hl[1]+"\n"+hl[2]
                else:
                    print("File not exist !")
                    sys.exit("Invalid filename")
                    
                p=input("press y for sending email ")

                if(p == 'y'):
                    send_email_new("Ticket Booking",m,"18bce116@nirmauni.ac.in","nihu3346",reciever_email)
            elif(c==4):
                sys.exit("Bye Bye")
            else:
                print("\n User doesn't exist or wrong password")
        

while(status != "q"):
    displayMenu()