# file: markov.py
# author: Jason Morse
# date: April 24, 2013

# This file contains scaffolding for a python (3) program that will generate random
# text that is statistically constrained by a Markov analysis of some
# input text. The idea was first suggested by Prof. Claude Shannon in
# in 1948.  The scaffolding is set up for distribution for a CS101 problem set.
#
import random
import pprint

from Tkinter import *
import tkFileDialog
import ScrolledText

DEBUG = False

class Markov():

    def __init__(self, root):
        frame1 = Frame(root)
        frame2 = Frame(root)
        frame3 = Frame(root)

        frame1.grid(row=0, column=0)
        frame3.grid(row=0, column=1)
        frame2.grid(row=0, column=2)

        self.inputText = ScrolledText.ScrolledText(frame1, bg='lightgray')
        loadButton = Button(frame1, text="load", command=self.load_file)
        loadButton.grid(row = 0, column = 0)
        self.inputText.grid(row=1, column=0)

        self.outputText = ScrolledText.ScrolledText(frame2, bg='orange')
        
        saveButton = Button(frame2, text="save", command=self.save_file)
        saveButton.grid(row = 0, column = 0)
        self.outputText.grid(row=1, column=0)

        self.degree = StringVar()
        degreeEntry = Entry(frame3, textvariable=self.degree)
        degreeEntry.insert(1, '4')

        generate = Button(frame3, text=">>>", command=self.generate)
        degreeEntry.grid(row=0, column=0)
        generate.grid(row=1, column=0)

    def load_file(self):
        f_name = tkFileDialog.askopenfilename(initialdir="./", title="Pick a text file")
        if(f_name != ''):

            # Open the selected file
            #
            file_in = open(f_name, 'r')

            # Read the file and load the input field.
            #
            lines = file_in.readlines()
            self.inputText.insert(1.0, lines)
            file_in.close()
    
    def save_file(self):
        file_out = tkFileDialog.asksaveasfile(initialdir="./", mode='w',defaultextension='.txt')

        # Write the output text field to the file and close the file
        #
        file_out.write(self.outputText.get(0.0, END))
        file_out.close()

    def getDegree(self):
        return int(self.degree.get())

    def getInputText(self):
        return self.inputText.get(0.0, END)

    def putOutputText(self, text):
        self.outputText.insert(1.0, text)
    
    def generate(self):

        inputText = Markov.getInputText(self)
        x = Markov.getDegree(self)
        
        def outputText(dic, x, n):
            
            string = ''
            outputText = []
            self.outputText.delete(1.0, END)
            
            while 0 != 1:
                if len(string) < x:
                    
                    if string in dic:
                        option = random.choice(dic[string[:x]])
                        outputText.append(option)
                        string = string + option
                        
                elif len(string) == x:
                    
                    if string in dic:
                        option = random.choice(dic[string[:x]])
                        
                        if option != None:
                            outputText.append(option)
                            string = string[1:] + option
                            
                        else:
                            n = ''.join(outputText)
                            return n
        
        def dictionary(inputText, x):

            dic = {}
            a = len(inputText)
            
            for i in range(a + 1):
                
                if i == a:
                    dic[inputText[(i - x):i]] = [None]
                    
                else:
                    if i < x :
                        if '' + inputText[:i] in dic:
                            dic['' + inputText[:i]].append(inputText[i])
                            
                        else:
                            dic['' + inputText[:i]] = [inputText[i]]
                    else:
                        if inputText[(i - x):i] in dic:
                            dic[inputText[(i - x):i]].append(inputText[i])
                            
                        else:
                            dic[inputText[(i - x):i]] = [inputText[i]]
            return dic

        def create(inputText, x):
            d = dictionary(inputText, x)
            n = outputText(d, x, '')
            return n

        dic = create(inputText, x)
        Markov.putOutputText(self, dic)
                
def main():
    root = Tk()    
    root.title("Shannon/Markov Model of Text")
    mark = Markov(root)

    root.mainloop()

main()
