#!/usr/bin/python3

# This is a web.config changing script

import os
import sys
import re
#from string import Template

# Commandline arguments
cmdLineArgs = sys.argv

# file name in same folder or directory we want to modify
outPutFileName = 'web.config'

# Absolute path to the file so we can open a file handle to work with
fullFile = os.path.abspath(outPutFileName)

# XML header
header = '<?xml version="1.0" encoding="utf-8"?>\n'

# Microsoft web.config comments
comment = '<!--\n  For more information on how to configure your ASP.NET application, please visit\n  http://go.microsoft.com/fwlink/?LinkId=169433\n  -->\n'

# Start config element
startConfigElem = '<configuration>\n'

# End config element
endConfigElem = '</configuration>'

# Start connection string element
startConnStringElem = '  <connectionStrings>\n'

# End connection string element
endConnStringElem = '  </connectionStrings>\n'

# Start app string element
startAppStringElem = '  <appSettings>\n'

# End app string element
endAppStringElem = '  </appSettings>\n'

# Execution file name for later error checking if needed
theExecFileName = str()

# Variable holding database name
global dbName
dbName = str

# Variable holding enviroment name ie. Dev, Stage, prod
global envName
envName = str

# Variable Holding website name
global webName
webName = str



# Execution file name pattern
fileNamePattern = re.compile(r'wconf_app.py')

# Database name pattern
dbNamePattern = re.compile(r'dbname=')

# Website name pattern
webNamePattern = re.compile(r'webname=')

# Enviroment name pattern
envNamePattern = re.compile(r'envname=')

# Interactive mode pattern
intModePattern = re.compile(r'-i')

def writeOutputFile():

    # Variable holding website template data
    wsTemplateData = str()

    # Variable holding database template data
    dbTemplateData = envName + '-' + dbName

    # Putting together the webAppStringElem
    if envName == 'prod':
        wsTemplateData = 'https://www.' + webName + '/site'
    else:
        wsTemplateData = 'https://' + envName + '.' + webName + '/secure'

    # The database connection string element
    dbConnStringElem = '    <add name="' + dbTemplateData +'" connectionString="Data Source=myServer;Initial Catalog=' + dbTemplateData + ';user id=myID;password=myPWD" providerName="System.Data.SqlClient" />\n'

    # The web application string element
    webAppStringElem = '    <add key="myURL" value="' + wsTemplateData + '" />\n'

    # Open file handle to the file we are modifying
    fileHandle = open(fullFile, 'w')

    # Write the formated output to the file
    fileHandle.write(header + comment + startConfigElem + startConnStringElem + dbConnStringElem + endConnStringElem + startAppStringElem + webAppStringElem + endAppStringElem + endConfigElem)

    # Close and save the file handle
    fileHandle.close()


def interactiveMode():

    print('Please enter your enviroment for this config: Dev, Stage, prod')
    global envName
    envName = input()

    print('Please enter your database name:')
    global dbName
    dbName = input()

    print('Please enter your website name:')
    global webName
    webName = input()

    writeOutputFile()



for i in cmdLineArgs:
    if bool(fileNamePattern.search(i)) == True:
        theExecFileName = i
    elif bool(intModePattern.search(i)) == True:
        interactiveMode()
        exit
    elif bool(dbNamePattern.search(i)) == True:
        dbName = i[7:]
    elif bool(webNamePattern.search(i)) == True:
        webName = i[8:]
    elif bool(envNamePattern.search(i)) == True:
        envName = i[8:]

writeOutputFile()
