##################################################################
##  Thane Fenton                                                #
##  Image Manipulation                                         #
##
##                      ENHANCING.py 
##  Allows to get the image and modify : DPI,Resolution,RBG #
##                                                         #
###########################################################

import ImageEnhance
import Image
import re
import Picture

class Enhancing(object):
    def __init__(self, pictureClass, image, size):
        self.pic = pictureClass
        self.currentImg = image
        self.imgSize = size


   # def changeDPI(self):
       # while(True):
            #try:
             #   dpi = input("Set your DPI Resolution : (32-520) ")
              #  if(dpi >= 32 and dpi <= 520):
               #     self.pic.setDPI(dpi) # set the dpi
                #    break
           # except(NameError) as e: ## mmm.. nope.
            #    print e, " You need to enter a correct Number"
             #   continue
            
            
        
    ## Change the RBG
    def changeRBG(self):
        tempImg = self.currentImg
        while(True):
            # Make sure the user puts a int            
           # while(True):
            print "Lower the Number, less RBG's :: Higher the number, more RBG's"
                #try:
                 #   modify = input("Enter a number range 0.1 - 99.9 : ")
                  #  if(modify >= 0.1 and modify <= 99.9): # higher - lighter, vice versa
                   #     tempImg = tempImg.point(lambda i : i * modify)
                    #    break
              #  except(NameError) as e: ## mmm.. nope.
               #     print e, " You need to enter a correct Number"
                #    continue
               
                
            #tempImg.show() # show results

            ## Ask for input
            userInput = raw_input("Finished : \n\tKeep Changes(save), \n\tModify changes(modify), \n\tLeave Without Changes(exit) : ").lower()
            if(userInput == "save"):
                self.savePicture(tempImg)
                break
            elif(userInput == "modify"):
                tempImg = self.currentImg
                continue
            else:
                break
            

    #change resolution
    def changeResolution(self): 
        tempImage = [] # create a array for diff sizes
        temp = self.currentImg
        
        width, height = self.pic.getWidthHeight(self.imgSize) # get the w/h sizes
 
        
        for i in range(4): # 4 is enough..
            if(int(width)/(i+2) < 32 or int(height)/(i+2) < 32):
                break # don't want any image less than 32px
            else:
                size = int(width)/(i+2), int(height)/(i+2) # resize
                tempImage.append(temp.resize(size, Image.ANTIALIAS)) # add to arr
 
        self.changeImage(tempImage) # do some printing..

    def changeImage(self, arr):
        numLength = []
        found = False
        print "Choose what resize you'd like! "
        for i in range(len(arr)):
            print "The Image Sizes are : ", i+1, ": ", arr[i].size, "\n"
            numLength.append(i+1)
        
        while(found == False):
          #  while(True):
               # try:
                #    userInput = input("Choose # for the image size : (-1 for none) ")
                 #   break
               # except(NameError) as e: ## mmm.. nope.
                #    print e, " You need to enter a correct Number"
                 #   continue
                
            if(userInput != -1): ## lets resize if not -1
                for i in numLength: #### O(1) , thats speed.. ####
                    if(userInput == i):
                        self.savePicture(arr[i-1])
                        arr[i-1].show()
                        found = True
            else:
                break

            
    def savePicture(self, img):
        self.pic.setImage(img)
        self.currentImg = img # chagne the currentImage