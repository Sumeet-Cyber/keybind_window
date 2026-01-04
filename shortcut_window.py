#!/home/sumeetj/space/code/projects/alternate_screen_buffer_window/venv/bin/python

import curses
from prettytable import PrettyTable

table_margin = 2

def recalculated_heading_arr(heading, size):
    heading_arr  = []
    for i in heading.split('\n'):
        print(i)
        if len(i) < size:
            heading_arr.append(i + ' ' * (size - len(i)))
        else:
            heading_arr.append(i)
    return heading_arr

hypr_heading = r'''
 _   _                  _                 _ 
| | | |_   _ _ __  _ __| | __ _ _ __   __| |
| |_| | | | | '_ \| '__| |/ _` | '_ \ / _` |
|  _  | |_| | |_) | |  | | (_| | | | | (_| |
|_| |_|\__, | .__/|_|  |_|\__,_|_| |_|\__,_|
       |___/|_| 
'''
hypr_sc = [
        [ 'A', 'Code Editor', ''],
        [ 'B', 'Brightness Up', 'Brightness Down'],
        [ 'C', 'Kill Active', ''],
        [ 'D', 'Toggle Split', ''],
        [ 'E', 'File Manager', ''],
        [ 'F', '', ''],
        [ 'G', '', ''],
        [ 'H', 'Move Focus Left', ''],
        [ 'G', '', ''],
        [ 'I', '', ''],
        [ 'J', '', ''],
        [ 'K', '', ''],
        [ 'L', '', ''], 
        [ 'M', '', ''], 
        [ 'N', '', ''], 
        [ 'O', '', ''], 
        [ 'P', '', ''], 
        [ 'Q', '', ''], 
        [ 'R', '', ''], 
        [ 'S', '', ''],
        [ 'T', '', ''],
        [ 'U', '', ''], 
        [ 'V', '', ''], 
        [ 'W', '', ''], 
        [ 'X', '', ''], 
        [ 'Y', '', ''], 
        [ 'Z', '', ''], 
        [ 'F5', '', ''],
        [ ';', '', ''],
        [ 'Print', '', ''], 
        [ 'Print', '', ''],
        [ 'Up', '', ''], 
        [ 'Down', '', ''], 
        [ 'Left', '', ''], 
        [ 'Right', '', ''], 
        [ '', '', ''], 
        ]


hypr_table = PrettyTable()
hypr_table.field_names = ['Key', 'Action', 'Shift']
hypr_table.max_width = {'Action':40, 'Shift':40}
hypr_table.add_rows(hypr_sc)
hypr_table_arr = str(hypr_table).split('\n')
hypr_table_width = len(hypr_table_arr[0])
hypr_heading_arr = recalculated_heading_arr(hypr_heading, hypr_table_width)
# print(hypr_heading_arr)
hypr_table_arr = hypr_heading_arr + hypr_table_arr
hypr_table_arr.insert(0, ' ' * hypr_table_width)
hypr_table_arr.insert(len(hypr_table_arr), ' ' * hypr_table_width)
print('hypr table width: ', hypr_table_width)
# print(hypr_table)


kitty_heading = r"""
 _  ___ _   _         
| |/ (_) |_| |_ _   _ 
| ' /| | __| __| | | |
| . \| | |_| |_| |_| |
|_|\_\_|\__|\__|\__, |
                |___/
"""
# Set up shortcut table for kitty -
kitty_sc = [
    [' --- Scrolling ---', ''],
    ['',''],
    ['Ctrl + Shift + Up', 'Scroll line up'],
    ['Ctrl + Shift + Down', 'Scroll line down'],
    ['Ctrl + Shift + Page-Up', 'Scroll page up'],
    ['Ctrl + Shift + Page-Down', 'Scroll page down'],
    ['Ctrl + Shift + Home', 'Scroll to top'],
    ['Ctrl + Shift + End', 'Scroll to bottom'],
    ['',''],
    [' --- Tabs management ---', ''],
    ['',''],
    ['Ctrl + Shift + T', 'New tab'],
    ['Ctrl + Shift + Q', 'Close tab'],
    ['Ctrl + Shift + Right', 'Next tab'],
    ['Ctrl + Shift + Left', 'Previous tab'],
    ['Ctrl + Shift + .', 'Move tab forward'],
    ['Ctrl + Shift + ,', 'Move tab backward'],
    ['Ctrl + Shift + Alt + T', 'Set tab title'],
    ['',''],
    [' --- Other keyboard shortcuts ---', ''],
    ['',''],
    ['Ctrl + Shift + C', 'Copy to clipboard'],
    ['Ctrl + Shift + V', 'Paste from clipboard'],
    ['Ctrl + Shift + S', 'Paste from selection'],
    ['Ctrl + Shift + Equal', 'Increase font size'],
    ['Ctrl + Shift + Minus', 'Decrease font size'],
    ['Ctrl + Shift + Backspace', 'Restore font size'],
    ['Ctrl + Shift + F11', 'Toggle fullscreen'],
    ['Ctrl + Shift + F10', 'Toggle maximized'],
    ['Ctrl + Shift + U', 'Input unicode character'],
    ['Ctrl + Shift + E', 'Click URL with keyboard'],
    ['Ctrl + Shift + Delete', 'Reset the terminal'],
    ['Ctrl + Shift + F5', 'Reload kitty.conf'],
    ['Ctrl + Shift + F6', 'Debug kitty.conf'],
    ['Ctrl + Shift + O', 'Pass selection to program'],
    ['Ctrl + Shift + F2', 'Edit kitty config file'],
    ['Ctrl + Shift + F1', 'View kitty docs in browser'],
    ['Ctrl + Shift + Escape', 'Open a kitty shell'],
    ['Ctrl + Shift + A > M', 'Increase background opacity'],
    ['Ctrl + Shift + A > L', 'Decrease background opacity'],
    ['Ctrl + Shift + A > 1', 'Full background opacity'],
    ['Ctrl + Shift + A > D', 'Reset background opacity'],
    ['',''],
    [' --- Shell integration ---',''],
    ['',''],
    ['Ctrl + Shift + G', 'View output of last command'],
    ['Ctrl + Shift + Z', 'Prev prompt in scrollback'],
    ['Ctrl + Shift + X', 'Next prompt in scrollback'],
    ['',''],
    [' --- Windows management ---',''],
    ['',''],
    ['Ctrl + Shift + Enter', 'New window'],
    ['Ctrl + Shift + L', 'Switch to next layout'],
    ['Ctrl + Shift + N', 'New OS window'],
    ['Ctrl + Shift + W', 'Close window'],
    ['Ctrl + Shift + ]', 'Next window'],
    ['Ctrl + Shift + [', 'Previous window'],
    ['Ctrl + Shift + F', 'Move window forward'],
    ['Ctrl + Shift + B', 'Move window backward'],
    ['Ctrl + Shift + `', 'Move window to top'],
    ['Ctrl + Shift + 1', 'Focus specific window 1'],
    ['Ctrl + Shift + 2', 'Focus specific window 2'],
    ['Ctrl + Shift + 3', 'Focus specific window 3'],
    ['Ctrl + Shift + 4', 'Focus specific window 4'],
    ['Ctrl + Shift + 5', 'Focus specific window 5'],
    ['Ctrl + Shift + 6', 'Focus specific window 6'],
    ['Ctrl + Shift + 7', 'Focus specific window 7'],
    ['Ctrl + Shift + 8', 'Focus specific window 8'],
    ['Ctrl + Shift + 9', 'Focus specific window 9'],
    ['Ctrl + Shift + 0', 'Focus specific window 10']
]

