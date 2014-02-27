"""
    Author: Jesse Vazquez, Jesse.Vazquez@trincoll.edu
    Last Modified: 02/27/2014
    Version: 1.5
   
    Apple Service Diagnostic Lookup is a program to help with identifying which version of Apple's ASD should be used based on the official Apple name given to that device.    
    
    Usage:
    -- cd to directory of the file
    -- type: python ASDLookup.py SERIAL
    -- ex: python ASDLookup.py C02H6EZ1DV7L
    
    Notes & Future Improvements:
    -- I will be updating this with future versions of ASD as Apple releases them
    -- Make checkASD more efficient as I have to loop through each compList individually
    -- Add more support for older Apple products, though it's not needed for my usage
    
    Recently Fixed:
    -- No longer using Tkinter module, now runs from command line
    -- Takes in the serial as an argument
    -- Ability to look up ASD version based on serial number
    -- Changed name to "ASD Lookup" from "ASDHelper"
    
    Adding an ASD version:
    -- Note: Follow the same format as all other versions
    -- >> Add a string to the array 'ASDVer'
    -- >> Add a class named after the version
    -- >> Add compList array to class with supported computers
    -- >> In checkASD, create for loop for the new class, and update versionCount
    
    Credit:
    -- Github user @magervalp shows how to grab the Apple Name from a serial number using their support site, I modified his methods slightly to make them more efficient and fit my needs.
"""
import sys
import urllib2
from xml.etree import ElementTree

computer = ""       # this will hold the computer's entire name
versionCount = 0    # used when looping to pull right version from ASDver array
returned = False    # used to determine if an ASD version was returned
serial = ""         # holds the serial number of the computer

##################### START ASD CLASSES #########################

#Global variable List that stores the string literal names of all classes.
ASDver = ["ASD3S108", "ASD3S116", "ASD3S123", "ASD3S132A", "ASD3S138", "ASD3S139", "ASD3S140", "ASD3S142A", "ASD3S144", "ASD3S145", "ASD3S146", "ASD3S147", "ASD3S148", "ASD3S149", "ASD3S150", "ASD3S151", "ASD3S152", "ASD3S155", "ASD3S156", "ASD3S157", "ASD3S158", "ASD3S159"]

#Each class has a compList array that will contains strings of all of the supported computers.
class ASD3S108():
    compList = ["iMac (17-inch, Early 2006)", "iMac (20-inch, Early 2006)", "iMac (17-inch, Mid 2006)", "iMac (17-inch, Late 2006)", "iMac (17-inch, Late 2006, CD)", "iMac (20-inch, Late 2006)", "iMac (24-inch)", "Mac mini (Early 2006)", "Mac mini (Late 2006)", "Mac Pro", "MacBook (13-inch)", "MacBook Pro (15-inch)", "MacBook Pro (15-inch, Glossy)", "MacBook Pro (17-inch)"]

class ASD3S116():
    compList = ["iMac (20-inch, Mid 2007)", "iMac (24-inch, Mid 2007)", "Mac mini (Mid 2007)", "Mac Pro (8x)", "MacBook (13-inch, Late 2006)", "MacBook (13-inch, Mid 2007)", "MacBook Pro (15-inch, Core 2 Duo)", "MacBook Pro (15-inch, 2.4/2.2 GHz)", "MacBook Pro (17-inch, Core 2 Duo)", "MacBook Pro (17-inch, 2.4 GHz)"]

class ASD3S123():
    compList = ["iMac (20-inch, Early 2008)", "iMac (24-inch, Early 2008)", "Mac Pro (Early 2008)", "MacBook (13-inch, Late 2007)", "MacBook (13-inch, Early 2008)", "MacBook (13-inch, Late 2008)", "MacBook Air (original)", "MacBook Pro (15-inch, Early 2008)", "MacBook Pro (17-inch, Early 2008)"]

class ASD3S132A():
    compList = ["iMac (20-inch, Early 2009)", "iMac (20-inch, Mid 2009)", "iMac (24-inch, Early 2009)", "Mac mini (Early 2009)", "Mac Pro (Early 2009)", "MacBook (13-inch, Aluminum, Late 2008)", "MacBook (13-inch, Early 2009)", "MacBook (13-inch, Mid 2009)", "MacBook Air (Late 2008)", "MacBook Air (Mid 2009)", "MacBook Pro (13-inch, Mid 2009)", "MacBook Pro (15-inch, Late 2008)", "MacBook Pro (15-inch, Mid 2009)", "MacBook Pro (15-inch, 2.53 GHz, Mid 2009)", "MacBook Pro (17-inch, Late 2008)", "MacBook Pro (17-inch, Early 2009)", "MacBook Pro (17-inch, Mid 2009)"]

class ASD3S138():
    compList = ["iMac (21.5-inch, Late 2009)", "iMac (27-inch, Late 2009)", "Mac mini (Late 2009)", "MacBook (13-inch, Late 2009)", "MacBook (13-inch, Mid 2010)", "MacBook Pro (13-inch, Mid 2010)", "MacBook Pro (15-inch, Mid 2010)", "MacBook Pro (17-inch, Mid 2010)"]
    
class ASD3S139():
    compList = ["Mac mini (Mid 2010)"]

class ASD3S140():
    compList = ["iMac (21.5-inch, Mid 2010)", "iMac (27-inch, Mid 2010)"]

