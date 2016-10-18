#for solving HW3 problems 2.2, 2.4

#constant mass energies (in MeV)
muc2 = 931.494 
mHc2 = 938.790
mnc2 = 939.57

#factors for SEMF (in MeV)
a_v = 15.56
a_s = 17.23
a_a = 23.28
a_c = 0.7
delta = 2


#function for calculating the binding energy
def B(A,Z):
    #equation to calculate binding energy 
    #(two calculations because plus/minus delta)
    B1 = a_v*A - a_s*A**(2./3) - a_c*Z*Z/(A**(1./3)) - a_a*(A-2*Z)**2/A + delta
    B2 = a_v*A - a_s*A**(2./3) - a_c*Z*Z/(A**(1./3)) - a_a*(A-2*Z)**2/A - delta
    
    return [B1,B2]

def mass(A,Z):
    #equation for calculating mass energy
    N = A - Z #number of neutrons
    [bener1, bener2] = B(A, Z)#binding energy
    m1 = Z*mHc2 + N*mnc2 - bener1 #using +delta mass
    m2 = Z*mHc2 + N*mnc2 - bener2 #using -delta mass
    return [m1,m2]

#-----------------2.2-------------------

A = 46 #mass number defined in problem

print "Problem 2.2"
#calculating Z from derivative
#solved from setting dm/dZ = 0
#(just plugging in)
print "Z = ", (4*a_a-mHc2+mnc2) / (2*a_c/(A**(1./3)) + 8*a_a/A) #returns ~21 

print "Z \t mass (MeV)"#headers
for i in range(1, 47):
    Z = i#looping thru all Z values
    [bener1, bener2] = B(A, Z)#binding energy
    [mass1, mass2] = mass(A,Z)#mass energy
    

    print Z, "\t", mass1
#we see that at Z = 21, the mass is the smallest
#so we can conclude that it is stable at Z = 21, A = 46
print "\n"
#------------------2.4------------------

#calculate U-238 binding energy and mass energy
BU238_1,BU238_2 = B(238,92)
mU238_1,mU238_2 = mass(238,92)

#calculate Pd-119 binding energy and mass energy
BPd119_1,BPd119_2 = B(119,46)
mPd119_1,mPd119_2 = mass(119,46)

#Difference in binding energies is our energy released
E = 2*BPd119_1 - BU238_1

print "Problem 2.4"
print "E = ", E # returns 183.783631102 MeV


