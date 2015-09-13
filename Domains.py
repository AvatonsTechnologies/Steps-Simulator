#from basic_units import cm
#import numpy as np
#from matplotlib import patches
#import matplotlib.pyplot as plt
from Elipse_Draw import Elips


def Domains_x(xcenter_lft, xcenter_rit):
    lft_bound = xcenter_lft - (xcenter_lft*xcenter_lft/2)
    rit_bound = xcenter_rit + (xcenter_rit*xcenter_rit/2)
    
    #print lft_bound, rit_bound
    return lft_bound, rit_bound

def Domains_y(ycenter_lft, ycenter_rit):
    upr_bound = ycenter_lft - (ycenter_lft*ycenter_lft/2)
    lwr_bound = ycenter_rit + (ycenter_rit*ycenter_rit/2)
    
    #print lft_bound, rit_bound
    return upr_bound, lwr_bound