class ASD3S142A():
    compList = ["MacBook Air (11-inch, Late 2010)", "MacBook Air (13-inch, Late 2010)"]
    
class ASD3S144():
    compList = ["MacBook Pro (13-inch, Early 2011)", "MacBook Pro (15-inch, Early 2011)", "MacBook Pro (17-inch, Early 2011)"]
    
class ASD3S145():
    compList = ["iMac (21.5-inch, Mid 2011)", "iMac (27-inch, Mid 2011)"]
    
class ASD3S146():
    compList = ["MacBook Air (11-inch, Mid 2011)", "MacBook Air (13-inch, Mid 2011)", "Mac mini (Mid 2011)"]
    
class ASD3S147():
    compList = ["iMac (21.5-inch, Late 2011)"]
    
class ASD3S148():
    compList = ["MacBook Pro (13-inch, Late 2011)", "MacBook Pro (15-inch, Late 2011)", "MacBook Pro (17-inch, Late 2011)"]
    
class ASD3S149():
    compList = ["Mac Pro (Mid 2010)", "Mac Pro (Mid 2012)"]
    
class ASD3S150():
    compList = ["MacBook Air (11-inch, Mid 2012)", "MacBook Air (13-inch, Mid 2012)", "MacBook Pro (13-inch, Mid 2012)", "MacBook Pro (15-inch, Mid 2012)", "MacBook Pro (Retina, Mid 2012)"]
    
class ASD3S151():
    compList = ["iMac (21.5-inch, Late 2012)", "iMac (27-inch, Late 2012)", "Mac mini (Late 2012)", "MacBook Pro (Retina, 13-inch, Late 2012)"]
    
class ASD3S152():
    compList = ["iMac (21.5-inch, Late 2012)", "iMac (27-inch, Late 2012)", "Mac mini (Late 2012)", "Mac mini Server (Late 2012)", "MacBook Pro (Retina, 13-inch, Late 2012)"]

class ASD3S155():
    compList = ["MacBook Air (11-inch, Mid 2012)", "MacBook Air (13-inch, Mid 2012)", "MacBook Pro (13-inch, Mid 2012)", "MacBook Pro (15-inch, Mid 2012)", "MacBook Pro (Retina, Mid 2012)", "MacBook Pro (Retina, 13-inch, Late 2012)", "MacBook Pro (Retina, 13-inch, Early 2013)", "MacBook Pro (Retina, 15-inch, Early 2013)"]

class ASD3S156():
    compList = ["MacBook Air (13-inch, Mid 2013)", "MacBook Air (11-inch, Mid 2013)"]

class ASD3S157():
    compList = ["iMac (21.5-inch, Late 2012)", "iMac (27-inch, Late 2012)", "Mac mini (Late 2012)", "Mac mini Server (Late 2012)", "iMac (21.5-inch, Early 2013)", "iMac (21.5-inch, Late 2013)", "iMac (27-inch, Late 2013)"]

class ASD3S158():
    compList = ["MacBook Pro (Retina, 13-inch, Late 2013)", "MacBook Pro (Retina, 15-inch, Late 2013)"]
    
class ASD3S159():
    compList = ["Mac Pro (Late 2013)"]

##################### END CLASSES / START FUNCTIONS #############

def printComputer():
    """ Sets the computer variable to the name of the computer, which is obtained by using the getCode and getModel functions. Once it has the computer name, it runs checkASD to identify the version based on the computer name"""
    # Reset the computer variable in case we run it multiple times
    computer = ""
    
    # Run getModel on the output from getCode
    computer = getModel(getCode(serial))    
    
    print "Serial Number: ", serial
    print "Apple Name: ", computer
    return checkASD(computer)

def checkASD(compName):
    """
        This function takes in a string which is the computer name, then loops through each of the class compList arrays looking for that string in each of the ASD version classes.
    """
    for j in ASD3S108.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 1
    for j in ASD3S116.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 2
    for j in ASD3S123.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 3
    for j in ASD3S132A.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 4
    for j in ASD3S138.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 5
    for j in ASD3S139.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 6
    for j in ASD3S140.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 7
    for j in ASD3S142A.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 8
    for j in ASD3S144.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 9
    for j in ASD3S145.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 10
    for j in ASD3S146.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 11
    for j in ASD3S147.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 12
    for j in ASD3S148.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 13
    for j in ASD3S149.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 14
    for j in ASD3S150.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 15
    for j in ASD3S151.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 16
    for j in ASD3S152.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 17
    for j in ASD3S155.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 18
    for j in ASD3S156.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 19
    for j in ASD3S157.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 20
    for j in ASD3S158.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    versionCount = 21
    for j in ASD3S159.compList:
        if compName == j:
            print ASDver[versionCount]
            returned = True
            break
    if returned == False:
        print "No ASD version found, check your input"
    
def getCode(sn):
    """ Gets the code, which is the last 3-4 characters of all 2008+ serial numbers, depending on length """
    return sn[8:]

def getModel(code):
    """ Given the code of the serial number, this looks up the name based on that code"""
    try:
        url = urllib2.urlopen("http://support-sp.apple.com/sp/product?cc=%s&lang=en_US" % code, timeout = 2)
        et = ElementTree.parse(url)
        return et.findtext("configCode").decode("utf-8")
    except:
        return None

#################### END FUNCTIONS / RUN ########################

serial = sys.argv[1]
printComputer()
