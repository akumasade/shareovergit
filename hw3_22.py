#for solving HW3 problem 2.2
import numpy as np

#function for calculating the binding energy
def B(A,Z):
    #constants
    a_v = 15.56
    a_s = 17.23
    a_a = 23.28
    a_c = 0.7 
    delta = 2

    #equation to calculate binding energy 
    #(two calculations because plus/minus delta)
    B1 = a_v*A - a_s*A**(2./3) - a_c*Z*Z/(A**(1./3)) - a_a*(A-2*Z)**2/A + delta
    B2 = a_v*A - a_s*A**(2./3) - a_c*Z*Z/(A**(1./3)) - a_a*(A-2*Z)**2/A - delta
    
    return [B1,B2]

#------------------------------------


muc2 = 931.494 #MeV
A = 46 #mass number defined in problem
mHc2 = 938.790
mnc2 = 939.57
muc2 = 931.5
start = 19
end  = 23

for i in range(19,23):
    Z = i
    N = A - Z
    [bener1, bener2] = B(A, Z)#binding energy
    mass1 = Z*mHc2 + N*mnc2 - bener1 #equation to calculate mass
    mass2 = Z*mHc2 + N*mnc2 - bener2
    
    print mass1 - A*muc2, mass2 - A*muc2


