import tkinter
import random

# notes for further improvement 
# 1. add an actually good bot. using random is just an lazy solution.
# 2. make the pop up windows interesting and adjust the position as its generated
# 3. idk probably add animation
# 4. make a character selection so the player can choose O or X

WIDTH = 6
PERCENT_X = 0.405
PERCENT_Y = 0.345

BG_COLOR = '#99b3de'
OFFSET_X = 0.283 # vertical lines x position
LINE_COLOR = '#6f8dbd'
CELL_COLOR = {' ':'black', 'O':'white', 'X':'#776e65'}
i = 20 # extra length

def popupmsg(msg):
    top = tkinter.Toplevel()
    top.geometry('200x70')
    top.resizable(0,0)
    
    tkinter.Message(top, text=msg, font=("Helvetica", 10)).pack()
    button = tkinter.Button(top, text="Ok", command=top.destroy, width=10, height=1)
    button.pack()
    button.bind('<Button-1>', restart_game)
    
def extract_text(grid_object):
    matrix = []
    for i in range(3):
        grid_row = [grid_object[i][j].itemcget(label, 'text') for j in range(3)]
        matrix.append(grid_row)
    return matrix

def print_grid(grid_object):
    matrix = extract_text(grid_object)
    for i in range(3):
        print('[', end='')
        for j in range(3):
            print(matrix[i][j]+' ', end='')
        print(']')

def fill_grid(value, position):
    if position == '00':
        grid_cells[0][0].itemconfig(label, text=value, fill=CELL_COLOR[value])
    elif position == '01':
        grid_cells[0][1].itemconfig(label, text=value, fill=CELL_COLOR[value])
    elif position == '02':
        grid_cells[0][2].itemconfig(label, text=value, fill=CELL_COLOR[value])
    elif position == '10':
        grid_cells[1][0].itemconfig(label, text=value, fill=CELL_COLOR[value])
    elif position == '11':
        grid_cells[1][1].itemconfig(label, text=value, fill=CELL_COLOR[value])
    elif position == '12':
        grid_cells[1][2].itemconfig(label, text=value, fill=CELL_COLOR[value])
    elif position == '20':
        grid_cells[2][0].itemconfig(label, text=value, fill=CELL_COLOR[value])
    elif position == '21':  
        grid_cells[2][1].itemconfig(label, text=value, fill=CELL_COLOR[value])
    elif position == '22':
        grid_cells[2][2].itemconfig(label, text=value, fill=CELL_COLOR[value])

# checking if a certain grid/cell empty or not
def cell_check(array_pos):
    global global_counter
    if array_pos == ' ' : # if empty
        global_counter += 1
        return True
    else:
        return False
    
def win_condition():
    matrix = extract_text(grid_cells)
    if matrix[0] in (['O', 'O', 'O'], ['X', 'X', 'X']):
        popupmsg(matrix[0][0]+' Wins!')
    elif matrix[1] in (['O', 'O', 'O'], ['X', 'X', 'X']):
        popupmsg(matrix[1][0]+' Wins!')
    elif matrix[2] in (['O', 'O', 'O'], ['X', 'X', 'X']):
        popupmsg(matrix[2][0]+' Wins!')
    elif [matrix[0][0], matrix[1][0], matrix[2][0]] in (['O', 'O', 'O'], ['X', 'X', 'X']):
        popupmsg(matrix[0][0]+' Wins!')
    elif [matrix[0][1], matrix[1][1], matrix[2][1]] in (['O', 'O', 'O'], ['X', 'X', 'X']):
        popupmsg(matrix[0][1]+' Wins!')
    elif [matrix[0][2], matrix[1][2], matrix[2][2]] in (['O', 'O', 'O'], ['X', 'X', 'X']):
        popupmsg(matrix[0][2]+' Wins!')
    elif [matrix[0][0], matrix[1][1], matrix[2][2]] in (['O', 'O', 'O'], ['X', 'X', 'X']):
        popupmsg(matrix[0][0]+' Wins!')
    elif [matrix[0][2], matrix[1][1], matrix[2][0]] in (['O', 'O', 'O'], ['X', 'X', 'X']):
        popupmsg(matrix[0][2]+' Wins!')
    else:
        counter = 0
        for i in range(3):
            for j in range(3):
                if matrix[i][j] != ' ': counter += 1
        if counter == 9:
            popupmsg('Draw!')

def update_grid(event, position, opt):
    global grid_cells
    global global_counter
    user_input = ''
    
    # O or X assignment
    if global_counter%2 == 0:
        user_input = 'O' 
    else:
        user_input = 'X'

    if global_counter < 10:
        if position == '00':
            if cell_check(extract_text(grid_cells)[0][0]): fill_grid(user_input, '00')
        elif position == '01':
            if cell_check(extract_text(grid_cells)[0][1]): fill_grid(user_input, '01')
        elif position == '02':
            if cell_check(extract_text(grid_cells)[0][2]): fill_grid(user_input, '02')
        elif position == '10':
            if cell_check(extract_text(grid_cells)[1][0]): fill_grid(user_input, '10')
        elif position == '11':
            if cell_check(extract_text(grid_cells)[1][1]): fill_grid(user_input, '11')
        elif position == '12':
            if cell_check(extract_text(grid_cells)[1][2]): fill_grid(user_input, '12')
        elif position == '20':
            if cell_check(extract_text(grid_cells)[2][0]): fill_grid(user_input, '20')
        elif position == '21':
            if cell_check(extract_text(grid_cells)[2][1]): fill_grid(user_input, '21')
        elif position == '22':
            if cell_check(extract_text(grid_cells)[2][2]): fill_grid(user_input, '22')

        if opt == '1': # for single player
            while True:
                x, y = [random.randint(0, 2) for i in range(2)]
                if global_counter == 9:
                    break
                if cell_check(extract_text(grid_cells)[x][y]):
                    fill_grid('X', str(x)+str(y))
                    break       

    win_condition()
    
