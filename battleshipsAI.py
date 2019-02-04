# Battleships + GUI
# Ben Cully
# 1/22/2019

'This is a simple human versus computer battleships game.'
'The number of ships is 5 at lengths [2,3,3,4,5].'
'To start we first need to place the ships using  l(x,y)  format.'
'Next we start the hunt phase and so does the program "Hunt Mode" to find targets.'
'This next phase "Target Mode" is used by the program to sink revealed ships.'

import tkinter as Tk



class Application(Frame):
    'Main Application'
    
    def __init__(self, Frame):
        'Intializer'
        Frame.__init__(self,master)
        self.launch()
        self.master = master




def start():
    window = Tk()
    window.title('BattleShips with AI')
    window.geometry('500x500')
    menu = Menu(window)
    new_item = Menu(menu)
    new_item.add_command(label='New')
    new_item.add_command(label='Exit')
    menu.add_cascade(label='File', menu=new_item)
    window.config(menu=menu)
    lbl = Label(window, text='Enter your positions', font=('Helvetica', 25))
    lbl.grid(column=0, row=0)
    ship5 = Entry(window, width=6)
    ship5.grid(column=1, row=0)
    ship4 = Entry(window, width=6)
    ship4.grid(column=1, row=1)
    ship3_1 = Entry(window, width=6)
    ship3_1.grid(column=1, row=2)
    ship3_2 = Entry(window, width=6)
    ship3_2.grid(column=1, row=3)
    ship2 = Entry(window, width=6)
    ship2.grid(column=1, row=4)




def ship(length):
    global Board
    ships = ['Submarine', 'Cruiser']
    random.shuffle(ships)
    printBoard(Board)
    if length == 2:
        shipType = 'Destroyer'
    elif length == 3:
        shipType = ships[0]
    elif length == 3:
        shipType = ships[1]
    elif length == 4:
        shipType = 'Battleship'
    elif length == 5:
        shipType = 'Carrier'
    print('Ship type : ' + shipType)
    print('Ship length : ' + str(length))
    print('Pick starting position:')
    place = input()
    if len(place) < 3:
        print('Pick orientation(R, L, U or D)')
        dir = input()
        if dir == 'r':
            endPlace = place[0] + str((int(place[1]) + length))
            if (place in Board) and (endPlace in Board) and (Board[endPlace] == '_') and (Board[place] == '_'):
                for i in range(length):
                    if Board[place[0] + str(int(place[1]) + i)] == '_':
                        Board[place[0] + str(int(place[1]) + i)] = 'o'
                    else:
                        print('Bad1')
                        Board = dict.fromkeys(Board, '_')
                        start()
                
            else:
                print('Bad1')
                start()
    
        elif dir == 'l':
            endPlace = place[0] + str((int(place[1]) - length))
            if (place in Board) and (endPlace in Board) and (Board[endPlace] == '_') and (Board[place] == '_'):
                for i in range(length):
                    if Board[place[0] + str(int(place[1]) - i)] == '_':
                        Board[place[0] + str(int(place[1]) - i)] = 'o'
                    else:
                        print('Bad2')
                        Board = dict.fromkeys(Board, '_')
                        start()
                
            else:
                print('Bad1')
                start()
    
        elif dir == 'u':
            if (place in Board) and (Board[place] == '_'):
                for i in range(length):
                    if place[0] == 'a':
                        letterPos = 0
                        
                    if place[0] == 'b':
                        letterPos = 1
                        
                    if place[0] == 'c':
                        letterPos = 2
                        
                    if place[0] == 'd':
                        letterPos = 3
                        
                    if place[0] == 'e':
                        letterPos = 4
                        
                    if place[0] == 'f':
                        letterPos = 5
                        
                    if place[0] == 'g':
                        letterPos = 6
                        
                    if place[0] == 'h':
                        letterPos = 7
                        
                    if place[0] == 'i':
                        letterPos = 8
                        
                    if place[0] == 'j':
                        letterPos = 9
                        
                    if letterPos < length - 1: #or (letterPos > (9 - length) + 1):
                        print('Bad2')
                        quit()
                        
                    endLetterPos = letterPos - i
                    
                    if endLetterPos == 0:
                        endLetter = 'a'
                        
                    if endLetterPos == 1:
                        endLetter = 'b'
                        
                    if endLetterPos == 2:
                        endLetter = 'c'
                        
                    if endLetterPos == 3:
                        endLetter = 'd'
                        
                    if endLetterPos == 4:
                        endLetter = 'e'
                        
                    if endLetterPos == 5:
                        endLetter = 'f'
                        
                    if endLetterPos == 6:
                        endLetter = 'g'
                        
                    if endLetterPos == 7:
                        endLetter = 'h'
                        
                    if endLetterPos == 8:
                        endLetter = 'i'
                        
                    if endLetterPos == 9:
                        endLetter = 'j'
                        
                    if Board[endLetter + place[1]] == '_':
                        Board[endLetter + place[1]] = 'o'
                    else:
                        print('Bad3')
                        Board = dict.fromkeys(Board, '_')
                        start()

            else:
                print('Bad1')
                start()
    
        elif dir == 'd':
            if (place in Board) and (Board[place] == '_'):
                for i in range(length):
                    if place[0] == 'a':
                        letterPos = 0
                        
                    if place[0] == 'b':
                        letterPos = 1
                        
                    if place[0] == 'c':
                        letterPos = 2
                        
                    if place[0] == 'd':
                        letterPos = 3
                        
                    if place[0] == 'e':
                        letterPos = 4
                        
                    if place[0] == 'f':
                        letterPos = 5
                        
                    if place[0] == 'g':
                        letterPos = 6
                        
                    if place[0] == 'h':
                        letterPos = 7
                        
                    if place[0] == 'i':
                        letterPos = 8
                        
                    if place[0] == 'j':
                        letterPos = 9
                        
                    if (letterPos > (9 - length) + 1):
                        print('Bad2')
                        quit()
                        
                    endLetterPos = letterPos + i
                    
                    if endLetterPos == 0:
                        endLetter = 'a'
                        
                    if endLetterPos == 1:
                        endLetter = 'b'
                        
                    if endLetterPos == 2:
                        endLetter = 'c'
                        
                    if endLetterPos == 3:
                        endLetter = 'd'
                        
                    if endLetterPos == 4:
                        endLetter = 'e'
                        
                    if endLetterPos == 5:
                        endLetter = 'f'
                        
                    if endLetterPos == 6:
                        endLetter = 'g'
                        
                    if endLetterPos == 7:
                        endLetter = 'h'
                        
                    if endLetterPos == 8:
                        endLetter = 'i'
                        
                    if endLetterPos == 9:
                        endLetter = 'j'

                    if Board[endLetter + place[1]] == '_':
                        Board[endLetter + place[1]] = 'o'
                    else:
                        print('Bad3')
                        Board = dict.fromkeys(Board, '_')
                        start()

            else:
                print('Bad1')
                start()
start()
