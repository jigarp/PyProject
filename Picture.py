####################################################################
##  Thane Fenton                                                  #
##  Image Manipulation                                           #
##
##                      PICTURE.py
##  This is the Class has the implementation to store the image#
##  Asks for the image location, save,dpi, show, width, height#
##                                                           #
#############################################################
import Image
import re

class Picture(object):
    def __init__(self, fileLoc):
        self.fileLocation = fileLoc # sets the image name/location
        self.dpi = 0
        
    def setFileImage(self):
        self.img = "" # start empty
        while(True): # go as long as the file location is incorrect
            try:
                self.img = Image.open(self.fileLocation)
                break
            except (OSError, IOError) as e:
                #print e # Debug
                print "The File you Inputed is not correct.. "
                self.fileLocation = raw_input("Enter the photo directory.. ")


    def setImage(self, replaceImage):
        self.img = replaceImage


    def setDPI(self, dpi):
        self.dpi = dpi

        
    def getWidthHeight(self, theImgSize): # split the two sizes
        a = re.findall('[0-9\s,]', str(theImgSize)) # find all numbs
        location = 0
        for i in range(len(a)):
            if(a[i] == ","): # knwo where to seperate width and height
                location = i
                break

        # join the two together
        width = "".join(a[:location])
        height = "".join(a[location+1:])
        
        return width, height

                
    def getImage(self):
        return self.img

    def getEval(self):
        return "tes"#Image.eval(self.img)
    
    def getSize(self):
        return self.img.size

    def saveImage(self, name):
        if(self.dpi == 0):
            self.img.save(name + ".png",  "PNG")
        else:
            self.img.save(name + ".png", dpi=(self.dpi,self.dpi))
        print "Image Saved..."

        
    def displayPicture(self):
        self.img.show()

        
    

    
