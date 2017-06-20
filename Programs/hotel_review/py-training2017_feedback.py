#!/usr/bin/env python

'''
FileName : py-training2017_feedback.py
Description : generate a random password and check that password is expired or not
Words input : Breakfast location staff fun happy city center food good service
output : {'mentions': {'city': 2, 'good': 2, 'center': 0, 'service': 1, 'food': 2, 'location': 2, 'fun': 0, 'breakfast': 2, 'staff': 2, 'happy': 1}, 
'topStatement': {'hotelid': '1', 'desc': "i came from south india, the location of hotel was too good, i'm happy with the city location and food."},
'hotels': ['1', '2', '3']}
'''
#module import
import sys
import re
import operator
import string
from collections import defaultdict

#take a user input
user_inputs = (raw_input("Enter your words : >")).lower().split()

try:
    #open a file
    file_data = open('feedback.txt')
    #read a data from file
    file_inputs = file_data.read().lower()
    #close a file
    file_data.close()
except IOError:
    print "File doesn't open,Try again.."
    sys.exit()

#total_occur of words 
def total_occur():
    #define blank output
    output = {}
    #split file data into words
    tempdata = re.findall(r'[^,.;\s]+',file_inputs)
    #match the word and count letters
    for input in user_inputs:
        output[input] = tempdata.count(input)
    return output

#topstatement 
def topStatement():
    #default result 
    result = 0
    #default output declaration
    output = {"desc" : None,"hotelid" : None}
    #default output declaration with value 0
    output1 = {}
    output1 = defaultdict(lambda:0,output1) #by default value for each key is 0
    #split data and generate a list
    tempstring_data = file_inputs.split("\n")
    #check top statement
    for i in range(len(tempstring_data)):
        if i % 2 != 0:
            #take one input and split it
            tempdata = re.findall(r'[^,.;\s]+',tempstring_data[i])
            tempresult = 0
            for input in user_inputs:
                tempresult += tempdata.count(input)
            #store mention word count for one unique id into dict
            output1[tempstring_data[i-1]] = tempresult + output1[tempstring_data[i-1]]
            #find top statement by its count
            if tempresult > result:
                #assignt tempresult to result
                result = tempresult
                #store result into output dict
                output['desc'] = tempstring_data[i]
                output['hotelid'] = tempstring_data[i-1]
    #sort disc by its value 
    sorted_output1 = sorted(output1.items(), key=operator.itemgetter(1),reverse=True)
    finaloutput = []
    #find key based on desending order and print it
    for k,v in sorted_output1:
        #append feedback id into finaloutput
        finaloutput.append(k)
    #return output fot topstatemet & hotelid's
    return output,finaloutput

#function call
o1 = total_occur()
o2 = topStatement()[0]
o3 = topStatement()[1]

#print final output
print { 'mentions' : o1,'topStatement' : o2,"hotels" : o3 }