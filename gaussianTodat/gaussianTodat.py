import numpy as np
import pandas as pd
import sys
import os

#first commandline arg : decalt coordinate only  Export csvfile from atomlist
#second commandline arg : output datfile name
inputfile = sys.argv[1] + '.csv'
file_name_dat = sys.argv[2] +'.dat'

df_prepro = pd.read_table(inputfile, skipinitialspace = True)
df = df_prepro.iloc[:,5:8]

atomnum = len(df.index)

pzswitch = []
inp = ''
while inp == '':
    inp = input('Enterで続行')
    orb = input('軌道:')
    on_site = input('on-site:')
    pzswitch.append((orb,on_site))


def main():

    coordinate = np.array([])
    atom = 0
    for i in range(atomnum ):
        col0 = [str(df.iloc[i,0]), ' '+ str(df.iloc[i,1]), ' ' +  str(df.iloc[i,2]) +'\n']
        if df_prepro.iloc[i,4] == 'H':
            row = ['10 -13.6\n'] + col0
            coordinate = np.concatenate([coordinate,row])
            atom +=1
        else:
            for orb,on_site in pzswitch:
                head = [orb,' '+ on_site+'\n']
                col = head + col0
                coordinate = np.concatenate( [coordinate,col] )
                atom += 1


    intro = np.array(['simple\n',str(atom) + '\n','2\n',input('cutoff')+'\n'])

    vec = ['100',' 0',' 0\n','0',' 100',' 0\n','0',' 0',' 100\n','gamma\n','y\n','20']


    with open(file_name_dat,'w') as f:
        f.writelines(intro)

    with open(file_name_dat,'a') as f:
        f.writelines(coordinate)

        f.writelines(vec)



if __name__ == '__main__':
    main()
