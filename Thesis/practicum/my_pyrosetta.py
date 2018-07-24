
## This script aim to return the atomic coordinates after the 
## set-up/changing dihedral angles 

from pyrosetta import *
import numpy as np 
from pyrosetta.toolbox import extract_coords_pose
init()

# get the pdb file
my_pep=pose_from_pdb("amber_tpp-1_changed_to_pyrosetta.pdb")

#my_pep=pose_from_sequence("SGQYASYHCWCWRDPGRSGGSK", "fa_standard")
#from pyrosetta.toolbox import cleaning
#cleaning.cleanATOM("tpp-1.pdb")
#my_pep.dump_pdb("Initial_tpp-1.pdb")

def generate_coord(agls):


    # modify phi and psi angles
    for i in range(1, my_pep.total_residue()+1):
        my_pep.set_phi(i,agls[i-1])
        my_pep.set_psi(i,agls[i+21])
    '''
    # set all 35 chi angles
    my_pep.set_chi(1,1,agls[44])
    my_pep.set_chi(1,3,agls[45])    
    my_pep.set_chi(2,3,agls[46])
    my_pep.set_chi(3,3,agls[47])
    my_pep.set_chi(1,4,agls[48])
    my_pep.set_chi(2,4,agls[49])    
    my_pep.set_chi(1,6,agls[50])
    my_pep.set_chi(1,7,agls[51])
    my_pep.set_chi(2,7,agls[52])
    my_pep.set_chi(1,8,agls[53])    
    my_pep.set_chi(2,8,agls[54])
    my_pep.set_chi(1,9,agls[55])
    my_pep.set_chi(1,10,agls[56])
    my_pep.set_chi(2,10,agls[57])    
    my_pep.set_chi(1,11,agls[58])
    my_pep.set_chi(1,12,agls[59])
    my_pep.set_chi(2,12,agls[60])
    my_pep.set_chi(1,13,agls[61])    
    my_pep.set_chi(2,13,agls[62])
    my_pep.set_chi(3,13,agls[63])
    my_pep.set_chi(4,13,agls[64])    
    my_pep.set_chi(1,14,agls[65])
    my_pep.set_chi(2,14,agls[66])
    my_pep.set_chi(1,17,agls[67])
    my_pep.set_chi(2,17,agls[68])
    my_pep.set_chi(3,17,agls[69])    
    my_pep.set_chi(4,17,agls[70])
    my_pep.set_chi(1,18,agls[71])
    my_pep.set_chi(1,21,agls[72])
    my_pep.set_chi(1,22,agls[73])    
    my_pep.set_chi(2,22,agls[74])
    my_pep.set_chi(3,22,agls[75])
    my_pep.set_chi(4,22,agls[76])
    '''

    coord=extract_coords_pose.extract_coordinates_from_pose_3x1(my_pep)
    
    #my_pep.dump_file("pyrosetta_generated_ser-gly_modified.pdb")

    #print "My peptide sequence is: ", my_pep.sequence()
    '''
    for i in range(1, my_pep.total_residue()+1):
        print i, "phi =", my_pep.phi(i), "psi =", my_pep.psi(i)#, "chi =", my_pep.chi(i,1)   

    print "My peptide length is: ", len(coord[0])
    '''
    # transpose the coord array.
    new_coord=np.transpose (coord)

    # find the coversion index from pyrosetta to amber atom type:
    n_ser_idx=[0,6,7,8,1,9,4,10,11,5,12,2,3]   # N_S: 13
    ser_idx=[0,6,1,7,4,8,9,5,10,2,3]           # S: 11
    gly_idx=[0,4,1,5,6,2,3]                    # G: 7
    gln_idx=[0,9,1,10,4,11,12,5,13,14,6,7,8,15,16,2,3] # Q: 17
    tyr_idx=[0,12,1,13,4,14,15,5,6,16,8,18,10,11,20,9,19,7,17,2,3]  # Y: 21
    ala_idx=[0,5,1,6,4,7,8,9,2,3]              # A: 10
    his_idx=[0,10,1,11,4,12,13,5,6,8,15,9,16,7,14,2,3]  # H: 17
    cys_idx=[0,6,1,7,4,8,9,5,10,2,3]            # C: 11
    trp_idx=[0,14,1,15,4,16,17,5,6,18,8,19,9,11,21,13,23,12,22,10,20,7,2,3]  # W: 24
    arg_idx=[0,11,1,12,4,13,14,5,15,16,6,17,18,7,19,8,9,20,21,10,22,23,2,3]  # R: 24 
    asp_idx=[0,8,1,9,4,10,11,5,6,7,2,3]         # D: 12
    pro_idx=[0,6,12,13,5,10,11,4,8,9,1,7,2,3]   # P: 14
    c_lys_idx=[0,10,1,11,5,12,13,6,14,15,7,16,17,8,18,19,9,20,21,22,2,3,4] # C_K: 23

    # put together, get the new index list
    new_idx=n_ser_idx+\
                        [x+13 for x in gly_idx]+\
                        [x+20 for x in gln_idx]+\
                        [x+37 for x in tyr_idx]+\
                        [x+58 for x in ala_idx]+\
                        [x+68 for x in ser_idx]+\
                        [x+79 for x in tyr_idx]+\
                        [x+100 for x in his_idx]+\
                        [x+117 for x in cys_idx]+\
                        [x+128 for x in trp_idx]+\
                        [x+152 for x in cys_idx]+\
                        [x+163 for x in trp_idx]+\
                        [x+187 for x in arg_idx]+\
                        [x+211 for x in asp_idx]+\
                        [x+223 for x in pro_idx]+\
                        [x+237 for x in gly_idx]+\
                        [x+244 for x in arg_idx]+\
                        [x+268 for x in ser_idx]+\
                        [x+279 for x in gly_idx]+\
                        [x+286 for x in gly_idx]+\
                        [x+293 for x in ser_idx]+\
                        [x+304 for x in c_lys_idx]
    ## for some reason the index after 229 is messed up, add-up one to each solve the problem!!!
    for i in range(len(new_idx)):
        if new_idx[i] > 229:
            new_idx[i]=new_idx[i]+1

    # convert!!! get the amber atom type coord, which is a 327*3 array  
    amber_coord=new_coord[new_idx]
    # concatenate to one-dimension
    final_coord=np.reshape(amber_coord,(1,981))
    
    return final_coord



'''
angles_file=open('Best_pose_phi_psi_angles_50pops_500_2.txt', 'r')
angle_array=[]
for line in angles_file:
    angle_array.append(float(line))

for i in range(1, my_pep.total_residue()+1):
        my_pep.set_phi(i,angle_array[i-1])
        my_pep.set_psi(i,angle_array[i+21])


my_pep.dump_pdb("optimized_tpp-1_3.pdb")
'''

# help(my_pep)

