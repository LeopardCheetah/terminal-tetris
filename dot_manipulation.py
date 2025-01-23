import keyboard

"""
# function get_pressed
# requires an input of type keyboard.KeyboardEvent (meant to be used after being hooked up to a keyboard.hook())
# returns both the string of the key pressed (whether that be 'a', 'ctrl', etc.) and whether the key was pushed "down" or pushed "up" (let go)
def get_key_pressed(event):
    # event is of type `keyboard.KeyboardEvent` (aka link this up directly to keyboard.hook)
    
    # print(type(event), event, str(event))
    # so it seems like the string version of event and the other event are the same
    _to_parse_event = str(event)
    _to_parse_event = _to_parse_event[14:-1] # this leaves just the letter and the other thing

    _ind = _to_parse_event.rfind(' ') # returns last ' ' index
    _up_or_down = _to_parse_event[_ind:]
    _char_pressed = _to_parse_event[:_ind]

    '''
    note:
    the following keys are two words long (separated by space):
    - caps lock
    - left windows 
    - right windows
    - page up
    - page down (see the bottom right on my keyboard)
    - Unknown 99 (this is the left most fn on my keyboard)
    - print screen
    
    definitely add some sort of disclaimer telling people not to press on these or something
    '''

    return str(_char_pressed), str(_up_or_down[1:]) # the [1:] is needed as otherwise there would be a space



def track_down_key_presses(event):
    # not using the dummy variable

    _char, _up_down = get_key_pressed(event)

    if _up_down == 'up':
        return # we don't want to duplicate anything


    print(f'{_char} has just been pressed!')
    return 





# keyboard.hook(track_down_key_presses)

# program closes when ctrl + q happens
# keyboard.wait(hotkey='ctrl+q')

"""

class DotManipulation():
    dotx = 10 # 10th index from the edge (9 spaces)
    doty = 10 # 10th line (9 lines printed)
    maxx = 60
    maxy = 20


    def __init__(self, dotx = 20, doty = 10, maxx = 60, maxy = 20):
        self.dotx = dotx
        self.doty = doty

        self.maxx = maxx # the "grid" that's being worked with -- grid cannot exceed maxx by maxy
        self.maxy = maxy 
        # yippee

   
    def clear(self):
        print('\033[2J\033[H') # clears the terminal screen
        return 

    def printboard(self):
        self.clear()
        
        print('\n'*(self.doty - 1))
        print(' '*(self.dotx - 1), end='')
        print('.')
        print()

        return 
    
    def getx(self):
        return self.dotx
    
    def gety(self):
        return self.doty 
    
    def setx(self, x):
        # i should probably validate x is an integer but nah

        # validate bounds
        if x < 0 or x > self.maxx:
            return 

        self.dotx = x
        return 
    
    def sety(self, y):
        if y < 0 or y > self.maxy:
            return 
        self.doty = y
        return



# these only work on a windows terminal
def show_cursor():
    print('\033[?25h', end="")
    return

def hide_cursor():
    print('\033[?25l', end="")




screen = DotManipulation()
hide_cursor()


while True:
    # Wait for the next event.

    screen.printboard() # note: in later iterations, this may need to be updated (instead of a simple static board)

    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
        break # leave loop
    
    if event.event_type == keyboard.KEY_DOWN and event.name == 'up':
        # move dot up
        screen.sety(screen.gety() - 1)
        continue

    
    if event.event_type == keyboard.KEY_DOWN and event.name == 'down':
        screen.sety(screen.gety() + 1) # if this fails its whatever
        continue
    
    if event.event_type == keyboard.KEY_DOWN and event.name == 'left':
        screen.setx(screen.getx() - 1)
        continue 
    
    if event.event_type == keyboard.KEY_DOWN and event.name == 'right':
        screen.setx(screen.getx() + 1)
    
print('execution stopped.')
show_cursor()


# print('\r' + 'rem ', end='')
print('\033[13')