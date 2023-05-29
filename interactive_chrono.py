# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:22:17 2023

@author: mbouchet
"""

import tkinter as tk
import numpy as np
import matplotlib.pyplot as mpl
from matplotlib.backends.backend_pdf import PdfPages

readarray=np.loadtxt('AICC2023_EDC.txt')
depth_EDC=readarray[:,0]
age_ice_EDC=readarray[:,1]
sigma_age_ice_EDC=readarray[:,2]
age_gas_EDC=readarray[:,3]
sigma_age_gas_EDC=readarray[:,4]

readarray=np.loadtxt('AICC2023_EDML.txt')
depth_EDML=readarray[:,0]
age_ice_EDML=readarray[:,1]
sigma_age_ice_EDML=readarray[:,2]
age_gas_EDML=readarray[:,3]
sigma_age_gas_EDML=readarray[:,4]

readarray=np.loadtxt('AICC2023_TALDICE.txt')
depth_TALDICE=readarray[:,0]
age_ice_TALDICE=readarray[:,1]
sigma_age_ice_TALDICE=readarray[:,2]
age_gas_TALDICE=readarray[:,3]
sigma_age_gas_TALDICE=readarray[:,4]

readarray=np.loadtxt('AICC2023_VOSTOK.txt')
depth_VOSTOK=readarray[:,0]
age_ice_VOSTOK=readarray[:,1]
sigma_age_ice_VOSTOK=readarray[:,2]
age_gas_VOSTOK=readarray[:,3]
sigma_age_gas_VOSTOK=readarray[:,4]

readarray=np.loadtxt('AICC2023_NGRIP.txt')
depth_NGRIP=readarray[:,0]
age_ice_NGRIP=readarray[:,1]
sigma_age_ice_NGRIP=readarray[:,2]
age_gas_NGRIP=readarray[:,3]
sigma_age_gas_NGRIP=readarray[:,4]

input1= input("Among EDC, EDML, TALDICE, VOSTOK and NGRIP, type the name of the core you are interested in:\n")
input2= input("Great choice, now type 1, 2, 3 or 4 depending on what you would like to estimate: \n 1/depth knowing the ice age \n 2/depth knowing the gas age \n 3/ice age kowing the depth \n 4/gas age knowing the depth \n")
if float(input2)<=2:
    input3=float(input("Corresponding age (years):\n"))
else :
    input3=float(input("Corresponding depth (meters):\n"))
    
if input1 == "EDC":
        if input2 == "1":
            s1=np.interp(input3, age_ice_EDC, depth_EDC)
            print("The corresponding depth is", round(s1,3), "m" )
        if input2 == "2":
            s2=np.interp(input3, age_gas_EDC, depth_EDC) 
            print("The corresponding depth is", round(s2,3), "m" )
        if input2 == "3":
            s3=np.interp(input3, depth_EDC,age_ice_EDC)
            s3_sigma=np.interp(input3, depth_EDC,sigma_age_ice_EDC)
            print("The corresponding ice age is", round(s3,2),"+/-", round(s3_sigma),"a BP (years before 1950)" )
        if input2 == "4":
            s4=np.interp(input3, depth_EDC,age_gas_EDC)
            s4_sigma=np.interp(input3, depth_EDC,sigma_age_gas_EDC)
            print("The corresponding gas age is", round(s4,2),"+/-", round(s4_sigma),"a BP (years before 1950)" )
if input1 == "EDML":
        if input2 == "1":
            s1=np.interp(input3, age_ice_EDML, depth_EDML)
            print("The corresponding depth is", round(s1,3), "m" )
        if input2 == "2":
            s2=np.interp(input3, age_gas_EDML, depth_EDML) 
            print("The corresponding depth is", round(s2,3), "m" )
        if input2 == "3":
            s3=np.interp(input3, depth_EDML,age_ice_EDML)
            s3_sigma=np.interp(input3, depth_EDML,sigma_age_ice_EDML)
            print("The corresponding ice age is",round(s3,2),"+/-", round(s3_sigma),"a BP (years before 1950)" )
        if input2 == "4":
            s4=np.interp(input3, depth_EDML,age_gas_EDML)
            s4_sigma=np.interp(input3, depth_EDML,sigma_age_gas_EDML)
            print("The corresponding gas age is",round(s4,2),"+/-", round(s4_sigma),"a BP (years before 1950)"  )
if input1 == "TALDICE":
        if input2 == "1":
            s1=np.interp(input3, age_ice_TALDICE, depth_TALDICE)
            print("The corresponding depth is", round(s1,3), "m" )
        if input2 == "2":
            s2=np.interp(input3, age_gas_TALDICE, depth_TALDICE) 
            print("The corresponding depth is",round(s2,3), "m" )
        if input2 == "3":
            s3=np.interp(input3, depth_TALDICE,age_ice_TALDICE)
            s3_sigma=np.interp(input3, depth_TALDICE,sigma_age_ice_TALDICE)
            print("The corresponding ice age is",round(s3,2),"+/-", round(s3_sigma),"a BP (years before 1950)" )
        if input2 == "4":
            s4=np.interp(input3, depth_TALDICE,age_gas_TALDICE)
            s4_sigma=np.interp(input3, depth_TALDICE,sigma_age_gas_TALDICE)
            print("The corresponding gas age is", round(s4,2),"+/-", round(s4_sigma),"a BP (years before 1950)" )
if input1 == "VOSTOK":
        if input2 == "2":
            s1=np.interp(input3, age_ice_VOSTOK, depth_VOSTOK)
            print("The corresponding depth is", round(s1,3), "m" )
        if input2 == "2":
            s2=np.interp(input3, age_gas_VOSTOK, depth_VOSTOK) 
            print("The corresponding depth is",round(s2,3), "m" )
        if input2 == "3":
            s3=np.interp(input3, depth_VOSTOK,age_ice_VOSTOK)
            s3_sigma=np.interp(input3, depth_VOSTOK,sigma_age_ice_VOSTOK)
            print("The corresponding ice age is",round(s3,2),"+/-", round(s3_sigma),"a BP (years before 1950)" )
        if input2 == "4":
            s4=np.interp(input3, depth_VOSTOK,age_gas_VOSTOK)
            s4_sigma=np.interp(input3, depth_VOSTOK,sigma_age_gas_VOSTOK)
            print("The corresponding gas age is", round(s4,2),"+/-", round(s4_sigma),"a BP (years before 1950)" )       
if input1 == "NGRIP":
        if input2 == "1":
            s1=np.interp(input3, age_ice_NGRIP, depth_NGRIP)
            print("The corresponding depth is",round(s1,3), "m" )
        if input2 == "2":
            s2=np.interp(input3, age_gas_NGRIP, depth_NGRIP) 
            print("The corresponding depth is", round(s2,3), "m" )
        if input2 == "3":
            s3=np.interp(input3, depth_NGRIP,age_ice_NGRIP)
            s3_sigma=np.interp(input3, depth_NGRIP,sigma_age_ice_NGRIP)
            print("The corresponding ice age is", round(s3,2),"+/-", round(s3_sigma),"a BP (years before 1950)")
        if input2 == "4":
            s4=np.interp(input3, depth_NGRIP,age_gas_NGRIP)
            s4_sigma=np.interp(input3, depth_NGRIP,sigma_age_gas_NGRIP)
            print("The corresponding gas age is", round(s4,2),"+/-", round(s4_sigma),"a BP (years before 1950)"  )
            

