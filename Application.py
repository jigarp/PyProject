import Tkinter as tk
import tkFileDialog
import Picture
import threading
class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()
        thread = Thread()

        ## creates widgets
    def createWidgets(self):
        
        self.a = tk.Button(text="Browse", command=self.loadFile, width=10)
        self.a.grid()
        self.pointScroller = tk.Scale(label="Point Pixel Ratio",
                                      orient=tk.HORIZONTAL,
                                      length=512)
        self.pointScroller.grid()

        
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)            
        self.quitButton.grid()

        ## Loads the filewindow
    def loadFile(self):
        self.filename = tkFileDialog.askopenfilename(filetypes=(("JPEG", "*.jpg;*.jpeg")
                                                             ,("PNG", "*.png")
                                                             ,("GIF", ".gif")
                                                             ,("All files", "*.*") ))

        print(self.filename)
        pic = Picture.Picture(self.filename)
        pic.setFileImage()
        pic.displayPicture()
        
class Thread():
    def __init__(self ):
        print "hfgs"
        

        
    
    
        
app = Application()                       
app.master.title('Sample application')    
app.mainloop() 
