##This script is to make plots of the peptide optimziation results
#

import numpy as np 
import matplotlib.pyplot as plt  


## read in the optimized raw data from the txt file

with open ("20pops.txt",'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()                    # remove the last empty element

    val20=[float(row.split(' ')[10]) for row in data]   # extract and store the y error values

with open ("30pops.txt",'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()                    # remove the last empty element

    val30=[float(row.split(' ')[10]) for row in data]   # extract and store the y error values

with open ("50pops.txt",'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()                    # remove the last empty element

    val50=[float(row.split(' ')[10]) for row in data]   # extract and store the y error values

with open ("80pops.txt",'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()                    # remove the last empty element

    val80=[float(row.split(' ')[10]) for row in data]   # extract and store the y error values

with open ("100pops.txt",'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()                    # remove the last empty element

    val100=[float(row.split(' ')[10]) for row in data]   # extract and store the y error values

with open ("150pops.txt",'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()                    # remove the last empty element

    val150=[float(row.split(' ')[10]) for row in data]   # extract and store the y error values

with open ("200pops.txt",'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()                    # remove the last empty element

    val200=[float(row.split(' ')[10]) for row in data]   # extract and store the y error values


with open ("50pops_500.txt",'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()                    # remove the last empty element

    val50_500=[float(row.split(' ')[10]) for row in data]   # extract and store the y error values




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
plt.xlim (0, 510)
plt.xlabel('# of Generations')   #('ABT-199 ('+ u'${\u03bc}$M)', labelpad=15)
plt.ylim (-100, 2000)
plt.ylabel('Energy (kcal/mol)') #('Ramachandran plot', labelpad=10)
'''
plt.plot(np.arange(150),val20, 'k-' ,label='20 pops')  #  yerr=std, fmt='.r-', markersize=16, capsize=5, elinewidth=2, linewidth=3)
plt.plot(np.arange(150),val30, 'y-', label='30 pops' )
plt.plot(np.arange(150),val50, 'r-', label='50 pops' )  
plt.plot(np.arange(150),val80, 'g-', label='80 pops' )
plt.plot(np.arange(150),val100, 'c-', label='100 pops' ) 
plt.plot(np.arange(150),val150, 'm-', label='150 pops' )
plt.plot(np.arange(150),val200, 'b-', label='200 pops' ) 
'''
plt.plot(np.arange(500),val50_500, 'r-', label='With 50 pops', linewidth=2.0 ) 
plt.title ('TPP-1 structure minimization', y=1.03)
plt.axhline(y=0, ls='--')
plt.legend(fontsize=12)
plt.show()




