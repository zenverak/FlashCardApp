import ast
from copy import deepcopy as dc

main_path=''



class Card():
    def __init__(self,word,definition,sentence=''):
        self.word=word
        self.definition=definition
        self.sentence=sentence

class Card_list():
    def __init__(self,path=''):
        self.list={}
        self.words=[]
        self.path=path

    def add_word(self,card):
        word = card.word
##        print word
        if word not in self.words:
            self.list[word]=card
            self.words.append(word)

    def get_new_words(self,words):
        new_list=[]
        for i in self.words:
            if i not in words:
                new_list.append(i)
        return new_list


    def save_list(self):
        f = open(self.path,'r')
        old_list = f.readline()
        words = ast.literal_eval(old_list)
        f.close()     
        new_words = self.get_new_words(words)
        if len(new_words)>0:
            f = open(self.path,'r')
            data = f.readlines()
            data[0] = str(self.words)+'\n'
            f.close()
            with open(self.path,'w') as f:
                f.writelines(data)
            f1 = open(self.path, 'a')
            for i in new_words:
                card = self.list[i]
                top='{'+i+'}\n'
                word_to_write = i+'\n'
                definition = card.definition+'\n'
                f1.write(top)
                f1.write(word_to_write)
                f1.write(definition)
                if card.sentence!='':
                    f1.write(card.sentence+'\n')
            f1.close()
        else:
            print "No new words"

    

    def create_list(self):
        f1 = open(self.path, 'w')
        f1.write(str(self.words)+'\n')
        for i in self.words:
            card = self.list[i]
            top='{'+i+'}\n'
            word_to_write = i+'\n'
            definition = card.definition+'\n'
            f1.write(top)
            f1.write(word_to_write)
            f1.write(definition)
            if card.sentence!='':
                f1.write(card.sentence+'\n')
        f1.close()
            
    
    
    def load_list(self):
        list_file  = open(self.path,'r')
        list_data = list_file.readlines()
        word=''
        definition=''
        sentence=''
        in_word_count=0
        for i in list_data[1:]:
            #print "word count ", in_word_count
            if i[0]=='{' and in_word_count==0:
                in_word_count=1
    
            elif in_word_count==1:
                word=i.rstrip('\n')
                in_word_count+=1
            elif in_word_count==2:
                definition=i.rstrip('\n')
                in_word_count+=1
            elif in_word_count==3 and i[0]!='{':
                sentence=i.rstrip('\n')
                in_word_count = 0
                self.add_word(Card(word,definition,sentence))                                
            elif in_word_count==3 and i[0]=='{':
                #print word+" "+definition+" "+sentence
                self.add_word(Card(word,definition,sentence))
                in_word_count=1        
        self.add_word(Card(word,definition,sentence))  
        list_file.close()

        def clear_list(self):
            self.list={}
            self.words=[]
                
                


if __name__=='__main__':
    pass
##    path = './filetest.txt'
##    l1 = Card_list(path)
####    hello = Card('hello','a greeting')
####    l1.add_word(hello)
####    l1.create_list()
####    no = Card('no','cannot do')
####    l1.add_word(no)
####    l1.save_list()
####    adf = Card('ard','af')
####    l1.add_word(adf)
####    l1.save_list()
##
##    l1.load_list()

##    root = tk.Tk()
##    l = tk.Label(root, text="Hello, world!\nTkinter on PocketPC!\nSee http://pythonce.sf.net.")
##    b = tk.Button(root, text='Quit', command=root.destroy)
##    l.pack()
##    b.pack()
##    root.mainloop()

    
    


        
