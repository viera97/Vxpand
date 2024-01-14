from pynput import keyboard
from keywords import words

controller = keyboard.Controller()


buffer = ""

def on_press(key):
    global buffer
    
    try:
        key = key.char
    except AttributeError:
        return
    
    buffer += key
    
    if buffer in words:
        for i in range(len(buffer)):
            controller.press(keyboard.Key.backspace)
            controller.release(keyboard.Key.backspace)

        controller.type(words[buffer])
        buffer = ""
        
    else:
        prefix = False
        for word in words:
            if word.startswith(buffer):
                prefix = True
                break
        if not prefix:
            buffer = ""

print("Starting Service")

try:
    with keyboard.Listener(on_press=on_press) as listener:
        print('Service Started Successfully')
        listener.join()
except:
    print('Starting Service Failed')