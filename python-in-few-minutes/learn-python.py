'''
This is the complete python hands on program to learn Basic programming in python
'''

# Single line comment
''' 
Multi line comments
'''

# imports of packages takes place here
import time
import os

# a sample function / method 
def learnfunction(): # each function defines with 'def' and all the subsequent statements under function (or ny part like if, etc), will be followed by ':'
     # works on indentation, whole python code

    # Sample print statement when function calls
    print "Hello" # this will print in new line
    print "World" # this will also print in new line
    # but to print those in same line
    print "Hello", # you can use comma ',' after print statement, or find your own stuff to arrange your output
    print "World"

    # calling another function from one
    print learnbeyondhelloworld(10,15)
    print learnbeyondhelloworld("hi,", " how are you")

def learntotakeinput():
	# Here we take input from console
	inp = raw_input("Enter anything: ")
	print "this is your input: " + inp
	inp = eval(raw_input("Enter a number: "))
	print type(inp), inp

'''
This is how you can write special comments for each function
'''
def learnbeyondhelloworld(x,y): # definition of a function with a magic, its arguments take its type automatically based on data type 
	return x + y # it's very good if you can maintain a 'space' around any operator(+)

def learntypes():
	# no need to define a type while declaring and initialize a variable
	sample_string = "Hello" # <- this will have type of string
	sample_bool = True # <- this will have type of boolean
	sample_int = 10 # this will have type of int
	sample_float = 10.10 # this will have type of float
	sample_long = 9223372036854775808  # this will becomes the type of long, btw this is the first number of long

	# Feeling bliss as we have these types too
	d = {} # initializing dict type of var
	d = { "name1": "John", "class": "B", "marks": 87} # or initializing with values

	l = [] # initializing list type of var
	l = [1,2,3,4,5,6,7,8,9,0] # initializing with values
	l = ["a","bc","def"] # same with string values

	a = None # initializing a with 'Null' or 'None'

	# Printing types of all the vars, plus, this is how you can print multiple values of vars
	print "%s %s %s %s %s %s %s %s" % (type(sample_string), type(sample_bool), type(sample_int), type(sample_float), type(sample_long), type(a), type(d), type(l))
	# the result will print something like : <type 'str'> <type 'bool'> <type 'int'> <type 'float'> <type 'long'> <type 'NoneType'> <type 'dict'> <type 'list'>

	# Accessing substring
	sample_string = "this string is very long, i will cut down to shorten one."

	#This is how you can access substrings
	print "Substring " + sample_string[45:]    # <<- this will print 'shorten one.' as from char index 45 onwards
	print "Substring " + sample_string[45:52]  # <<- this will print 'shorten'
	print "Substring " + sample_string[:4]  # <<- this will print 'this'

	# accessing dict values
	print "This is a dict value: %s" % d["name1"]
	d["marks"] = 100
	# This is how we access the list value
	print "This is a dict value: %s" % l[0]

	learnflowcontrol()


