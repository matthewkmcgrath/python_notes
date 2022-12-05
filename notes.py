import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

# need a menu function
# need a notes function
# need a settings function

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_RED)
    CLASSICTERM = curses.color_pair(1)
    EYEBLEED = curses.color_pair(2)
    
    stdscr.clear()
    stdscr.border()
    stdscr.refresh()
    dimensions = stdscr.getmaxyx()
    y = dimensions[0]
    x = dimensions[1]
    three_fourths_x = ((x//4)*3)
    one_fourth_x = (x//4)
    top = 0

    filename = "2022-12-03.txt"

    file_manager(y, x, one_fourth_x, top)

    yeah = notes(y, x, three_fourths_x, one_fourth_x, top, filename)

    with open('notes_curses/notes.txt', 'w') as f:
        f.write(yeah)

    
    #win = curses.newwin(18, 3, 2, 2)


    #stdscr.attron(CLASSICTERM) # activates attribute CLASSICTERM
    #rectangle(stdscr, 1, 1, 5, 20) # draws rectangle with attribute CLASSICTERM
    #pad = curses.newpad(100,100) # creates pad
    #box = Textbox(win) # creates textbox within window
    #stdscr.refresh() # refreshes screen
    #box.edit() 
    #stdscr.attroff(CLASSICTERM)
    #stdscr.refresh()
    
def notes(y, x, three_fourths_x, one_fourth_x, top, filename):
    
    three_fourths_x_plus_three = ((x//4)*3) + 3 # 3/4 of the screen width, + 3
    one_fourth_x = (x//4) # 1/4 of the screen width
    half_x = ((three_fourths_x//2)-int((len(filename)/2))) # centers the filename in the middle of window
    height = y - 2 # height of window
    width = three_fourths_x_plus_three - 2 # width of notes window
    top_y_coordinate = top + 1
    left_x_coordinate = one_fourth_x
    notes_window = curses.newwin(height, width, top_y_coordinate, left_x_coordinate)
    notepad_height = height - 6
    notepad_width = width - 4
    notepad_top_y_coordinate = top_y_coordinate + 2
    notepad_left_x_coordinate = left_x_coordinate + 2
    notepad_window = curses.newwin(notepad_height, notepad_width, notepad_top_y_coordinate, notepad_left_x_coordinate)
    #rectangle(notes_window, 0, 0, 40, 10)
    notes_window.border()
    box = Textbox(notepad_window)
    notes_window.addstr(top, half_x, filename)
    notes_window.refresh()
    box.edit()
    note = box.gather()
    return note

def file_manager(y, x, one_fourth_x, top):
    height = y - 2
    width = one_fourth_x - 2
    top_y_coordinate = top + 1
    left_x_coordinate = 2
    file_manager_window = curses.newwin(height, width, top_y_coordinate, left_x_coordinate)
    file_manager_window.border()
    file_manager_window.addstr(5, 3, "file manager to be here")
    file_manager_window.refresh()

def resize():
    stdscr.refresh()
    dimensions = stdscr.getmaxyx()
    stdscr.addstr(str(dimensions))
    time.sleep(.02)
    stdscr.getch()
    stdscr.getch()
    stdscr.resize(dimensions[0], dimensions[1])
    stdscr.addstr(str(dimensions))
    stdscr.refresh()
    stdscr.getch()

wrapper(main)