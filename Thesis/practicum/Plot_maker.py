##This script is to make plots of the peptide optimziation results
#

import numpy as np 
import matplotlib.pyplot as plt  


## read in the raw data from the txt file

angles_file=open('Best_pose_phi_psi_angles_50pops_500_2.txt', 'r')
angle_array=[]
for line in angles_file:
    angle_array.append(float(line))

'''
with open (abspath("binding-assay-2.txt"),'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()                    # remove the last empty element

    x = [float(row.split(' ')[0]) for row in data]   # extract and store the x axis values
    y = [float(row.split(' ')[2]) for row in data]   # extract and store the y axis values
    std=[float(row.split(' ')[4]) for row in data]   # extract and store the y error values
'''
## make the plot

# adjust some fonts and parameters
SMALL_SIZE = 8
MEDIUM_SIZE = 12
BIGGER_SIZE = 20

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize

# plot
fig = plt.figure()
fig.patch.set_facecolor('white')
plt.xlim (-185, 185)
plt.xlabel('Phi')   #('ABT-199 ('+ u'${\u03bc}$M)', labelpad=15)
plt.ylim (-185, 185)
plt.ylabel('Psi') #('Ramachandran plot', labelpad=10)
plt.plot(angle_array[0:22],angle_array[22:44], 'b+' )  #  yerr=std, fmt='.r-', markersize=16, capsize=5, elinewidth=2, linewidth=3)
plt.title ('Ramachandran plot', y=1.03)
plt.axvline(x=0)
plt.axhline(y=0)
plt.show()




