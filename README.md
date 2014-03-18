ASDLookup
=========

    Author: Jesse Vazquez, Jesse.Vazquez@trincoll.edu
    Last Modified: 03/18/2014
    Version: 1.6
   
    Apple Service Diagnostic Lookup is a program to help with identifying which version of Apple's ASD should be used based on the official Apple name given to that device.    
    
    Usage:
    -- cd to directory of the file
    -- type: python ASDLookup.py SERIAL
    -- ex: python ASDLookup.py C02H6EZ1DV7L
    
    Notes & Future Improvements:
    -- I will be updating this with future versions of ASD as Apple releases them
    -- Add more support for older Apple products, though it's not needed for my usage
    -- Potentially integrate with GSX API for a live list of ASD versions
    
    Recently Fixed:
    -- Made checkASD() more efficient using the eval() method
    -- Updated printComputer() to handle for if no computer is found
    -- Updated checkASD() to initialize "returned" variable
	-- Removed unnecessary variable "versionCount" and "returned" from top declarations section
    
    Adding an ASD version:
    -- Note: Follow the same format as all other versions
    -- >> Add a string to the array 'ASDVer'
    -- >> Add a class named after the version
    -- >> Add compList array to class with supported computers
    
    Credit:
    -- Github user @magervalp shows how to grab the Apple Name from a serial number using their support site, I modified his methods slightly to make them more efficient and fit my needs.