import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import pandas as pd

filebase = sys.argv[1]
inputfile = filebase + '.log'


def main():
    lines = getdata(inputfile)
    startindex,endindex = serchindex(lines)
    preproband = lines[startindex:endindex]
    # print(preproband[2][-3:]=='eV\n')
    bandproduction = production(preproband)
    bandproduction.getlocalrownum()
    occnum,shape0 = bandproduction.getshapenum()
    # print(shape0)
    energymat = bandproduction.getenergymat()
    makepic_onedim(energymat, occnum,bottom = 1)

def getdata(inputfile):
    with open(inputfile,'r') as f:
        return f.readlines()

def serchindex(lines):
    for index,line in enumerate(lines):
        if line[:10] == ' SCF Done:':
            startindex = index+4
        elif line[:5] == ' HOCO':
            endindex = index
    return (startindex,endindex)


class production:
    def __init__(self,preproband):
        self.preproband = preproband

    def getlocalrownum(self): #get number of row(gyou)
        self.localrownum = 0
        for line in self.preproband:
            if line[39:52] == '0     0     0':
                self.localrownum += 1

    def getshapenum(self): #get number of valaence orbital and conduction orbital
        self.shape0 = int((len(self.preproband)/ self.localrownum)-1)
        self.occnum = 0
        self.virtnum = 0
        for i in range(self.localrownum):
            line = self.preproband[i]
            if line[:4] == ' occ':
                if line[-3:] == 'eV\n':
                    energys = line[52:-4]
                    energyline = [energys[i:i+8] for i in range(0,len(energys),8)]
                else:
                    energys = line[52:-2]
                    energyline = [energys[i:i+8] for i in range(0,len(energys),8)]
                self.occnum += len(energyline)
            else:
                if line[-3:] == 'eV\n':
                    energys = line[52:-4]
                    energyline = [energys[i:i+8] for i in range(0,len(energys),8)]
                else:
                    energys = line[52:-2]
                    energyline = [energys[i:i+8] for i in range(0,len(energys),8)]
                self.virtnum += len(energyline)
        self.shape1 = self.occnum + self.virtnum
        return (self.occnum,self.shape0)

    def getenergymat(self): #make table of energys
        energylist = []
        for line in self.preproband[self.localrownum:]:
            if line[:4] == ' occ':
                if line[-3:] == 'eV\n':
                    energys = line[52:-4]
                    energyline = [energys[i:i+8] for i in range(0,len(energys),8)]
                else:
                    frag = 1
                    energys = line[52:-2]
                    energyline = [energys[i:i+8] for i in range(0,len(energys),8)]
            else:
                if line[-3:] == 'eV\n':
                    energys = line[52:-4]
                    energyline = [energys[i:i+8] for i in range(0,len(energys),8)]
                else:
                    frag = 0
                    energys = line[52:-2]
                    energyline = [energys[i:i+8] for i in range(0,len(energys),8)]
            energylist += energyline
        return np.array(energylist,dtype = np.float64 ).reshape([self.shape0,self.shape1])


def makepic_onedim(energymat, occnum,bottom = 0, top = 0): #make figure
    SAVEDATA = filebase + '.png'
    SAVEDIR = './pic'

    os.makedirs(SAVEDIR,exist_ok = True)
    os.chdir(SAVEDIR)
    os.makedirs(filebase,exist_ok = True)
    os.chdir(filebase)

    np.savetxt('frontier.csv',energymat[:,occnum - 1:occnum + 1], delimiter = ',')

    xaxis = np.arange(energymat.shape[0])
    xaxis = xaxis[::-1]     #gaussian ga Xpoint kara hajimarukara
    plt.rcParams['ytick.direction'] = 'in'
    fig = plt.figure()
    ax = fig.add_subplot(131)
    plt.xlim(0,xaxis[0])
    plt.tick_params(labelbottom = False, bottom = False)
    ax.set_ylabel('Energy [eV]')
    for i in range(bottom, energymat.shape[1]-top):
        if i < occnum:
            ax.plot(xaxis, energymat[:,i], linestyle = 'solid', linewidth = 1.0, color = 'red')
        else:
            ax.plot(xaxis, energymat[:,i], linestyle = 'solid', linewidth = 1.0, color = 'blue')
    ax.text(0,-28,r'$\Gamma$')
    ax.text(xaxis[0],-28,r'$X$')
    fig.savefig(SAVEDATA, bbox_inches = 'tight')

if __name__ == '__main__':
    main()