def restart_game(event):
    global global_counter
    v.set('0')
    global_counter = 0
    fill_grid(' ', '00')
    fill_grid(' ', '01')
    fill_grid(' ', '02')
    fill_grid(' ', '10')
    fill_grid(' ', '11')
    fill_grid(' ', '12')
    fill_grid(' ', '20')
    fill_grid(' ', '21')
    fill_grid(' ', '22')

def rb_value_single(event):
    global value
    value = '1'

def rb_value_two(event):
    global value
    value = '0'
    
# ------------------------------- main -------------------------------
# -------------------- Graphics -------------------- 
root = tkinter.Tk()
root.geometry('500x400')
root.title('Tic Tac Toe')
root.resizable(0, 0)

top_frame = tkinter.Frame(root, bg='white', width=500, height=70)
top_frame.pack(side='top')

canvas = tkinter.Canvas(root, width=510, height=280, bg=BG_COLOR, bd=0, highlightthickness=0)
canvas.place(relx=0, rely=0.175)

bottom_frame = tkinter.Frame(root, bg='white', width=500, height=50, cursor='hand2')
bottom_frame.pack(side='bottom')

label_restart = tkinter.Label(bottom_frame, text='RESTART GAME', font=('calibri', 12, 'bold'), bg='white', fg=LINE_COLOR, cursor='hand2')
label_restart.place(relx=0.4, rely=0.25)

# radio buttons
v = tkinter.IntVar()
rb_single = tkinter.Radiobutton(top_frame, text="Single Player", font=('calibri', 15, 'bold'), variable=v, value=0, # just for the sake of look
                                fg='#6b6b6b', bg='white', highlightbackground='white', takefocus=False)
rb_two = tkinter.Radiobutton(top_frame, text="Two Players",  font=('calibri', 15, 'bold'), variable=v, value=1,
                             fg='#6b6b6b', bg='white', highlightbackground='white', takefocus=False)

rb_single.place(relx=0.08, rely=0.2)
rb_two.place(relx=0.65, rely=0.2)

# vertical lines
canvas.create_line(510*PERCENT_X, 20, 510*PERCENT_X, 260, width=WIDTH, fill=LINE_COLOR)
canvas.create_line(510-(510*PERCENT_X), 20, 510-(510*PERCENT_X), 260, width=WIDTH, fill=LINE_COLOR)

# horizontal lines
canvas.create_line(0+(510*OFFSET_X)-i, 280*PERCENT_Y, 240+(510*OFFSET_X), 280*PERCENT_Y, width=WIDTH, fill=LINE_COLOR)
canvas.create_line(0+(510*OFFSET_X)-i, 280-(280*PERCENT_Y), 240+(510*OFFSET_X), 280-(280*PERCENT_Y), width=WIDTH, fill=LINE_COLOR)

# cells
coordinates = [[(0.244,0.231),(0.43,0.231),(0.615,0.231)],
               [(0.244,0.435),(0.43,0.435),(0.615,0.435)],
               [(0.244,0.645),(0.43,0.645),(0.615,0.645)]]
grid_cells = []
for i in range(3):
    grid_row = []
    for j in range(3):
        X, Y = coordinates[i][j]
        cv = tkinter.Canvas(root, width=80, height=70, bg=BG_COLOR, bd=0, highlightthickness=0)
        cv.place(relx=X, rely=Y)

        label = cv.create_text(40, 35, text=' ', font=('clear sans', 60, 'bold'))
        grid_row.append(cv)

    grid_cells.append(grid_row)
# -------------------------------------------------
# Logic
value = '1' # for single player
global_counter = 0

rb_single.focus_set()
rb_two.focus_set()

rb_single.bind('<Button-1>', rb_value_single)
rb_two.bind('<Button-1>', rb_value_two) 

grid_cells[0][0].bind('<Button-1>', lambda event: update_grid(event, '00', value))
grid_cells[0][1].bind('<Button-1>', lambda event: update_grid(event, '01', value))
grid_cells[0][2].bind('<Button-1>', lambda event: update_grid(event, '02', value))

grid_cells[1][0].bind('<Button-1>', lambda event: update_grid(event, '10', value))
grid_cells[1][1].bind('<Button-1>', lambda event: update_grid(event, '11', value))
grid_cells[1][2].bind('<Button-1>', lambda event: update_grid(event, '12', value))

grid_cells[2][0].bind('<Button-1>', lambda event: update_grid(event, '20', value))
grid_cells[2][1].bind('<Button-1>', lambda event: update_grid(event, '21', value))
grid_cells[2][2].bind('<Button-1>', lambda event: update_grid(event, '22', value))

# restart game
label_restart.focus_set()
bottom_frame.focus_set()

label_restart.bind('<Button-1>', restart_game)
bottom_frame.bind('<Button-1>', restart_game)

root.mainloop()
