from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
import random
import math


class GameBoard(GridLayout):

    # Override the initialization
    def __init__(self, **kwargs):
    
        # Call the super constructor and then set the number of columns
        super(GameBoard, self).__init__(**kwargs)
        self.cols = 4
        self.rows = 4
        
        # Create the 2D array to store the board
        self.game_board = [[0 for x in range(4)] for x in range(4)]

        # Add the grid of blocks (first row)
        self.c11 = Label(text='11')
        self.add_widget(self.c11)
        self.c12 = Label(text='12')
        self.add_widget(self.c12)
        self.c13 = Label(text='13')
        self.add_widget(self.c13)
        self.c14 = Label(text='14')
        self.add_widget(self.c14)

        # Add the grid of blocks (second row)
        self.c21 = Label(text='21')
        self.add_widget(self.c21)
        self.c22 = Label(text='22')
        self.add_widget(self.c22)
        self.c23 = Label(text='23')
        self.add_widget(self.c23)
        self.c24 = Label(text='24')
        self.add_widget(self.c24)

        # Add the grid of blocks (third row)
        self.c31 = Label(text='31')
        self.add_widget(self.c31)
        self.c32 = Label(text='32')
        self.add_widget(self.c32)
        self.c33 = Label(text='33')
        self.add_widget(self.c33)
        self.c34 = Label(text='34')
        self.add_widget(self.c34)

        # Add the grid of blocks (fourth row)
        self.c41 = Label(text='41')
        self.add_widget(self.c41)
        self.c42 = Label(text='42')
        self.add_widget(self.c42)
        self.c43 = Label(text='43')
        self.add_widget(self.c43)
        self.c44 = Label(text='44')
        self.add_widget(self.c44)

        # Add the keyboard listener
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        # Initialize the board
        self._initialize_board()

        # Update the board
        self._update_board()

    # Function for releasing the keyboard
    def _keyboard_closed(self):
        
        print('My keyboard has been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    
    # Function for listening to the key presses
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        
        # Keycode is composed of an integer + a string
        print('The key', keycode, 'have been pressed')
        
        # Update the board if the down arrow is pressed
        if keycode[1] == 'down':
            self._down_move()
            self._add_new_block()
            self._update_board()
        
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()
        
        # Return True to accept the key. Otherwise, it will be used by the system.
        return True

    # Function for initializing the game board
    def _initialize_board(self):
        
        row_ind = random.randint(0,3)
        col_ind = random.randint(0,3)
        rand_num = random.randint(0,1)
    
        if rand_num == 0:
            self.game_board[row_ind][col_ind] = 2
        else:
            self.game_board[row_ind][col_ind] = 4

    # Function for adding new block
    def _add_new_block(self):
    
        open_space = 0
        
        while open_space == 0:
    
            row_ind = random.randint(0,3)
            col_ind = random.randint(0,3)
        
            if self.game_board[row_ind][col_ind] == 0:
        
                open_space = 1
        
        rand_num = random.randint(0,1)
        
        if rand_num == 0:
            self.game_board[row_ind][col_ind] = 2
        else:
            self.game_board[row_ind][col_ind] = 4

    # Function for updating the game board
    def _update_board(self):

        # Update the first row
        self.c11.text=str(self.game_board[0][0])
        self.c12.text=str(self.game_board[0][1])
        self.c13.text=str(self.game_board[0][2])
        self.c14.text=str(self.game_board[0][3])
        
        # Update the second row
        self.c21.text=str(self.game_board[1][0])
        self.c22.text=str(self.game_board[1][1])
        self.c23.text=str(self.game_board[1][2])
        self.c24.text=str(self.game_board[1][3])
        
        # Update the third row
        self.c31.text=str(self.game_board[2][0])
        self.c32.text=str(self.game_board[2][1])
        self.c33.text=str(self.game_board[2][2])
        self.c34.text=str(self.game_board[2][3])
        
        # Update the fourth row
        self.c41.text=str(self.game_board[3][0])
        self.c42.text=str(self.game_board[3][1])
        self.c43.text=str(self.game_board[3][2])
        self.c44.text=str(self.game_board[3][3])

    # Function for calculating down move
    def _down_move(self):
        
        # Create the 2D array to store the board
        new_game_board = [[0 for x in range(4)] for x in range(4)]

        # Move the rows down
        for col_ind in range(0,4):

            temp_ind = 3;

            for row_ind in range(3,-1,-1):

                if self.game_board[row_ind][col_ind] != 0:
    
                    new_game_board[temp_ind][col_ind] = self.game_board[row_ind][col_ind]
                    temp_ind = temp_ind - 1

        # Combine like blocks
        for col_ind in range(0,4):
            
            row_ind_cond = 3
            
            while row_ind_cond != 0:
            
                if new_game_board[row_ind_cond][col_ind] == new_game_board[row_ind_cond-1][col_ind]:
            
                    new_game_board[row_ind_cond][col_ind] = 2*new_game_board[row_ind_cond-1][col_ind]

                    for row_ind in range(row_ind_cond-1,0,-1):

                        new_game_board[row_ind][col_ind] = new_game_board[row_ind-1][col_ind]
            
                    new_game_board[0][col_ind] = 0

                row_ind_cond = row_ind_cond - 1

        self.game_board = new_game_board

class Run2048(App):
    
    def build(self):
        return GameBoard()


if __name__ == '__main__':
    Run2048().run()