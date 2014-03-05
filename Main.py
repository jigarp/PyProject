###################################################################
##  Thane Fenton                                                 #
##  Image Manipulation                                          #
##
##                         MAIN.py                                     
##  This is the main        which calls all the other classes#
##  Asks for the image location, then allows user to modify #
##                                                         #
###########################################################

#from media import *
#setLibPath('/Users/Jigar/Desktop/CST205/')
import Picture
import os, sys
import enhancing


def currentDirectory():
    print("The Current Directory you are in : " + os.getcwd())


def start():
    fileName = raw_input("Enter the photo directory.. ")

    ## Photo
    pic = Picture.Picture(fileName) ## set filename
    pic.setFileImage() ## set/get photo
    
    ## Edit Photo
    enhanceImage(pic)

    
def enhanceImage(pic):
    img = pic.getImage() ## get Image
    size = pic.getSize() ## get size of image
    enhance = Enhancing.Enhancing(pic, img, size) # some initializing
    while(True):
        
        # Resize
        resizeInput = raw_input("Would you like to resize your image? (yes/no) ")
        if(resizeInput == "yes"):
            enhance.changeResolution()

        # Change the RBG
        rbgInput = raw_input("Would you like to change the RBG? (yes/no) ")
        if(rbgInput == "yes"):
            enhance.changeRBG()

        # Change DPI   
        dpiChange = raw_input("Would you like to modify the DPI? (yes/no) ")
        if(dpiChange == "yes"):
            enhance.changeDPI()

        # Display new Image
        currentState = raw_input("Would you like to see the current Image? (yes/no) ")
        if(currentState == "yes"):
            pic.displayPicture()

        # Save The Image
        saveImage = raw_input("Would you like to save your image? (yes/no) ")
        if(saveImage == "yes"):
            imageName = raw_input("Enter the name of your new Image: ")
            pic.saveImage(imageName)

        #New Image Modify
        continueToModify = raw_input("Edit a new Image? (yes/no) ")
        if(continueToModify == "yes"):
            print "\n\n"
            start()
        else:
            print "\n\n Bye.."
            break

def main():
    currentDirectory() ## Display where we are at
    start() ## lets start this change
    
main()
