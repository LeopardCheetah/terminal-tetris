import keyboard 
import time
import random
import sys



###########
###########
###########



# function clear() clears the screen by printing a special driver code
def clear():
    print('\033[2J\033[H')
    return 


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





# clear()
# time.sleep(1)


# 4 inputs/piece * ~2pps = 8 inputs/s -- this is what my program should AT LEAST be able to accomodate
# probably should accomodate up to 10 inputs/s


# manipulate a dot
# i need to track key presses in some way -- when L key is pressed or something like that




# keyboard.hook(track_down_key_presses)
# keyboard.wait(hotkey='ctrl+q')
