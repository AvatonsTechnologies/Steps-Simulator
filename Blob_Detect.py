
"""
        Coordinates = feature.blob_dog(
            lum_img, # This is the image
            min_sigma=15, #The minimum standard deviation for Gaussian Kernel. Keep this low to detect smaller blobs.
            max_sigma=60, #The maximum standard deviation for Gaussian Kernel. Keep this high to detect larger blobs.
            #num_sigma=10, 
            threshold=0.05,#The absolute lower bound for scale space maxima. 
                   #Local maxima smaller than thresh are ignored. 
                   #Reduce this to detect blobs with less intensities.
            overlap=0.5)  #A value between 0 and 1. If the area of two blobs overlaps by 
                  #a fraction greater than threshold, the smaller blob is eliminated.
"""


from matplotlib import pyplot as plt
from skimage import data, measure
from skimage.feature import blob_log, canny
from math import sqrt
from skimage.color import rgb2gray
import time
#%matplotlib inline


def Blobing(image, min_sigma, max_sigma, threshold):
    #image = mpimg.imread('stepping.png')[0:500, 0:500] 
    image_gray = rgb2gray(image)
    image_fltrd = canny(image_gray,
                        sigma=1.0,
                        low_threshold=None,
                        high_threshold=None,
                        mask=None)
    
    blobs_log = blob_log(image_fltrd,
                         min_sigma=min_sigma, # set to10
                         max_sigma=max_sigma, # set to 40
                         num_sigma=10,
                         threshold=threshold)
    
    #-----------------------------------------------------
    #----- Calculating the average of all blobs
    #      This will issue the location of each step
    lngth = len(blobs_log[0:])
    x_avg = sum(blobs_log[:,0])/lngth
    y_avg = sum(blobs_log[:,1])/lngth
    #print 'Step coordinates: (x,y):''(',x_avg,',', y_avg,')'
    
    # Compute belowradii in the 3rd column, this is just the radial of each circle
    blobs_log[:, 2] = blobs_log[:, 2]*sqrt(2)
    
    #-----------------------------------------------------
    #----- Ploting
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image, interpolation='gaussian')
    #time.sleep(0.5)
    plt.close(fig) # save time by closing figure
 
    for circles in blobs_log:
        y, x, r = circles
        c = plt.Circle((x, y), r, color='blue', linewidth=2, fill=False)
        ax.add_patch(c)
        #print x, y
    plt.show()
    #time.sleep(0.5)
    plt.close(fig) # close figure
    
    return x_avg, y_avg # The Blobing returns the coordinates to be used for move command isuers










#==========================================================================

# ------- Older version of Blob detection algorithm, created by Dr. Ahmed Abdelrahman Sep. 05, 2015 
#from skimage import data, io, feature, filters
#from skimage import measure 
#import skimage.io as skio
#import matplotlib.pyplot as plt


#def Blobing(image):
    
    #---------------- Blob detection goes here
    #------------ reading the ion chain image file
    #ImageRead = skio.imread('TwoBlobs.png')
#    image = image#mpimg.imread('TwoBlobs.png')
    #imgplot = plt.imshow(image)
#    lum_img = image[:,:,0]
    #imgplot = plt.imshow(lum_img)
#    contours = measure.find_contours(lum_img, 0.5)
#    fig, ax = plt.subplots(figsize=(7,7))
#    ax.imshow(lum_img, interpolation='nearest', cmap=plt.cm.gray)
#    for n, contour in enumerate(contours):
#        ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
#        ax.axis('image')
#        ax.set_xticks([])
#        ax.set_yticks([])
#        plt.show()
        
#        edges = filters.sobel(lum_img)
        #io.imshow(edges)
#        io.show()
        
#        Coordinates = feature.blob_dog(
#            lum_img, # This is the image
#            min_sigma=30, 
#            max_sigma=50, 
            #num_sigma=10, 
#            threshold=0.05,
#            overlap=0.5)
        
    #print '(xo left, yo left) coordinates  :', (Coordinates[0,0],Coordinates[0,1])
    #print '(xo right, yo right) coordinates:' ,(Coordinates[1,0],Coordinates[1,1])
#    print Coordinates
    
