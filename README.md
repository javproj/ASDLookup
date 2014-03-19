ASDLookup
=========

    Author: Jesse Vazquez, Jesse.Vazquez@trincoll.edu
    Last Modified: 03/19/2014
    Version: 1.7
   
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
	-- Cleaned up coding
    -- Now using a dictionary to store versions and supported computers 
	-- >> Storing this data in classes and using the eval() method can be a security problem
	-- Made checkASD() more efficient
    -- Updated printComputer() to handle for if no computer is found
    -- Updated checkASD() to initialize "returned" variable
	-- Removed unnecessary variable "versionCount" and "returned" from top declarations section
    
    Adding an ASD version:
    -- Note: Follow the same format as all other versions
    -- >> Add comma to the end of the last dictionary value
    -- >> Add dictionary pair to ASDver dictionary in format:
    -- >>>> "ASD3S###" : ["computer1", "computer 2"]
    
    Credit:
    -- Github user @magervalp shows how to grab the Apple Name from a serial number using their support site, I modified his methods slightly to make them more efficient and fit my needs.