def learnflowcontrol():
	# let's check values by IF statements

	if True:
		print "It's true"


	x = 40
	# now If with value check and else
	if x < 50:
		print "Yes, the value of x is < 50"
	else:
		print "the value is > 50"

	y = "one"

	# now, with else if
	if y is "one":
		print "it's 1"
	elif y is "two":
		print "it's 2"
	elif y is "three":
		print "It's three"
	else:
		print "i don't know what Y has"

	# some more 'if' play
	l = [1,2,3,4,5,6]
	if 80 in l:
		print "80 is available in l"

	# with 'not'
	if 80 not in l:
		print "80 isn't available in l" # <- this will get print


	# Now, let's do a loop around
	'''
	There are basically two kind of loops available,
	One is For, as mentioned below
	'''

	# Iterate through a list of items
	l = [1,2,3,4,5,6] # list

	for i in l:    # See, this is how simple it is
		print "for loop1 printing int: %d" % i

	# now this for loop prints strings
	l = ["string1", "string2", "string3"]
	for i in l:    # See, this is how simple it is
		print "for loop2 printing string: " + i

	# preparing list with hybrid values
	l = [1,2,"string1", "string2", False]
    # Now, this one iterate through hybrid list
	for i in l: # this is amazing
		print i, type(i) # This will print values and its type side by side

	# now, let's break out of the loop
	for i in range (0,50):    # <<- this is how you can provide range of the loop which is exactly same as C's for loop 'for(i=0;i<50;i++)'
		# but, i dont want to continue after 50
		if i > 20:
			break
		# and, all divisible by 2 should not be printed
		if i % 2 is 0:
			continue  # skipping
		# printing the value
		print i

	# While loop
	'''
	this is infinite loop which never stops
	'''
	while True:
		break  # lol, kiddin
		continue # unreached


	# now let's iterate through dict values
	d = { "name1": "John", "class": "B", "marks": 87}

	for key in d:
		print "Key:" + key

	for key, value in d.iteritems():
		print "Key: %s Value: %s" % (key, str(value))

	# check if dict has a key or not, similar way you can also check in list
	if "key" in d:
		print "Dict has Key: key"

	'''
	Python doesn't have switch case feature, 
	but has alternative way if you know how to do it 
	( a kind of work around soln)
	'''
	num = 2
	def zerocase():
		print "Zerocase called"
	def onecase():
		print "Onecase called"
	def twocase():
		print "Twocase called" # this will be printed
	def threecase():
		print "Threecase called"
	cases = {
			   0 : zerocase,
	           1 : onecase,
	           2 : twocase,
	           3 : threecase,
           }

	# this will call the appropriate method
	cases[num]()

	'''
	now let's learn some cool stuff
	lambda it is.
	let's assume we have an array as defined in l below. 
	and we need to do square of only those number which are divisible by 3
	'''
	l = [1,2,3,4,5,6,7,8,9]
	print filter(lambda x: x % 3 == 0, l) # this prints number only which are div by 3
	print map(lambda x: x*x if x % 3 == 0 else x, l) # this prints square of the number if number is div by 3

	# now json
	'''
	let say you have a JSOn string came from web, and you want to parse the Json and get a single element's value.
	This is how you can do with json lib
	'''
	import json # Not suggested to import in between, recommended to use import at top
	s = """{"key1":"value1","key2": { "innerkey1": "innervalue" } }"""
	jsonobj = json.loads(s) # this will raise exception as well if the string is not proper
	print "printing after parsing json : " + jsonobj["key2"]["innerkey1"]  # this will print innervalue

	learnotherstuff()

# writing default values of any argument
def learndefaultvalue(x, y, z = 10): # setting default value for z
	return x * y * z

def learnotherstuff():
	# here we will see how to write a default value for a param/arg if it's not passed
	print "printing from default value:", learndefaultvalue(4, 5, 7) # this will print 140 (4 * 5 * 7)
	print "printing from default value:", learndefaultvalue(4, 5) # this will print 200 (4 * 5 * 10) as 10 was the default value of last param
	# Let's make some http request
	learnhttprequest()

	# now, let's learn how to write things in python
	learnfile()

def learnhttprequest():
	# here we use urllib2 to make http requests
	import urllib2    # again, it's bad to import here, do it on top
	response = urllib2.urlopen('http://python.org/') # this will make a GET request
	html = response.read() # 'html' prints the whole html source from the page
	print response.info()

	# similarly, we can use 'requests'
	import requests
	r = requests.get('http://python.org/')
	print r.status_code

	'''
	you can do more with requests other than POST, GET, one of the example of POST is as follows
	>>> import json

	>>> url = 'https://api.github.com/some/endpoint'
	>>> payload = {'some': 'data'}   # < this is JSON

	>>> r = requests.post(url, data=json.dumps(payload))
	'''

def learnfile():
	# here we will write a file
	st = "This is a sample string which will be written in file."
	f = open("thefile.txt","w")
	f.write(st)
	f.close()  # this is good practice

	# now, hopefully you must have idea about reading from file.
	f = open("thefile.txt","r")
	print "Reading from file: ",f.read()
	f.close()

	# now, let's create CSV file 
	import csv # again, don't import here in real usage, do all imports on top
	a = []
	row = ["name", "age", "height"]
	row1 = ["Alpha", "22", "6ft"]
	a.append(row)
	a.append(row1)
	with open('thecsvfile.csv', 'wb') as csvfile:
	    spamwriter = csv.writer(csvfile)
	    for each in a:
	    	spamwriter.writerow(each)

# starting the program
learnfunction()
learntotakeinput()
learntypes()

