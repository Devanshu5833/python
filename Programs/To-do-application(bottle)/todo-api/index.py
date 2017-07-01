#!/usr/bin/env python

'''
FileName : index.py
Description : TO-DO application
'''

#import pip modules
from bottle import run
#import other modules
import apis
from databaseconnection import Setconfiguration

#start a server
if __name__ == "__main__":
    ##set object for congiguration
    config = Setconfiguration.get_config_instance()
    #start server
    run(host=config.get('application','ipaddress')
        ,port=config.get('application','port'))