import sys
sys.path.append('\\Program Files\\Python\\Lib\\python23.zip\\lib-tk')
import Tkinter as tk
from FlashCard import Card,Card_list







class App(tk.Tk):
    def __init__(self,path='./filetest.txt'):
        tk.Tk.__init__(self)
        self.lblHello = tk.Label(self,text='Hello, please choose an option')
        self.lblWord = tk.Label(self, text='Add Word')
        self.lblDef = tk.Label(self, text='Add Definition')
        
        self.list = Card_list(path)
        
        self.btnLoad = tk.Button(self, text='Load list', command=self.load_list)
        self.btnSave = tk.Button(self, text='Save List', command=self.save_list)
        self.btnAddWord = tk.Button(self, text='Add Word to List', command = self.add_word)
        self.btnPrintWords = tk.Button(self, text ='Print Words', command = self.print_words)

        self.entWord = tk.Entry(self)
        self.entDef = tk.Entry(self)

        self.card = tk.Text(self)

        self.lblHello.pack()
        
        self.lblWord.pack()
        self.entWord.pack()
        
        self.lblDef.pack()
        self.entDef.pack()
        
        self.btnAddWord.pack()
        self.btnLoad.pack()
        self.btnSave.pack()
        self.btnPrintWords.pack()

        self.card.pack()
        
    def load_list(self):
        self.list.load_list()

    def save_list(self):
        self.list.save_list()

    def add_word(self):
        word = Card(self.entWord.get(),self.entDef.get())
        self.entWord.delete(0,tk.END)
        self.entDef.delete(0,tk.END)
        self.list.add_word(word)
        pass

    def print_words(self):

        ##If the text box has text in it, delete it and then input the new data
        l = len(self.card.get(1.0, tk.END))       
        if l>0:
            self.card.delete(1.0,tk.END)
        self.card.insert(tk.END,str(self.list.words))
        
        
    





if __name__=='__main__':
    app = App()
    app.mainloop()
