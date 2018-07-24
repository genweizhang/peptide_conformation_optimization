## This is from amber manual to implement amber force field in python

# import the libraries
import sander
from parmed.amber import AmberParm
import sys, os
import numpy as np 
from my_pyrosetta import generate_coord

'''
def convert_pdb_to_coor_arrary():
    # get the file name and read it in
    file_name=raw_input("Please type the pdb file name here:")
    
    try: 
        pdb_content=open(os.path.abspath(file_name), "r")
    except IOError:
        print ("Sorry, we can't find: ", file_name)
        sys.exit ("Mission aborted!!!")
    # initilize an array that holds all the coordinates
    coor_array=[]

    for line in pdb_content:
        if line[0:6]=="ATOM  " or line[0:6]=="HETATM":
            coor_array.append(float(line[30:38]))
            coor_array.append(float(line[38:46]))
            coor_array.append(float(line[46:54]))
    
    return coor_array
            
inp_coor=convert_pdb_to_coor_arrary()
'''
def get_total_energy(agls):
    # get the coor from pyrosetta
    inp_coor=generate_coord(agls)
    # initialize the object topology with coordinates
    parm=AmberParm("tpp-1.prmtop",inp_coor)
    # set up the input options
    inp=sander.gas_input() 
    sander.setup (parm, parm.coordinates, None, inp)

    # compute the energy and force
    eney, frc=sander.energy_forces()
    # print('sander',eney.tot,eney.gb,eney.vdw, eney.elec, eney.dihedral,eney.angle, eney.bond)

    # clean and finish
    sander.cleanup()
    return eney.tot