kitty_table = PrettyTable()
kitty_table.field_names = ['Keys', 'Action']
kitty_table.max_width = {'Keys':40, 'Action':40}
kitty_table.add_rows(kitty_sc)
kitty_table_arr = str(kitty_table).split('\n')
kitty_table_width = len(kitty_table_arr[0])
kitty_heading_arr = recalculated_heading_arr(kitty_heading, kitty_table_width)
kitty_table_arr = kitty_heading_arr + kitty_table_arr
kitty_table_arr.insert(0, ' ' * kitty_table_width)
kitty_table_arr.insert(len(kitty_table_arr), ' ' * kitty_table_width)

# print(kitty_table_arr[21])
for i in recalculated_heading_arr(kitty_heading, kitty_table_width):
    print(len(i))

# Main function to navigate through alternate screen buffer-
def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()
    stdscr.refresh()

    hypr_pad = curses.newpad(len(hypr_table_arr) + 1, hypr_table_width)
    for row in range(len(hypr_table_arr)):
        hypr_pad.addstr(hypr_table_arr[row])

    kitty_pad = curses.newpad(len(kitty_table_arr) + 1, kitty_table_width)
    for row in range(len(kitty_table_arr)):
        kitty_pad.addstr(kitty_table_arr[row])

    global table_margin
    hypr_y = kitty_y = 0
    hypr_pointer = kitty_pointer = 0
    case2 = False
    # Case - 1 -- Both tables side by side
    if (width - hypr_table_width -  (3 * table_margin)) >= kitty_table_width:
        table_margin = (width - hypr_table_width - kitty_table_width) // 3
        kitty_x = width - kitty_table_width - table_margin
        hypr_x  = table_margin
        kitty_pad.refresh(kitty_pointer, 0, kitty_y, kitty_x, 55, width)
    else:
        # Case - 2 -- One Table on top of other
        case2 = True
        hypr_x = (width - hypr_table_width) // 2
        kitty_x = (width - kitty_table_width) // 2
        kitty_y = len(hypr_table_arr)
        kitty_pad.refresh(kitty_pointer, 0, kitty_y, kitty_x, 55, width)
    
    # curses.napms(2000)
    hypr_pad.refresh(hypr_pointer, 0, hypr_y, hypr_x, height, width)
    # print(f'height: {height}, width: {width}')

    # curses.napms(3000)
    stdscr.addstr(height - 2, 0, f'height={height}, width={width}')
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('j') or key == curses.KEY_DOWN:
            if hypr_pointer < len(hypr_table_arr)-1:
                hypr_pointer+=1
                # kitty_pointer+=1
            if case2:
                kitty_y -= 1
            elif kitty_pointer < len(kitty_table_arr)-1:
                kitty_pointer+=1
            hypr_pad.refresh(hypr_pointer, 0, hypr_y, hypr_x, height, width)
            kitty_pad.refresh(kitty_pointer, 0, kitty_y, kitty_x, 55, width)
 
        elif key == ord('k') or key == curses.KEY_UP:
            if hypr_pointer > 0:
                hypr_pointer-=1
                # kitty_pointer-=1
            if case2:
                kitty_y += 1
            elif kitty_pointer > 0:
                kitty_pointer -=1

            hypr_pad.refresh(hypr_pointer, 0, hypr_y, hypr_x, height, width)
            kitty_pad.refresh(kitty_pointer, 0, kitty_y, kitty_x, 55, width)
            
       # curses.napms(3000)
# print(table_margin)
print('kitty table width: ', kitty_table_width)
print('hypr table width: ',  hypr_table_width)
print(f'len of kitty table : {len(kitty_table_arr)}')

curses.wrapper(main)
