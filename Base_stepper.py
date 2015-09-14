
"""

To initiate the width and size for the step,
Create the ellipses
The functions 'rit_foot' and 'lft_foot' are not used at the moment.

"""

from basic_units import cm
#import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt
from Elipse_Draw import Elips
#from Domains import*


#%matplotlib inline

    
class Base:
    def __init__(self, width, height, angle):
        self.width = width
        self.height = height
        self.angle =  angle
        
    def Right(self, xcenter_rit, ycenter_rit):
        self.xcenter_rit = xcenter_rit
        self.ycenter_rit = ycenter_rit
        #self.angle = angle
        
        x_rit, y_rit = Elips( # These coordinates are not used at the moment
            xcenter_rit, 
            ycenter_rit, 
            self.width, 
            self.height, 
            self.angle) 
        
        rit_foot = patches.Ellipse(
            (xcenter_rit, ycenter_rit), 
            self.width, 
            self.height,
            angle= -self.angle, 
            linewidth=1, 
            fill=False, 
            zorder=2)
        
        return rit_foot
    
    def Left(self, xcenter_lft, ycenter_lft):
        self.xcenter_lft = xcenter_lft
        self.ycenter_lft = ycenter_lft
        #self.angle = angle
        
        x_lft, y_lft = Elips( # These coordinates are not used at the moment
            xcenter_lft, 
            ycenter_lft, 
            self.width, 
            self.height, 
            -self.angle)
        
        lft_foot = patches.Ellipse(
            (xcenter_lft, ycenter_lft), 
            self.width, 
            self.height,
            angle= self.angle, 
            linewidth=1, 
            fill=False, 
            zorder=2)
        
        return lft_foot
