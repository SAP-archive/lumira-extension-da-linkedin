# -*- coding: utf-8 -*-
#imports
from linkedin import linkedin
import easygui
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import requests





def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

Mode = enum('PREVIEW', 'EDIT', 'REFRESH')
mode = 0


paramslist = []
key = ''
i = 0
msg = "Enter Required Information"
title = "Linkedin Extractor"
fieldNames = ["Consumer Key","Consumer Secret",
              "User Key","User Secret"]


fieldValues = []  # we start with blanks for the values
for i in range(4):
    fieldValues.append(i)

for i in range(len(sys.argv)):
    if str(sys.argv[i]).lower() == "-mode" and (i + 1) < len(sys.argv):
        if str(sys.argv[i + 1]).lower() == "preview":
            mode = Mode.PREVIEW
        elif str(sys.argv[i + 1]).lower() == "edit":
            mode = Mode.EDIT
        elif str(sys.argv[i + 1]).lower() == "refresh":
            mode = Mode.REFRESH
    elif str(sys.argv[i]).lower() == "-size":
        size = int(sys.argv[i + 1])
    elif str(sys.argv[i]).lower() == "-params":
        params = str(sys.argv[i + 1])
        paramslist = params.split(';')

    i += 1



def setArgs(fieldValues):

    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    USER_TOKEN = ''
    USER_SECRET = ''

    RETURN_URL = '' # Not required for developer authentication

    fieldValues[0] = ''
    fieldValues[1] = ''
    fieldValues[2] = ''
    fieldValues[3] = ''
    return fieldValues


def parseArgs(fieldValues):


    #if paramslist is None: break

    for i in range(len(paramslist)):
        if paramslist[i].split('=')[0].lower() == 'consumer_key':
            try:
                fieldValues[0] = paramslist[i].split('=')[1].decode('hex')
            except:
                fieldValues[0] = 'ENTER_CONSUMER_KEY'
        elif paramslist[i].split('=')[0].lower() == 'consumer_secret':
            try:
                fieldValues[1] = paramslist[i].split('=')[1].decode('hex')
            except:
                fieldValues[1] = 'ENTER_CONSUMER_SECRET'
        elif paramslist[i].split('=')[0].lower() == 'user_token':
            try:
                fieldValues[2] = paramslist[i].split('=')[1].decode('hex')
            except:
                fieldValues[2] = 'ENTER_USER_TOKEN'
        elif paramslist[i].split('=')[0].lower() == 'user_secret':
            try:
                fieldValues[3] = paramslist[i].split('=')[1].decode('hex')
            except:
                fieldValues[3] = 'ENTER_USER_SECRET'
        i += 1

    return fieldValues




def getScreenInput(fieldValues):

    fieldValues = easygui.multenterbox(msg = msg, title = title, fields = fieldNames, values = fieldValues )
        # make sure that none of the fields was left blank
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])

        if errmsg == "":
            break # no problems found
        fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)

    return fieldValues

def printData(fieldValues):

    if fieldValues != None:


        CONSUMER_KEY = fieldValues[0]
        CONSUMER_SECRET = fieldValues[1]
        USER_TOKEN = fieldValues[2]
        USER_SECRET = fieldValues[3]
        RETURN_URL = ''



        print "beginDSInfo"
        print """fileName;#;true
    csv_first_row_has_column_names;true;true;
    csv_separator;|;true
    csv_number_grouping;,;true
    csv_number_decimal;.;true
    csv_date_format;d.M.yyyy;true"""
        print ''.join(['consumer_key;', str(fieldValues[0]).encode('hex'), ';true'])
        print ''.join(['consumer_secret;', str(fieldValues[1]).encode('hex'), ';true'])
        print ''.join(['user_token;', str(fieldValues[2]).encode('hex'), ';true'])
        print ''.join(['user_secret;', str(fieldValues[3]).encode('hex'), ';true'])
        print "endDSInfo"
        print "beginData"
        print 'First_Name, Last_Name, Location'
        #try:
            # Instantiate the developer authentication class

        auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,
                            USER_TOKEN, USER_SECRET,
                            RETURN_URL,
                            permissions=linkedin.PERMISSIONS.enums.values())

        # Pass it in to the app...

        app = linkedin.LinkedInApplication(auth)
        try:
            connections = app.get_connections()
        except requests.ConnectionError:
            easygui.msgbox('Connection Error, Extension Doesnt Support Proxies Yet')

        #print connections

        for c in connections['values']:
              #if c.has_key('location')]
            try:
                print ''.join([c['firstName'].replace(',', ''), ',']),
            except:
                print ''.join(['None', ', ']),
            try:
                print ''.join([c['lastName'].replace(',', ''), ',']),
            except:
                print ''.join(['None', ', ']),
            try:
                print ''.join([c['location']['name'].replace(',', '')])
            except:
                print ''.join(['None'])
        print "endData"
    else:

        print "beginDSInfo"
        print "endDSInfo"
        print "beginData"
        print """Error
User Cancelled"""
        print "endData"




if mode == Mode.PREVIEW:
	fieldValues = setArgs(fieldValues)
	#easygui.textbox(msg = 'preview1', text = sys.argv)
	fieldValues = getScreenInput(fieldValues)
	#easygui.textbox(msg = 'preview2', text = fieldValues)
	printData(fieldValues)
elif mode == Mode.EDIT:
	#easygui.textbox(msg = 'edit1', text = sys.argv)
	fieldValues = parseArgs(fieldValues)
	#easygui.textbox(msg = 'edit2', text = fieldValues)
	fieldValues = getScreenInput(fieldValues)
	#easygui.textbox(msg = 'edit2', text = fieldValues)
	printData(fieldValues)
elif mode == Mode.REFRESH:
	fieldValues = parseArgs(fieldValues)
	#easygui.textbox(msg = 'refresh1', text = sys.argv)
	printData(fieldValues)




