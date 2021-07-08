# Tickit Reservation System Using Python
Group Members:        
	1) 18BCE116 - Nihar Markana
	2) 18BCE119 - Vasu Mavani

Library Used : 
	1)import random
	2)import string
	3)import datetime
	4)from random import randint
	5)from os import path
	6)import smtplib
	7)import sys

Important Modules:
	1)Login System
	2)Registration
	3)TicketReservation
	4)PNR status
	5)E-Mail
	6)exit

Instruction's followed to be :
	1) Register User if not exist otherwise login using username and password
	2) now press 1 for Ticket Reservation :
		Now Enter your customer id number (must be in digits otherwise ready for error)
		Now select your source and destination place using necessary inputs 
		enter how many tickets you want to buy
		enter ticketwisw name , age and gender
		now it get's a message that "Your ticket booking has been confirmed " and print your information

	3) now press 2 for PNR status :
		again enter your customer id number (NOTE :: if your cid already exist then and only then)  
		it prints like in this order :
			{ PNR Number,
			  Order Id,
			  Tickit ID,
			  Booking time,
			  from source to destination,
		          Ticket x
			  Name : xxx
			  Age  : xxx
			  Sex  : xxx,
			  Price per Ticket : xxx,
			  Total Fare : xxx }
	
	4) now press 3 for E-mail send using python :
		enter receiver E-mail and customer id number
		it prints like " E-Mail Sent Successfully"
		and send E-mail to that Mail address 
		and write message like this 
		{  
		Hello , xxxx
		
		Your ticket Booking confirmed from xxxx to xxxx 

		PNR Number : xxxx
		Order Id   : xxxx
		Thank You ! 
                }
	
	5) press 5 for exit.

Points to be noted :

	1) Exception handling
	2) File handling
	3) E-mail sending using python
	4) Login - Register system

Gitub Link : https://github.com/Nihu3346/Nihar123

Python Filename : Ticket_R_S.py
