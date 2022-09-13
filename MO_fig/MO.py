import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import pandas as pd
from adjustText import adjust_text

#global parameter define
filebase = sys.argv[1]
inputfile = filebase + '.txt'

def main():
    data = getData(inputfile)
    enelist = data.getEnergy()
    occlist = data.getOcc()
    symlist = data.getSym()
    makepic(filebase,enelist,occlist,symlist,bottom = 6)


class getData:
    def __init__(self,inputfile):
        self.inputfile = inputfile

    def getEnergy(self):
        with open(self.inputfile,'r') as f:
            lines = f.readlines()

        enelist = []
        for line in lines[5:]:
            rowlist = line.split()
            enelist.append(float(rowlist[2]))

        return enelist

    def getOcc(self):
        with open(self.inputfile,'r') as f:
            lines = f.readlines()

        occlist = []
        for line in lines[5:]:
            rowlist = line.split()
            occlist.append(float(rowlist[1]))

        return occlist

    def getSym(self):
        with open(self.inputfile,'r') as f:
            lines = f.readlines()

        symlist = []
        for line in lines[5:]:
            rowlist = line.split()
            str = rowlist[3]
            sym = '$' + str[1] + '_{' + str[2:-1] + '}$'
            symlist.append(sym)
        return symlist

def makepic(filebase,enelist,occlist,symlist,bottom = 0,top = 0):
    SAVEDIR = "./"+filebase
    SAVEDATA = filebase + '_MO.png'

    os.makedirs("./enepic",exist_ok = True)
    os.chdir("./enepic")
    os.makedirs(SAVEDIR,exist_ok = True)
    os.chdir(SAVEDIR)

    x_a = [4.3,5.7]
    x_e1 = [1.3,2.7]
    x_e2 = [7.3,8.7]

    plt.rcParams['ytick.direction'] = 'in'
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_position(('data',0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_xlim(0,10)



    i=top
    texts = []
    while i < (len(enelist)-bottom):
        state = [enelist[i],enelist[i]]

        if enelist[i] != enelist[i+1] or i == (len(enelist)-1):
            ax.plot(x_a, state, linestyle = 'solid', linewidth = 1.0 , color = checkCOLOR(occlist[i]) )
#spin no byouga
            if occlist[i] == 2:
                ax.text(4.7, state[0]-0.03, r'$\uparrow\downarrow$')
#iranekereba kokowo comment out

#            texts.append( ax.text(6.1,state[0] + 0.01, symlist[i], size = 'small') )


            i += 1
        else:
            ax.plot(x_e1, state, linestyle = 'solid', linewidth = 1.0 , color = checkCOLOR(occlist[i]) )
            if occlist[i] == 2:
                ax.text(1.7, state[0]-0.03, r'$\uparrow \downarrow$')

            ax.plot(x_e2, state, linestyle = 'solid', linewidth = 1.0 , color = checkCOLOR(occlist[i]) )
            if occlist[i] == 2:
                ax.text(7.7, state[0]-0.03, r'$\uparrow \downarrow$')
#mosi kiyakuhyougenwo igiritakattara koko

#            texts.append( ax.text(3.1,state[0] +0.01, symlist[i], size = 'small') )
#            texts.append( ax.text(9.1,state[0] +0.01, symlist[i], size = 'small') )


            i += 2

#               adjust_text(texts)
    fig.savefig(SAVEDATA, bbox_inches = 'tight')

def checkCOLOR(col):
    if col == 0:
        return 'blue'
    elif col == 2:
        return 'red'
    elif col == 1:
        return 'green'

if __name__ == '__main__':
    main()
