#!/usr/bin/env python

'''
FileName : py-training2017_pwdgenerate.py
Description : generate a random password and check that password is expired or not
'''

#import requires modules
import random
import string
import sys
import time

#global variables declaration for storing expiration time with password
ver_disc = {} 

#function to generate a random n password of m length with define expiration time
def password_generate(m,expire) :
	password = '';
	while len(password) < m:
		#generate random password combination of digits,lowercase,uppercase,specialcharacter
		password += random.choice(string.digits) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.punctuation)
		#convert password string into list
	password = list(password)
	#shuffle list data
	random.shuffle(password)
	#generate length of exact password
	password = ''.join(password)[:m]
	ver_disc[password] = {'createdtime' : int(time.time()),'expire' : int(time.time()) + expire }
	return password

#function to check that define password is expired or not
def password_verification(check_password):
	try :
		if ver_disc[check_password]['expire'] < int(time.time()):
			return "Expired"
		else:
			return "Not-expired"
	except KeyError,e:
		return 'Password does not exist Try another password'

#menu driven
while True :
	print "********* Password Generation ***********"
	print "1 - Password Generation"
	print "2 - Password Verifivation"
	print "3 - exit"
	print "******************************************"
	#choice to perform specific operation
	choice = eval(raw_input("Enter Your Choice : \n"))
	if choice == 1:
		print "-------------"
		#no of password to be generate
		n = eval(raw_input("Password to be genterated :> \n"))
		#length of each password
		m = eval(raw_input("password length :> \n"))
		#check password length
		if m < 8:
			print "Minimum length 8 characters"
			continue;
		#function to generate password
		expire = eval(raw_input("Enter password expiration time : \n"))
		#start time of password generation
		start = int(time.time())
		#call the function n no of times to generate n no password
		for i in range(n):
			#call a function each time
			print password_generate(m,expire)
		#end time password generation
		end = int(time.time())
		#benchmarking
		print 'Benchmarking Time = %d' %(end - start)
	elif choice == 2:
		print "-----------"
		#password to be verified
		check_password = raw_input("Enter Your password : \n")
		#verify that password expire or not
		print password_verification(check_password)
	elif choice == 3:
		sys.exit()
	else:
		print "Invalid Choice"


