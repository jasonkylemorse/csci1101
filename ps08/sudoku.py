# file: sudoku.py
# author: Jason Morse & Wantong Liu
# date: April 12, 2013
#

from Tkinter import *
import tkFileDialog

import threading
import os.path

class Sudoku(threading.Thread):

    def __init__(self, master):

        self.the_board = [[ 0 for col in range(9)] for row in range(9)]

        frame = Frame(master)
        frame.pack()

        self.check_button = Button(frame, text="Check", command=self.check_board_validity)
        self.load_button  = Button(frame, text="Load", command=self.load_file)
        self.solve_button = Button(frame, text="Solve", command=self.solve)
        self.clear_button = Button(frame, text="Clear", command=self.clear_board)
        self.save_button  = Button(frame, text="Save", command=self.save_file)
        
        self.show_work_value = IntVar()
        self.show_work_box = Checkbutton(frame, text="Show Work", variable=self.show_work_value)

        self.status = ''
        self.status_bar = Entry(frame, text="Status", textvariable=self.status, state=DISABLED, width=40)

        self.check_button.grid(row=0, column=0)
        self.load_button.grid(row=0,  column=1)
        self.solve_button.grid(row=0, column=2)
        self.clear_button.grid(row=0, column=3)

        self.save_button.grid(row=1,  column=0)
        self.show_work_box.grid(row=1, column=2, columnspan=2)

        board_frame = Frame(frame)
        board_frame.grid(rowspan=9, columnspan=9)
        self.status_bar.grid(columnspan=9, column=0)

        self.textfields = [[self.makeEntry(board_frame, row, col) for col in range(9)] for row in range(9)]
            
        self.guesses = 0

    def makeEntry(self, frame, row, col):
        entry = Entry(frame, width=8, justify='center', textvariable=StringVar())
        entry.grid(row=row, column=col)
        return entry

    def load_file(self):
        f_name = tkFileDialog.askopenfilename(initialdir="./", title="Select a File")
        if(f_name != ''):

            file_in = open(f_name, 'r')

            lines = file_in.readlines()
            self.set_board(lines)

            (_, name) = os.path.split(f_name)
            self.set_status_bar_msg(name + ' loaded.')
            file_in.close()

    def save_file(self):

        self.update_board()

        file_out = tkFileDialog.asksaveasfile(mode='w',defaultextension='.txt')

        board = self.board_to_string()

        file_out.write(board)
        file_out.close()

    def board_to_string(self):
        board = ''
        for i in range(9):
            for j in range(9):
                board += str(self.the_board[i][j])
                board += ' '
            board += '\n'
        return board

    def set_board(self, lines):
        i = 0
        for line in lines:
            j = 0
            for num in line:
                if(num != ' ' and not ('\n' in num or '\r' in num)):
   
                    self.textfields[i][j].config(state=NORMAL)
                    self.textfields[i][j].delete(0, END)
                    
                    if(num != '0'):
                        self.the_board[i][j] = int(num)
                        self.textfields[i][j].insert(0, self.the_board[i][j])

                    else:
                        self.the_board[i][j] = 0
                    j += 1
            i += 1
            
    def update_board(self):
        for i in range(9):
            for j in range(9):
                cellContents = self.textfields[i][j].get()
                if(cellContents != ''):
                    
                    try:
                        n = int(cellContents)
                        
                        if(n > 0 and n < 10):
                            self.the_board[i][j] = n
                        else:
                            self.the_board[i][j] = 0
                            self.textfields[i][j].delete(0, END)

                    except ValueError: 
                        self.textfields[i][j].delete(0, END)
                else:
                    self.the_board[i][j] = 0

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.textfields[i][j].delete(0,END)
                self.the_board[i][j] = 0

    def set_status_bar_msg(self, msg):
        self.status_bar.config(state=NORMAL)
        self.status_bar.delete(0, END)
        self.status_bar.insert(0, msg)
        self.status_bar.config(state=DISABLED)
        
    def update_textfield(self, row, col):
        if(self.the_board[row][col] != 0):
            self.textfields[row][col].delete(0, END)
            self.textfields[row][col].insert(0, self.the_board[row][col])
        
    def update_all_textfields(self):
        for i in range(9):
            for j in range(9):
                self.update_textfield(i,j)

    ##########First Homework Assignment##########

    def check_board_validity(self):
 
        if self.boardIsOK():
            self.set_status_bar_msg("Board is valid")
        else:
            self.set_status_bar_msg("Board is invalid")

    def boardIsOK(self):

        self.update_board()

        for i in range(9):
            if not self.check_col(i) or not self.check_row(i) or not self.check_cluster(i):
                return False
        
        return True

    def check_col(self, col):

        numbers = [0] * 9

        for i in range(9):
            x = self.the_board[i][col]

            if (x != 0 and numbers[x - 1] != 0):
                return False
            
            else:
                numbers[x - 1] = x

        return True

    def check_row(self, row):
        
        numbers = [0] * 9

        for j in range(9):
            x = self.the_board[row][j]

            if (x != 0 and numbers[x - 1] != 0):
                return False
            
            else:
                numbers[x - 1] = x

        return True

    def check_cluster(self, cluster):
 
        initial_col = int(cluster % 3) * 3
        initial_row = int(cluster / 3) * 3
        
        numbers = [0] * 9

        for i in range(initial_row, initial_row + 3):
            for j in range(initial_col, initial_col + 3):
                x = self.the_board[i][j]

                if (x != 0):
                    if (numbers[x - 1] != 0):
                        return False
                    else:
                        numbers[x - 1] = x

        return True
    
    ##########END FIRST HOMEWORK ASSIGNMENT#########         

    ##########START SECOND HOMEWORK ASSIGNMENT##########

    def solve(self):
        
        class MyThread(threading.Thread):
            self.sudoku = ''
            def __init__(self, sudoku):
                threading.Thread.__init__(self)
                self.sudoku = sudoku
                
            def run(self):
                if(self.sudoku.boardIsOK()):
                    self.sudoku.set_status_bar_msg('Working...')
                    result = self.sudoku.solve_helper(0, 0)
                    if(result):
                        self.sudoku.set_status_bar_msg('Solved in ' + str(self.sudoku.guesses) + ' guesses.')
                self.sudoku.guesses = 0
                self.sudoku.update_all_textfields()
                        
        MyThread(self).start()

    def solve_helper(self, row, col):

        while self.the_board[row][col] != 0:
            col = col + 1
            if col == 9:
                col = 0
                row = row + 1
                if row == 9: return True

        for n in range(1, 10):
            self.set_cell(row, col, n)
            self.guesses += 1
        
            if self.check_cell(row, col):
                if self.solve_helper(row, col):
                    return True
        self.set_cell(row, col, 0)
        return False


    def set_cell(self, row, col, val):
        self.the_board[row][col] = val
        

        if(self.show_work_value.get()):
            self.update_textfield(row, col)

    def check_cell(self, row, col):
        cluster = int(row / 3) * 3 + int(col / 3)
        return self.check_col(col) and self.check_row(row) and self.check_cluster(cluster)

                
    ##########END SECOND HOMEWORK ASSIGNMENT##########

root = Tk()

app = Sudoku(root)

root.mainloop() 

