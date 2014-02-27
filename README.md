ASDLookup
=========

    Author: Jesse Vazquez, Jesse.Vazquez@trincoll.edu
    Last Modified: 02/27/2014
    Version: 1.5
   
    Apple Service Diagnostic Lookup is a program to help with identifying which version of Apple's ASD should be used based on the official Apple name given to that device.    
    
    Usage:
    -- cd to directory of the file
    -- type: python ASDLookup1.5.py SERIAL
    -- ex: python ASDLookup1.5.py C02H6EZ1DV7L
    
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
