from basic_units import cm
import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt
from Elipse_Draw import Elips
from Domains import*
import matplotlib.image as mpimg
from Blob_Detect import Blobing
import time
from Base_stepper import*

#%matplotlib inline

def main():
    
    x = Base(0.5e-1*cm ,2e-1*cm,10)
    #xcenter_rit, ycenter_rit = 0.55, 0.5
    #x.Right(0.55, 0.5)
    i = 0
    while i < 2:
        fig = plt.figure(figsize=(5,5)) 
        ax = fig.add_subplot(111, aspect='auto')
        ax.add_patch(x.Right(0.6, 0.5))
        plt.close(fig) # close figure to save time
        plt.show()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        #time.sleep(0.5)
        fig.savefig('stepping.png')
        image = mpimg.imread('stepping.png')[0:500, 0:500]
        x0,y0 = Blobing(image, 5, 40, 0.01)
        print 'Step coordinates: (x,y):''(',x0,',', y0,')'
        time.sleep(0.5)
        
        fig = plt.figure(figsize=(5,5)) 
        ax = fig.add_subplot(111, aspect='auto')
        ax.add_patch(x.Left(0.45, 0.5))
        plt.close(fig) # closing figure to save time
        plt.show()
        
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        fig.savefig('stepping.png')
        image = mpimg.imread('stepping.png')[0:500, 0:500]
        x0, y0 = Blobing(image, 5, 40, 0.01)
        print 'Step coordinates: (x,y):''(',x0,',', y0,')'
        i = i+1
    
main()
