# GUI for English Test Application

import tkinter
class EnglishTesterApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.translateInput = tkinter.Entry(self)
        self.translateInput.pack()
        self.translate = tkinter.StringVar()
        self.translate.set("Bitte hier Uebersetzung eingeben")
        self.translateInput["textvariable"]=self.translate
        self.check=tkinter.Button(self)
        self.check["text"]="Check"
        self.check["command"]=self.quit
        self.check.pack(side="right")

root=tkinter.Tk()
app=EnglishTesterApp(root)
app.mainloop()
