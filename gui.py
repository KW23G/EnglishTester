# GUI for English Test Application


##################
# Jannis made this:
# How to use the backend:

# from backend import backend
# backend.check_en_to_de(en, de) <- en = english word, de = german word (check from en to de)
# backend.check_de_to_en(de, en) <- en = english word, de = german word (check from de to en)
# backend.get_word(lan) <- lan = "en" or "de" (language of output word)

# backend.get_word() isn't working yet; the other functions should work
# -> If something isn't working (althought it should), go to Issues on GitHub and add the
# Label "Bug" to the Issue which is not working. (you can ask me how to do do that)

##################


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
        self.translateInput["textvariable"] = self.translate
        self.check = tkinter.Button(self)
        self.check["text"] = "Check"
        self.check["command"] = self.quit
        self.check.pack(side="right")


root = tkinter.Tk()
app = EnglishTesterApp(root)
app.mainloop()
