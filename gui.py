#!/usr/bin/python3

import tkinter
from tkinter import font
import sys
import os
from logic import Board, Program

# stack for moves

moves = []

class Application(tkinter.Canvas):
        def __init__(self, master=None):
            super().__init__(master)
            self.master.configure(highlightthickness=0, borderwidth=0)
            self.master.title('Tic Tac Toe')
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.initialize_player()
            self.font = font.Font(family="Helvetica", weight = 'bold')
            self.avatar = None
            self.program = None
            self.buttons = []
            self.turn = None # 0 for program, 1 for human
            self.game = Board()

        def initialize_player(self):
            self.label = tkinter.Label(self.master, text='Choose a player. X goes first')
            self.label.grid(row=2, sticky='W')
            self.oval = tkinter.Button(self.master, text='0', width=4, height=4)
            self.oval.bind('<Button-1>', self._oval)
            self.oval.grid(row=3, column=4)
            self.exe = tkinter.Button(self.master, text='X' , width=4, height=4)
            self.exe.bind('<Button-1>', self._exe)
            self.exe.grid(row=3, column=5)
            #self.create_board()

        def create_board(self):
            self.oval.destroy()
            self.exe.destroy()
            self.label.destroy()
            for index, position in enumerate(self.game.positions):
                if index < 3:
                    self.button = tkinter.Button(self.master, text='.', width=4, height=4, font=self.font,
                        command= lambda pos = index: self.draw(pos))
                    self.button.grid(row=0, column=index)
                elif index >= 3 and index < 6:
                    self.button = tkinter.Button(self.master, text='.', width=4, height=4, font=self.font,
                        command= lambda pos = index: self.draw(pos))
                    self.button.grid(row=1, column=index%3)
                else:
                    self.button = tkinter.Button(self.master, text='.', width=4, height=4, font=self.font,
                        command= lambda pos = index: self.draw(pos))
                    self.button.grid(row=2, column=index%3)
                self.buttons.append(self.button)

            self._quit = tkinter.Button(self.master, text='Quit', command=self._quit, height=2, width=2).grid(row=7, column=0)
            self._undo = tkinter.Button(self.master, text='Undo', command=self._undo, height=2, width=2).grid(row=7, column=4)
           

        def _quit(self):
                sys.exit(1)

        def _undo(self):
            self.game = Board
            self.update()
        def _oval(self, event):
            event.widget.destroy()
            self.set_avatar('0')
            self.program = self.get_opponent('0')
            self.turn = 0
            self.create_board()
            self.first_move()
            return 
        def _exe(self, event):
            event.widget.destroy()
            self.set_avatar('X')
            self.program = self.get_opponent('X')
            self.turn = 1
            self.create_board()
            return

        def set_avatar(self, icon):
            self.avatar = icon
            return self.avatar


        def draw(self, position):
            print(self.turn)
            if self.turn == 1:
                self.human_player(position)
                self.program_move()
                self.turn = 0
            elif self.turn == 0:
                self.program_move()
#                self.turn = 1

            return True


        def program_move(self):
            state, winner = self.game.game_over()
            self.turn = 1
            if not state:
                program = Program(self.game, self.program)
                score = program.minimax(self.game, self.avatar)
                move = program.choice
                self.buttons[move].configure(text = self.program, state='disabled')
                self.buttons[move]['disabledforeground'] = 'black'
                self.game.positions[move] = self.program
                self.buttons[move].update()
                return True
            else:
                move = None
                return move


        def first_move(self):
            program = Program(self.game, self.program)
            score = program.minimax(self.game, self.avatar)
            move = program.choice
            self.buttons[move].configure(text = self.program, state='disabled')
            self.buttons[move]['disabledforeground'] = 'black'
            self.game.positions[move] = self.program
            self.turn = 1

        def get_opponent(self, player):
            if player == 'X':
                opponent = '0'
            else:
                opponent = 'X'
            return opponent

        def human_player(self, position):
            self.buttons[position].configure(text = self.avatar, state='disabled')
            self.buttons[position]['disabledforeground'] = 'black'
            self.game.positions[position] = self.avatar
            self.buttons[position].update()
            print('move')



root = tkinter.Tk()
root.geometry('300x400')
app = Application(master=root)

if __name__ == '__main__':
    try:
        app.mainloop()
    except Exception as e:
        raise
