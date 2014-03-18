"""
    Author: Jesse Vazquez, Jesse.Vazquez@trincoll.edu
    Last Modified: 03/18/2014
    Version: 1.7
   
    Apple Service Diagnostic Lookup is a program to help with identifying which version of Apple's ASD should be used based on the official Apple name given to that device.    
    
    Usage:
    -- cd to directory of the file
    -- type: python ASDLookup.py SERIAL
    -- ex: python ASDLookup.py C02H6EZ1DV7L
    
    Adding an ASD version:
    -- Note: Follow the same format as all other versions
    -- >> Add comma to the end of the last dictionary value
    -- >> Add dictionary pair to ASDver dictionary in format:
    -- >>>> "ASD3S###" : ["computer1", "computer 2"]
    
    Credit:
    -- Github user @magervalp shows how to grab the Apple Name from a serial number using their support site, I modified his methods slightly to make them more efficient and fit my needs.
"""
import sys
import urllib2
from xml.etree import ElementTree

computer = ""       # this will hold the computer's entire name
serial = ""         # holds the serial number of the computer

##################### START ASDver DICTIONARY #########################
ASDver = { 
    "ASD3S108" : ["iMac (17-inch, Early 2006)", "iMac (20-inch, Early 2006)", "iMac (17-inch, Mid 2006)", "iMac (17-inch, Late 2006)", "iMac (17-inch, Late 2006, CD)", "iMac (20-inch, Late 2006)", "iMac (24-inch)", "Mac mini (Early 2006)", "Mac mini (Late 2006)", "Mac Pro", "MacBook (13-inch)", "MacBook Pro (15-inch)", "MacBook Pro (15-inch, Glossy)", "MacBook Pro (17-inch)"],
     
    "ASD3S116" : ["iMac (20-inch, Mid 2007)", "iMac (24-inch, Mid 2007)", "Mac mini (Mid 2007)", "Mac Pro (8x)", "MacBook (13-inch, Late 2006)", "MacBook (13-inch, Mid 2007)", "MacBook Pro (15-inch, Core 2 Duo)", "MacBook Pro (15-inch, 2.4/2.2 GHz)", "MacBook Pro (17-inch, Core 2 Duo)", "MacBook Pro (17-inch, 2.4 GHz)"],
    
    "ASD3S123" : ["iMac (20-inch, Early 2008)", "iMac (24-inch, Early 2008)", "Mac Pro (Early 2008)", "MacBook (13-inch, Late 2007)", "MacBook (13-inch, Early 2008)", "MacBook (13-inch, Late 2008)", "MacBook Air (original)", "MacBook Pro (15-inch, Early 2008)", "MacBook Pro (17-inch, Early 2008)"],
    
    "ASD3S132A" : ["iMac (20-inch, Early 2009)", "iMac (20-inch, Mid 2009)", "iMac (24-inch, Early 2009)", "Mac mini (Early 2009)", "Mac Pro (Early 2009)", "MacBook (13-inch, Aluminum, Late 2008)", "MacBook (13-inch, Early 2009)", "MacBook (13-inch, Mid 2009)", "MacBook Air (Late 2008)", "MacBook Air (Mid 2009)", "MacBook Pro (13-inch, Mid 2009)", "MacBook Pro (15-inch, Late 2008)", "MacBook Pro (15-inch, Mid 2009)", "MacBook Pro (15-inch, 2.53 GHz, Mid 2009)", "MacBook Pro (17-inch, Late 2008)", "MacBook Pro (17-inch, Early 2009)", "MacBook Pro (17-inch, Mid 2009)"],
    
    "ASD3S138" : ["iMac (21.5-inch, Late 2009)", "iMac (27-inch, Late 2009)", "Mac mini (Late 2009)", "MacBook (13-inch, Late 2009)", "MacBook (13-inch, Mid 2010)", "MacBook Pro (13-inch, Mid 2010)", "MacBook Pro (15-inch, Mid 2010)", "MacBook Pro (17-inch, Mid 2010)"],
    
    "ASD3S139" : ["Mac mini (Mid 2010)"],
    
    "ASD3S140" : ["iMac (21.5-inch, Mid 2010)", "iMac (27-inch, Mid 2010)"],
    
    "ASD3S142A" : ["MacBook Air (11-inch, Late 2010)", "MacBook Air (13-inch, Late 2010)"],
    
    "ASD3S144" : ["MacBook Pro (13-inch, Early 2011)", "MacBook Pro (15-inch, Early 2011)", "MacBook Pro (17-inch, Early 2011)"],
    
    "ASD3S145" : ["iMac (21.5-inch, Mid 2011)", "iMac (27-inch, Mid 2011)"],
    
    "ASD3S146" : ["MacBook Air (11-inch, Mid 2011)", "MacBook Air (13-inch, Mid 2011)", "Mac mini (Mid 2011)"],
    
    "ASD3S147" : ["iMac (21.5-inch, Late 2011)"],
    
    "ASD3S148" : ["MacBook Pro (13-inch, Late 2011)", "MacBook Pro (15-inch, Late 2011)", "MacBook Pro (17-inch, Late 2011)"],
    
    "ASD3S149" : ["Mac Pro (Mid 2010)", "Mac Pro (Mid 2012)"],
    
    "ASD3S150" : ["MacBook Air (11-inch, Mid 2012)", "MacBook Air (13-inch, Mid 2012)", "MacBook Pro (13-inch, Mid 2012)", "MacBook Pro (15-inch, Mid 2012)", "MacBook Pro (Retina, Mid 2012)"],
    
    "ASD3S151" : ["iMac (21.5-inch, Late 2012)", "iMac (27-inch, Late 2012)", "Mac mini (Late 2012)", "MacBook Pro (Retina, 13-inch, Late 2012)"],
    
    "ASD3S152" : ["iMac (21.5-inch, Late 2012)", "iMac (27-inch, Late 2012)", "Mac mini (Late 2012)", "Mac mini Server (Late 2012)", "MacBook Pro (Retina, 13-inch, Late 2012)"],
    
    "ASD3S155" : ["MacBook Air (11-inch, Mid 2012)", "MacBook Air (13-inch, Mid 2012)", "MacBook Pro (13-inch, Mid 2012)", "MacBook Pro (15-inch, Mid 2012)", "MacBook Pro (Retina, Mid 2012)", "MacBook Pro (Retina, 13-inch, Late 2012)", "MacBook Pro (Retina, 13-inch, Early 2013)", "MacBook Pro (Retina, 15-inch, Early 2013)"],
    
    "ASD3S156" : ["MacBook Air (13-inch, Mid 2013)", "MacBook Air (11-inch, Mid 2013)"],
    
    "ASD3S157" : ["iMac (21.5-inch, Late 2012)", "iMac (27-inch, Late 2012)", "Mac mini (Late 2012)", "Mac mini Server (Late 2012)", "iMac (21.5-inch, Early 2013)", "iMac (21.5-inch, Late 2013)", "iMac (27-inch, Late 2013)"],
    
    "ASD3S158" : ["MacBook Pro (Retina, 13-inch, Late 2013)", "MacBook Pro (Retina, 15-inch, Late 2013)"],
    
    "ASD3S159" : ["Mac Pro (Late 2013)"]
}

##################### END DICTIONARY / START FUNCTIONS #############

def printComputer():
    """ Sets the computer variable to the name of the computer, which is obtained by using the getCode and getModel functions. Once it has the computer name, it runs checkASD to identify the version based on the computer name"""
    # Run getModel on the output from getCode
    computer = getModel(getCode(serial))    
    
    print "Serial Number: ", serial
    if computer == None:
        print "Could not identify Apple name from serial"
    else:
        print "Apple Name: ", computer
    return checkASD(computer)

def checkASD(compName):
    """
        This function takes in a string which is the computer name, then loops through each of the dictionary keys looking for a matching value in ASDver. If found: Print the key (ver), otherwise let user know that none were found
    """
    returned = False
    # Loop through 
    for ver in ASDver:
        # Check is computer name is a value for the given key
        if compName in ASDver[ver]:
            print ver
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
