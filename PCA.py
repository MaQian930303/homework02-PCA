import numpy as np
from pylab import *
import matplotlib.pyplot as plt

def PCA(data):
    means = np.mean(data,axis=0)
    decentralized = data - means
    covmatrix = np.cov(decentralized, rowvar=0)
    D,V = np.linalg.eig(np.mat(covmatrix))
    D_tmp = np.argsort(D)
    MaxV = V[:,D_tmp[0:2]]
    Pdata = decentralized * MaxV
    return Pdata  

def Show(feature):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.array(feature[:,0])
    y = np.array(feature[:,1])
    ax.scatter(x,y,marker='o',s = 90,c='r')
    plt.show()

# Load data
filename = 'optdigits-orig.wdep'
Data = []
Data_tmp = []
for line in open(filename):
    if not line:
        break
    line = line.strip('\n')
    if len(line) < 5:
        number = int(line)
        if number == 3:
            Data.append(Data_tmp)
        Data_tmp=[]
    else:
       for str in line:
           Data_tmp.append(int(str))

Data_three = array(matrix(Data).T)

# PCA
feature = PCA(Data_three)
Show(feature)

