import sys
sys.path.append('\\Program Files\\Python\\Lib\\python23.zip\\lib-tk')
import Tkinter as tk
from FlashCard import Card,Card_list
from copy import deepcopy as dc
import random







class App(tk.Tk):
    def __init__(self,path='./filetest.txt'):
        tk.Tk.__init__(self)
        self.lblHello = tk.Label(self,text='Hello, please choose an option')
        self.lblWord = tk.Label(self, text='Add Word')
        self.lblDef = tk.Label(self, text='Add Definition')
        
        self.list = Card_list(path)
        print self.list.list
        
        self.btnLoad = tk.Button(self, text='Load list', command=self.load_list)
        self.btnSave = tk.Button(self, text='Save List', command=self.save_list)
        self.btnAddWord = tk.Button(self, text='Add Word to List', command = self.add_word)
        self.btnPrintWords = tk.Button(self, text ='Print Words', command = self.print_words)

        self.current={'word':'','list':[],'index':0,'yesno':''}
        self.good_words=[]
        self.bad_words=[]
        self.old_words=[]
        

        self.entWord = tk.Entry(self)
        self.entDef = tk.Entry(self)

        self.card = tk.Text(self,height=10)

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

        #Eventually put these widgets onto a different screen
        self.btnStart = tk.Button(self, text='Start Flash Card', command=self.flash_cards)
    
        self.flashWord=tk.Text(self,width=30,height=10)

        self.btnYes = tk.Button(self, text='I got the definition correct',command=self.yes)
        self.btnNo = tk.Button(self, text='I did not get the definition correct',command=self.no)
        self.btnFlip = tk.Button(self, text='Flip to definition',command=self.flip)

        self.txtAnswer = tk.Entry(self)
        
        self.btnFlip.pack()

        self.btnStart.pack()
        self.flashWord.pack()
        self.btnYes.pack()
        self.btnNo.pack()
        
    def load_list(self):
        self.list.load_list()


    def save_list(self):
        self.list.save_list()

    def add_word(self):
        _word = Card(self.entWord.get(),self.entDef.get())
        self.entWord.delete(0,tk.END)
        self.entDef.delete(0,tk.END)
        self.list.add_word(_word)
    

    def print_words(self):

        ##If the text box has text in it, delete it and then input the new data
        _l = len(self.card.get(1.0, tk.END))       
        if _l>0:
            self.card.delete(1.0,tk.END)
        self.card.insert(tk.END,str(self.list.words))

    def _change_card_info(self,text):
        self.card.delete(1.0,tk.END)
        self.card.insert(tk.END,text)

    def flash_cards(self,other_list=''):
        _l = len(self.card.get(1.0,tk.END))
        if _l>0:
            self.card.delete(1.0,tk.END)
        self.current['list'] = dc(self.list.words)
        self.current['index']=0
        _word = self.current['list'][0]
        self.current['word']=self.list.list[_word]
        self.card.insert(tk.END,self.current['word'].word)

    def _sort_n_show(self):
        for _i in self.old_words:
            if _i['yesno']=='yes':
                self.good_words.append(_i['word'])
            else:
                self.bad_words.append(_i['word'])

        self._change_card_info('You are done with this list!\n')
        self.card.insert(tk.END,'You got the following words Right:\n\n')
        for _i in self.good_words:
            self.card.insert(tk.END,str(_i.word)+'\n')
        self.card.insert(tk.END,'\n')
        self.card.insert(tk.END,'You got the following words Wrong:\n\n')
        for _i in self.bad_words:
            self.card.insert(tk.END,str(_i.word)+'\n')


        


    def _next_card(self):
        ##Check to see if the person said yes or no if they got the definition correct. Perhaps need to make sure the person also flipped the card first.
        if self.current['yesno']=='':       
            self._change_card_info('You need to select yes or no before you continue')
        else:
            self.old_words.append(dc(self.current))
            _l = len(self.current['list'])
            self.current['index']+=1
            self.current['yesno']=''
            if self.current['index']+1>=_l:
                self._sort_n_show()
            else:
                _word = self.current['list'][self.current['index']]
                self.current['word'] = self.list.list[_word]
                self._change_card_info(self.current['word'].word)
        
        

        
    

    def no(self):
        self.current['yesno'] = 'no'
        self._next_card()
    def yes(self):
        self.current['yesno'] = 'yes'
        self._next_card()
    def flip(self):
        self._change_card_info(self.current['word'].definition)

        
##        if other_list=='':
##            ##This gives us the possibility of using another list should
##            ## we have some need for it. Honestly I forget my original intent
##            other_list=dc(self.list.list)
##        while len(word_list)>0:
##            ##get a random word. Person has to say if they got it right
##            ## if they did they say yes and then the word gets removed from
##            ##  word_list
##            word = word_list[random.randint(0,len(word_list))]
##            card = other_list[word]
##            self.flashWord.insert(tk.END, "Word: "+word+'\n\n\n Press flip when you are ready and the press yes or no if you got the definition correct')
##            




        
        
    





if __name__=='__main__':
    app = App()
    app.mainloop()
    
