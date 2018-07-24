from os.path import abspath 

# main function
def main():
    # call function to read .pdb files
    atom_list=read_pdb()
    
    # call function to calculate torsion angles
    phi,psi=calc_torsion(atom_list)

    # call function to generate the rama plot
    plot_rama(phi,psi, "Phi(Deg)","Psi(Deg)")


def read_pdb():
    # import library
    import sys
    # create an empty list
    atom_list=[]
    # get file name by calling function read_file_name()
    file_name=read_file_name()
    # try to open .pdb file
    try:
        my_file=open(abspath(file_name),"r")
    except IOError:
        print("Error! Cannot find file:",file_name)
        sys.exit("Execution abort!")
    # read in every line through looping
    for line in my_file:
        if line[0:6]=="ATOM  " or line[0:6]=="HETATM":
            atom_list.append(line)
        
    # close file
    my_file.close()
    # return the atom_list
    return atom_list
    


def read_file_name():
    file_name=raw_input("Type file name here: ")
    return file_name

def calc_torsion(my_atom_list):
    # import library
    import numpy as np
    # columns and rows equal to 3
    columns=3
    rows=9999
    # initialize three arrays holding Co, N, Ca
    co=np.array ([[0]*columns]*rows, float)
    n=np.array([[0]*columns]*rows,float)
    ca=np.array([[0]*columns]*rows,float)
    # Set up the counts
    count_res=0
    former_res=2222
    new_res=1111
    found_co=0
    found_n=0
    found_ca=0
    # loop through my_atom_list
    for line in my_atom_list:
        # the order is important
        if line[0:6]=="ATOM  " and line[13:15]=="C ":
            co[count_res,0]=float(line[30:38])
            co[count_res,1]=float(line[38:46])
            co[count_res,2]=float(line[46:54])
            new_res=int(line[22:26])
            found_co=1
        elif line[0:6]=="ATOM  " and line[13:15]=="N ":
            n[count_res,0]=float(line[30:38])
            n[count_res,1]=float(line[38:46])
            n[count_res,2]=float(line[46:54])
            new_res=int(line[22:26])
            found_n=1
        elif line[0:6]=="ATOM  " and line[13:15]=="CA":
            ca[count_res,0]=float(line[30:38])
            ca[count_res,1]=float(line[38:46])
            ca[count_res,2]=float(line[46:54])
            new_res=int(line[22:26])
            found_ca=1
        complete_mc=found_ca*found_co*found_n
        if former_res != new_res and complete_mc:
            former_res=new_res
            count_res +=1
            found_ca=0
            found_co=0
            found_n=0
    # Creat array for storing phi and psi angles
    phi=np.zeros(count_res-1)
    psi=np.zeros(count_res-1)
    # Compute the phi and psi angles, loop through
    for i in range(count_res-1):
        # call the important function, which calculate torison angles
        phi[i]=torsion(co[i],n[i+1],ca[i+1],co[i+1])
        psi[i]=torsion(n[i+1],ca[i+1],co[i+1],n[i+2])
    print(phi,psi)
    return phi, psi

def torsion(a,b,c,d):

    ''' 
    Calculate vector q1,q2, and q3
    Calculate cross vector q1xq2 and q2xq3
    Calculate normal vectors n1 and n2
    Calculate orthogonal unit vectors
    Calculate sin(theta) and cos(theta)
    Calculate atan2(sin(theta),cos(theta) )
    '''
    # vector q1, q2, q3
    import numpy as np
    import math
    q1=np.subtract(b,a)
    q2=np.subtract(c,b)
    q3=np.subtract(d,c)
    # cross vector
    q12=np.cross(q1,q2)
    q23=np.cross(q2,q3)
    n1=q12/(np.sqrt(np.dot(q12,q12)))
    n2=q23/(np.sqrt(np.dot(q23,q23)))
    # unit vector
    u1=n2
    u=q2/np.sqrt(np.dot(q2,q2))
    u2=np.cross(u,u1)
    # sin(theta) and cos(theta)
    costheta=np.dot(n1,u1)
    sintheta=np.dot(n1,u2)
    # atan2()
    theta=-math.atan2(sintheta,costheta)
    theta_deg=np.degrees(theta)
    return theta_deg

def plot_rama(phi,psi,x_label,y_label):
    # import plot library
    import matplotlib.pyplot as plt
    import numpy as np
    # generate the rama plot
    plt.plot(phi, psi, '.')
    plt.xlim(-180,180)
    plt.ylim(-180,180)
    plt.xticks(np.arange(-180,180.1,45))
    plt.yticks(np.arange(-180,180.1,45))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    ax=plt.axes()
    ax.arrow(-180,0,360,0) 
    ax.arrow(0,-180,0,360)
    plt.show()


# main()


from pylab import *
import matplotlib
import matplotlib.pyplot as plt
cdict = {'red': ((0.0, 0.0, 0.0),
                 (0.5, 1.0, 0.7),
                 (1.0, 1.0, 1.0)),
         'green': ((0.0, 0.0, 0.0),
                   (0.5, 1.0, 0.0),
                   (1.0, 1.0, 1.0)),
         'blue': ((0.0, 0.0, 0.0),
                  (0.5, 1.0, 0.0),
                  (1.0, 0.5, 1.0))}
my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)
pcolor(rand(100,100),cmap=my_cmap)
colorbar()
plt.show() 
































