#!/usr/bin/env python

'''
FileName : databaseconnection.py
Description : Database connection with mongodb
'''

#import core modules
import ConfigParser
import sys
import os.path
#import pip modules
import pymongo

'''
className : Setconfiguration
description : return config.ini file object
'''

class Setconfiguration(object):
    _INSTANCE = {}
    #constructor
    def __init__(self): 
        try:
            if bool(self._INSTANCE):
                raise ValueError("An instantiation already exists!")
            _config = ConfigParser.ConfigParser()
            #check that file exist or not
            if not os.path.exists('../config.ini'):
                raise IOError
            #read data from file
            _config.read('../config.ini')
            #return config object
            self._INSTANCE['config'] = _config
        except IOError:
            print "No such file or directory Exist like 'config.ini'"
            sys.exit(0)
        except ValueError:
            print "An instantiation already exists!"
        
    #classmethod to get object of configuration
    @classmethod
    def get_config_instance(cls):
        if not cls._INSTANCE:
            Setconfiguration()
        return cls._INSTANCE['config']

'''
className : Setdatabaseconfiguration
description : return database connection object and inherit Setconfiguration class
'''
class Setdatabaseconfiguration(Setconfiguration):
    _INSTANCE = {}
    #access get_config_instance for getting object of config
    config = Setconfiguration.get_config_instance()
    #constructor
    def __init__(self): 
        try:
            if bool(self._INSTANCE):
                raise ValueError("An instantiation already exists!")
            #create a connection with database
            client = pymongo.MongoClient(self.config.get('database','databaseurl'))
            self._INSTANCE['databaseconfig'] = client
        except IOError:
            print "No such file or directory Exist like 'config.ini'"
            sys.exit(0)
        except pymongo.errors.InvalidURI:
            print "Invalid Database connection Url"
            sys.exit(0)
        except pymongo.errors.ConfigurationError:
            print "configuration error"
            sys.exit(0)
        except pymongo.errors.ConnectionFailure:
            print "Connection Failure"
            sys.exit(0)
        except pymongo.errors.PyMongoError:
            print "Database Connection not done "
    
    #classmethod to get object of databaseconnection
    @classmethod
    def get_databaseconfig_instance(cls):
        if not cls._INSTANCE:
            Setdatabaseconfiguration()
        return cls._INSTANCE['databaseconfig']